#!/bin/bash

sudo docker run -idt -p 8000:8000 -v /home/ubuntu/kkugong:/root/kkugong --name=kkugong seungsu3579/python:1.1 /bin/bash

sudo docker run -idt -p 10001:10001 -v /home/ubuntu/clothesToVector:/root/clothesToVector -v /home/ubuntu/kkugong:/root/kkugong --name=vectorization seungsu3579/ield_vision:1.1 /bin/bash

sudo docker run -idt -p 8888:8888 -v /home/ubuntu/recommand:/root/recommand --name=recommand seungsu3579/ield_vision:1.1 /bin/bash