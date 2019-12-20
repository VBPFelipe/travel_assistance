# travel_assistance


# Linux

Open a terminal screen:

  ```python index.py```

In another terminal to send request (HTTP POST):

  ```curl -H "Content-Type: application/json" -X POST '[JSON]' http://[localhost_url]:5000/json```

On browser to get request (HTTP GET):

  ```http://[localhost_port]:5000/read```


---------------------------

It's also possible to do tunnelling with NGrok.

It's necessary to build NGrok with the same port which is used in the project (5000).

On terminal:

  ```ngrok http 5000```

And, replace the local url with that one given by ngrok tunneling when built, adding the url sufixes.

i.e.:

    to POST - curl -H "Content-Type: application/json" -X POST '[JSON]' [ngrok_tunneling_url]/json
    to GET  - [ngrok_tunneling_url]/read
