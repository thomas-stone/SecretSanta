FROM python:3.9-alpine
WORKDIR /
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./backend /src/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]