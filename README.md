# BEON
## _Python/Django Challenge_

### Requirements

- Docker (last version)

### Running env


1. Build the store image

```text
docker build --no-cache -t  service/store:1.0.0 -f ./docker/local/store/Dockerfile ./
```

2. Run the docker env

```text
docker-compose --profile local up
```

3. Execute migrations and create the first user

```text
docker exec -ti store /bin/bash
```
```text
./manage.py migrate
```

```text
./manage.py createsuperuser
```

4. Restart the store container
```text
docker container restart store
```

5. Start your challenge!
