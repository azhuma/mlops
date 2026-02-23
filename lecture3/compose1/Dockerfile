FROM python:3
WORKDIR /app
COPY ./app .
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "color_boxes:APP"]
