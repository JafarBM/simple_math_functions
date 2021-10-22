FROM python:3.7

ENV TZ 'Asia/Tehran'

RUN apt update && apt install -y ca-certificates && \
    echo $TZ > /etc/timezone && \
    apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

ADD . .

RUN make dependencies

EXPOSE 8080:8080

ENTRYPOINT ["sh deploy.sh"]
