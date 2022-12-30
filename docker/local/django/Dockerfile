# pull the official base image
FROM python

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# set level
LABEL maintainer='sizanmahmud08@gmail.com'
LABEL description="Development image for home_sale project"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# SHELL ["/bin/sh", "-c"]
ENTRYPOINT [ "/entrypoint" ]


EXPOSE 8008

# CMD ["--help"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]