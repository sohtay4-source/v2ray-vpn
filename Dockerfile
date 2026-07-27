FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip && \
    curl -L -o /tmp/v2ray.zip https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip && \
    unzip /tmp/v2ray.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/v2ray && \
    apt-get remove -y curl unzip && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

EXPOSE 8080

CMD ["python3", "run.py"]
