FROM alpine:3.12

WORKDIR /usr/app

COPY fibonacci.sh .

ENV VAR=5

RUN VAR=$VAR ./fibonacci.sh
