# Pull official base image
FROM python:3.8.2-alpine

# Set work directory
WORKDIR /usr/src/portfolio

# Set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install Pillow dependencies
RUN apk add jpeg-dev zlib-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copy project
COPY . .

# Run entrypoint.sh
ENTRYPOINT [ "/usr/src/portfolio/entrypoint.sh" ]