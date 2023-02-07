# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

WORKDIR /app

EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# copy neccessary file to the code
COPY ./requirements.txt /app/requirements.txt
COPY ./prisma /app/prisma

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN sleep 10
RUN prisma db push 
RUN prisma generate

COPY . /app


# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# CMD ["uvicorn", "main:app"]
# CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]`
