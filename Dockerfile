FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN chmod +x ./main.py
ENTRYPOINT ["python", "./main.py"]