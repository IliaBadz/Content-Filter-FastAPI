import openai

from app.settings.config import settings


API_KEY = settings.api_key
TOXIC_THRESHOLD = -0.355


def _output(content_to_classify: str) -> dict:
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine="content-filter-alpha",
        prompt="<|endoftext|>" + content_to_classify + "\n--\nLabel:",
        temperature=0,
        max_tokens=1,
        top_p=0,
        logprobs=10
    )

    return response


def _check_logprob(output_label, logprobs) -> str:

    if output_label == "2":
        if logprobs['2'] < TOXIC_THRESHOLD:
            logprob_0 = logprobs.get('0', None)
            logprob_1 = logprobs.get('1', None)

            if logprob_0 is not None and logprob_1 is not None:
                if logprob_0 >= logprob_1:
                    output_label = "0"
                else:
                    output_label = "1"

            elif logprob_0 is not None:
                output_label = "0"
            elif logprob_1 is not None:
                output_label = "1"

    if output_label not in ['0', '1', '2']:
        output_label = '2'

    return output_label


def filter_text(content_to_classify: str) -> int:

    response = _output(content_to_classify)
    output_label = response['choices'][0]["text"]
    logprobs = response['choices'][0]['logprobs']['top_logprobs'][0]

    return int(_check_logprob(output_label, logprobs))
