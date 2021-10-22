FROM python3.7

ADD . .

EXPOSE 8080:8080

ENTRYPOINT ["sh deploy.sh"]
