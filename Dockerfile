FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5117

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "5117" ]