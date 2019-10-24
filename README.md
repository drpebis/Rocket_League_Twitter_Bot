# Rocket_League_Twitter_Bot

A helpful twitter bot written in python to combat toxicity in Rocket League.

It is currently live at: https://twitter.com/helper_rl go check it out!

# Collecting and responding via text metrics

Adding code to collect the overall sentiment of tweets sent to this bot over the course of a day. The bot will then respond to a specific que tweet and display how positive/negative the tweets are. 

# Dockerized

The provided `Dockerfile` and `docker-compose.yml` files will enable you to
run the script inside of a Docker container. This should make it more portable
and will allow you to run it pretty much anywhere in the same fashion.

Ensure you have Docker and Docker Compose installed on your local machine and wherever you want
the script to run.

### Building the Image

```
$ docker build -t rl_helper_bot:latest .
```

### Running the Container

```
# Run container in foreground
$ docker run --rm rl_helper_bot:latest
# Run container in background
$ docker run --rm -d rl_helper_bot:latest
```

You can also use `docker-compose`:

```
# Foreground
$ docker-compose up --build
# Background
$ docker-compose up --build -d
```

You can also shell into the container and inspect the internals - useful for debugging

```
$ docker run --rm -it rl_helper_bot:latest /bin/sh
```



