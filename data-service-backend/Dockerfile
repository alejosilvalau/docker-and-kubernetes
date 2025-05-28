FROM python:3.12-alpine3.19

#
# NOTE: Application reads contents of /data in container
# If not found, application returns errors.
# 

WORKDIR /app
ENV FLASK_RUN_HOST=0.0.0.0

COPY code/app.py .
COPY code/requirements.txt .

RUN pip install -r requirements.txt --root-user-action=ignore

EXPOSE 5000

CMD ["flask", "run"]
