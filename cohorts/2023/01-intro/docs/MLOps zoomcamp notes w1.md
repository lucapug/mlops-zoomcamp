# MLOps Zoomcamp Notes Week1

Sun, May 21, 2023 3:39 PM

## Setup of the development environment for the course

In a video of this week, Alexey shows how to setup a rented VM in AWS with these characteristics: 

* Ubuntu 22.04, 
* 16GB of RAM, 
* instance type t3.xlarge (4 vCPU), 
* 30GB of EBS storage. 

The instance type is outside of the free tier resources; an approximate estimate for a workload of `10hrs/week` is `10-20$/month`.

My personal setup is depicted in the figure below. I have duplicated the dev environment (both cloud and local). It is clearly redundant with respect to the needs of the course; my scope is to learn how to work in the cloud but to be safe with respect to cloud expenses, by doing the most of my work locally. <strong>I can do so, because I have sufficient local hardware resources</strong>.

![schema dev environment](.media/img_0.png)

To have all development jobs in sync between local and cloud dev environments, I have created a centralized Github repo that is a fork of the DataTalkClub course repo. This allows me to update my fork from the source repo without pushing back my personal course activities.