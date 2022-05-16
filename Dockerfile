FROM python:3.9.6-slim-buster


ENV PYTHONFONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
	&& apt-get -y install netcat gcc \
	&& apt-get clean

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv /opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install --upgrade pip
ADD ./requirements.txt /project/
RUN pip install -r /project/requirements.txt

COPY ./project ./project

ENV PYTHONPATH=/project


WORKDIR /project/

CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]


