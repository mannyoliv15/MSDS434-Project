FROM python:3.8

WORKDIR /cloudrun_MSDS434
ADD . /cloudrun_MSDS434


RUN pip install -r requirements.txt

CMD [ "python" , "/cloudrun_MSDS434/app.py" ]

ENV HOME=/cloudrun_MSDS434