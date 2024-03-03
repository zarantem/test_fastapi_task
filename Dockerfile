FROM python:3.10-slim-buster

COPY pyproject.toml

WORKDIR .

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]