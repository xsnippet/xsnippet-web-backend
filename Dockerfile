FROM python:latest
MAINTAINER The XSnippet Team <dev@xsnippet.org>

COPY . /app
WORKDIR /app
RUN pip install -e .

EXPOSE 5000
ENTRYPOINT ["python", "-m", "xsnippet.web_backend"]
