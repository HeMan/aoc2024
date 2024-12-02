FROM python:alpine
COPY . /solution
RUN pip --no-cache-dir install -r /solution/requirements.txt
WORKDIR /solution

CMD ["python", "solution.py"]
