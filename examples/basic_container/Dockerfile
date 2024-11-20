FROM python:3.11


WORKDIR /app

#to COPY the remote file at working directory in container
COPY main.py ./
COPY requirements.txt ./
COPY src/ ./src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./main.py"]
