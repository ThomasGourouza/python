FROM python:latest
RUN useradd --create-home --shell /bin/bash thomas
WORKDIR /home/thomas
USER thomas
ENTRYPOINT ["bash"]