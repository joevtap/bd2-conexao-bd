FROM python:3.11.5-slim
RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app
COPY . .
CMD [ "bash" ]