1.a. With docker-compose:
    docker-compose up -d

1.b. Or with Docker:
    docker build -t python_image --rm .
    docker run -dit --name python_app --rm --mount type=bind,source=/c/Users/GourouzaT/Documents/perso/python/data,target=/home/thomas/data python_image

2. And then:
    docker exec -it <container-name-or-id> bash
