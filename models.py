FROM python:3.8

ADD . /List_Task1
WORKDIR /List_Task1
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
