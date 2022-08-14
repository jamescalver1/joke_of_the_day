# joke_of_the_day

This application scrapes and returns the current joke of the day from https://www.ajokeaday.com/ via the following endpoint :

http://ec2-18-133-64-83.eu-west-2.compute.amazonaws.com:8888/joke_of_the_day

The application is written in Python.

Beautifulsoup4 to used scrape the current joke of the day. 

Flask is used to create the API.

The application is dockerised and hosted via AWS ECS running on a t2.micro EC2 instance.
