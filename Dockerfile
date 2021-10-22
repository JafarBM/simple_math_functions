FROM python3.7

RUN apt update && apt install -y ca-certificates && \
    echo $TZ > /etc/timezone && \
    apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

# Maybe you will need to reconfigure the timezone as well:
ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
dpkg-reconfigure -f noninteractive tzdata

ADD . .

EXPOSE 8080:8080

ENTRYPOINT ["sh deploy.sh"]
