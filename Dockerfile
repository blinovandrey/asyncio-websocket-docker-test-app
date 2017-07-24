FROM daocloud.io/library/python:3.6.1

RUN apt-get update

RUN mkdir /code
ADD . /code

WORKDIR /code
RUN pip3 install aiohttp aiohttp_jinja2 asyncio

EXPOSE 7000

CMD ["/usr/local/bin/python", "-u", "server.py"]