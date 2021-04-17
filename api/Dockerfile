FROM python:latest

RUN mkdir /code
WORKDIR /code

COPY entrypoint.sh /code/entrypoint.sh
COPY apps/ /code

## PIPインストールおよび
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/code/"
ENV FLASK_APP "/code/server.py"
CMD ["/code/entrypoint.sh"]