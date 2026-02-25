FROM python:3.10
WORKDIR /app
COPY bookmarks .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
CMD ["uwsgi", "bookmarks_uwsgi.ini"]
