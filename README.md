# Content-Filter-FastAPI
This is a simple FastAPI project that uses OpenAI's `Content filter` engine to filter a text. After providing text the outcome could be one of three possible results: 
1. Text is safe.
2. Text is sensitive.
3. Text is unsafe.


## How to run

1. Clone this repository to your local machine.

2. Add API_KEY to the `.env` file. Key could be generated on the OpenAI's website after registration. 

3. Run following command from the root: `docker-compose up --build`

4. Open your browser at http://127.0.0.1:8000/docs to see API documentation
