FROM python:3.11-slim

# Install V2Ray
RUN apt-get update && apt-get install -y curl unzip && \
    curl -L -o /tmp/v2ray.zip https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip && \
    unzip /tmp/v2ray.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/v2ray && \
    apt-get remove -y curl unzip && apt-get clean

COPY config.json /etc/v2ray/config.json

# Copy healthcheck server
COPY healthcheck.py /app/healthcheck.py

EXPOSE 80 8080

CMD ["sh", "-c", "python3 /app/healthcheck.py & v2ray run -c /etc/v2ray/config.json"]
