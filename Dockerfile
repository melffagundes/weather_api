FROM python:3.9
# Run commands from /app directory inside container
WORKDIR /src


# Copy requirements from local to docker image
COPY . /src
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

COPY . .
ENTRYPOINT [ "flask"]
CMD [ "run"]
