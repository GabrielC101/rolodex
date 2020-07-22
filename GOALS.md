## Goals

While writing this code, I strived to ensure reusability, deployability, reliability, and extensibility. 


To ensure reusability;

* This application includes a mini framework to create schemes for tabular data, like CSVs 
("first element must be a string, second must be a string, third must be a string of length==5 containing only 
numerals, etc"). 

* This application includes custom readers, writers, and tokenizers. 
These classes integrate with each other to make the read, translate, write process configurable. 
For example, if a user wanted to add email address as a column on the CSV, 
it would be easy and only change a few lines of code.

To ensure deployability:
* This application includes Dockerfiles, requirements files, and a Makefile to automate deployment and 
dependency resolution.

To ensure reliability:

* This application includes unit tests using the pytest framework. There is even a Dockerfile that creates an image 
that runs the tests and verifies the code is working. In a real-world situation, this might be a separate Jenkins task.

To ensure extensibility:
* This application includes methods (not fully implemented) to allow the reading and writing of files from cloud 
services. This is basically a Todo, but the code is ready for it to be done.

The code is very high quality. It's what I would write for production. It also shows my ability to use design 
patterns, and work in a cloud environment.
