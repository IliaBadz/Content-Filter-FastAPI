from enum import Enum

from app.settings.config import settings

import openai

API_KEY = settings.api_key
TOXIC_THRESHOLD = -0.355


class Output(Enum):
    safe = '0'
    sensitive = '1'
    unsafe = '2'


def _output(content_to_classify: str) -> dict:
    openai.api_key = API_KEY

    sampling_temperature = 0  # Higher values means model will take more risks. Lower values make model confident
    max_tokens = 1  # The maximum number of tokens to generate in the completion
    top_p = 0  # Nucleus sampling. Model considers the results of the tokens with top_p probability mass
    logprobs = 10  # Include the log probabilities on the logprobs most likely tokens

    response = openai.Completion.create(
        engine="content-filter-alpha",
        prompt="<|endoftext|>" + content_to_classify + "\n--\nLabel:",
        temperature=sampling_temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        logprobs=logprobs
    )

    return response


def _check_logprob(output_label: str, logprobs: dict) -> str:

    if output_label == Output.unsafe.value:

        # If the logprob for 2 is beneath -0.355,
        # then we should use as output whichever of 0 or 1 has a logprob closer to 0

        if logprobs[Output.unsafe.value] < TOXIC_THRESHOLD:
            logprob_safe = logprobs.get(Output.safe.value, None)
            logprob_unsafe = logprobs.get(Output.sensitive.value, None)

            if logprob_safe is not None and logprob_unsafe is not None:
                if logprob_safe >= logprob_unsafe:
                    output_label = Output.safe.value
                else:
                    output_label = Output.sensitive.value

            elif logprob_safe is not None:
                output_label = Output.safe.value
            elif logprob_unsafe is not None:
                output_label = Output.sensitive.value

    if output_label not in [Output.safe.value, Output.sensitive.value, Output.unsafe.value]:
        output_label = Output.unsafe.value

    return output_label


def filter_text(content_to_classify: str) -> int:

    response = _output(content_to_classify)
    output_label = response['choices'][0]["text"]
    logprobs = response['choices'][0]['logprobs']['top_logprobs'][0]
    checked_result = _check_logprob(output_label, logprobs)

    return int(checked_result)
