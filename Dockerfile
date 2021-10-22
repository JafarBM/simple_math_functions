FROM python3.7

ADD . .

ENTRYPOINT ["sh deploy.sh"]
