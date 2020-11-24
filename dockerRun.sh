#!/bin/bash

sudo docker run -idt -p 8000:8000 -v /home/ubuntu/kkugong:/root/kkugong --name=kkugong seungsu3579/python:1.1 /bin/bash

sudo docker run -idt -p 10001:10001 -p 10002:10002 -p 10003:10003 -v /home/ubuntu/clothesToVector:/root/clothesToVector -v /home/ubuntu/kkugong:/root/kkugong --name=vectorization seungsu3579/ield_vision:1.1 /bin/bash

sudo docker run -idt -p 10011:10011 -p 10012:10012 -p 10013:10013 -p 10014:10014 -v /home/ubuntu/recommender:/root/recommender --name=recommend seungsu3579/ield_vision:1.1 /bin/bash
