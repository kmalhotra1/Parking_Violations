# Parking Violations Analysis

[Dataset Link](https://data.cityofnewyork.us/resource/nc67-uf89.json)

# Executive Summary
This analysis will load and then analyze a subset (n=200,000) of a dataset containing millions of NYC parking violations since January 2016. In completing this analysis, the following skills will be leveraged: principles of containerization, terminal navigation, python scripting, artifact deployment, AWS EC2 provisioning, and Kibana. An overview of the vast majority of steps taken to conduct this analysis are depicted below for the reader. Towards the conlusion, we will visualize a few intersting insights/relationships by leveraging Kibana.
____________________________________________________________________________________________________________________________

# Part 1: Python Scripting

### Create the necessary folders and cd into the directory. Once the environment is properly contained, we can begin deployment.

1) Login to docker via terminal:\
&nbsp;&nbsp;&nbsp;&nbsp;- docker login --username=krm444

2) Build the image in terminal:\
&nbsp;&nbsp;&nbsp;&nbsp;- docker build -t bigdata1:1.0 .
  
3) Obtain the UUID of the newly built image:\
&nbsp;&nbsp;&nbsp;&nbsp;- docker images | grep bigdata1

4) Tag the image (UUID) with 2 elements: dockerhub username (make sure username is lowercase) + version number\
&nbsp;&nbsp;&nbsp;&nbsp;- docker tag {UUID} krm444/bigdata1:1.0

5) Push the docker image WITHOUT the version number:\
&nbsp;&nbsp;&nbsp;&nbsp;- docker push krm444/bigdata1

6) Run it to visualize data:\
&nbsp;&nbsp;&nbsp;&nbsp;- docker run -e APP_KEY={YOUR_APP_KEY} -it bigdata1:1.0 python -m main --page_size=4 --num_pages=4 --     output=results.json


## Following are two sample outputs:

### 1) page_size = 1 and num_pages = 1
![](Images/2.png)

### 2) page_size = 2 and num_pages = 1
![](Images/1.png)

### That's all folks, it should be deployed to Dockerhub. On your docker, just click into the repo to make sure.
____________________________________________________________________________________________________________________________
