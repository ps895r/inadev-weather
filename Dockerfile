FROM python:3.12.1-slim-bookworm
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install requests
COPY . .
EXPOSE 5000
ENV FLASK_APP=weather.py
CMD ["flask", "run", "--host", "0.0.0.0"]
