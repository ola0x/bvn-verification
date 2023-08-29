# frontent/Dockerfile

FROM python:3.8-slim-buster

RUN apt-get update -y --no-install-recommends

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]