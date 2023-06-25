FROM pypy:latest
WORKDIR /app

# copies app into folder
COPY . /app

# sets up the environment to run app
RUN pip3 install -r requirements.txt
COPY . . 

# execute py files in order
CMD ["python", "manage.py", "runserver"]
