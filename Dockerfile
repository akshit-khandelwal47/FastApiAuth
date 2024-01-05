FROM python

WORKDIR /fastapiauth

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /fastapiauth

CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port=8000"]

EXPOSE 8000