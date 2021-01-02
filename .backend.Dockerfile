FROM python:3.7

COPY django-polls /django-polls
WORKDIR /django-polls
RUN python setup.py sdist
RUN pip install dist/django-polls-justas-0.1.tar.gz

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD mysite /my-django-app

WORKDIR /my-django-app
