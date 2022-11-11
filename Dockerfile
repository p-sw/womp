FROM python:3.10.7

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel
RUN pip install --upgrade pipenv

# Install app
COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy

# Run app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]