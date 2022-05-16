# Content-Filter-FastAPI
This is a simple FastAPI project that uses OpenAI's `Content filter`, a fine-tuned model that can detect whether text may
be sensitive or unsafe. It is in beta mode thus results might not be always correct. For current project's purposes text should be provided through `/app/v1/text/filter` endpoint. 

In order to generate results you will need OpenAI API Key. Key should be generated on the OpenAI's website after registration ([see docs](https://beta.openai.com/docs/api-reference/authentication)). 

After providing text the outcome could be one of three possible results: 
1. Text is safe.
2. Text is sensitive.
3. Text is unsafe.

For further details about OpenAI's module please refer to the [official documentation](https://beta.openai.com/docs/engines/content-filter).


## How to run

1. Clone this repository to your local machine

2. Add OPENAI_API_KEY to the `.env` file in `Content-Filter-FastAPI/project` 

3. Run following command from the root: `docker-compose up --build`

4. Open your browser at http://127.0.0.1:8000/docs to see API documentation