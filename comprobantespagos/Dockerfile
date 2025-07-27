FROM python:3.11-slim-bullseye
WORKDIR /comprobantespagos
COPY . /comprobantespagos
## COPY .env.development .env
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy
RUN pip install flask
## RUN export $(cat .env | xargs)
EXPOSE 3001
ENV FLASK_APP=/comprobantespagos/api/__init__.py
## ENV ENVIROMENT=.env.development
ENV PYTHONUNBUFFERED=1
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "-p", "3001"]