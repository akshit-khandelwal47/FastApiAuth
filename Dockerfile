FROM python:3.11

WORKDIR /FastApiAuth

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./FastApiAuth /FastApiAuth

CMD ["uvicorn", "FastApiAuth.main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000