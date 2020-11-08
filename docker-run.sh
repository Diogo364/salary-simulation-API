docker run --rm -it \
--name salary-simulation \
-p 5000:5000 \
-v $( pwd )/data:/app/data \
flask-salary-simulation
