FROM python:3.8

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

#Create the home directory and add files
WORKDIR /cloudrun_MSDS434
ADD . /cloudrun_MSDS434

## Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install flask gunicorn transformers

# Now copy the app
COPY ./app.py .

# Run the web service on container startup. Here we use gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 1 --timeout 0 app:app