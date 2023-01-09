# Base image
FROM python:3.10.8-bullseye

# Create a work directory
WORKDIR /opt

# Copy the file containing dependencies
COPY ./requirements.txt .
COPY ./test_requirements.txt .

# Install the dependencies using the copied file
RUN pip install --no-cache-dir --upgrade -r test_requirements.txt \
    && pip-chill

# Copy the source code
COPY ./src .

# Entry point. Run the app
CMD ["python", "./my_app/main.py", "host", "0.0.0.0","--port", "8005"]
