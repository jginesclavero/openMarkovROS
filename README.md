# openMarkovROS

This package connects a ROS node with the application OpenMarkov developed by UNED [1]. It was developed within our project in Context Awareness in Social Robots for indoors environments. 

## Abstract
Facing long-term autonomy with a cognitive architecture raises several difficulties for processing symbolic and sub-symbolic information under different levels of uncertainty, and deals with complex decision-making scenarios.For reducing environment uncertainty and simplifying the decision-making process, this paper establishes a method for translating robot knowledge to a Conceptual Graph to later extract probabilistic context information that allows to bound of the actions present at the deliberative layer.This research develops two ROS components, one for translating robot knowledge to the Conceptual Graphs and one for extracting context knowledge from this graph using Bayesian Networks.We evaluate these components in a real-world scenario, performing a task where a robot notifies to a user a message of an event at home. Our results show an improvement in task completion when using our approach, decreasing the planning requests by 65\% percent and doing the task in a third of the time.


# Installation

Requeriments:
 - Eclipse
 - Py4J [2]
 - OpenMarkov repos [1]
 - ExampleApi repo
 - OpenMarkov-roswrap

Install Eclipse and Py4J:
- sudo snap install eclipse --classic
- pip install py4j

Clone OpenMarkov repos and our ROS API (ExampleApi):
- create a directory to contains the repos - mkdir ~/openmarkov
- cd ~/openmarkov
- Follow the official steps to clone the repos - https://bitbucket.org/cisiad/org.openmarkov/wiki/resources/User%20repositories%20-%20script
- Clone the ROS API repo in the same location - https://github.com/jginesclavero/org.openmarkov.exampleapi

Importing OpenMarkov to Eclipse:
- Open eclipse and go to File > Import > Maven > Existing Maven Projects
- Select your openmarkov folder > Finish and wait a moment

Import Py4J to ExampleApi:
- Locate the repo in Eclipse - org.openmarkov.exampleAPI
- Right Click > New > Folder > Folder Name: lib
- Locate your Py4J .jar, usually is in ~/.local/share/py4j or in /usr/local/share/py4j
- Copy or Drag&Drop the .jar in the folder created before.
- In Eclipse, Right Click in the .jar copied > Build Path > Add to Build Path

Clone and compile OpenMarkov-roswrap:
- Clone this repo in your ROS workspace and compile - catkin_make


# Testing the API

Execute OpenMarkov Eclipse API:
- Open the ExampleAPI in Eclipse and Run.

ROS:
- Init a roscore
- Execute the openMarkov-roswrap: rosrun openmarkov_roswrap openMarkovROS_node.py

Getting probs:
- rosservice call /openmarkov_ros/get_var_probs "variable: 'HumanLocalization'"

Setting a new finding:
- rosservice call /openmarkov_ros/set_finding "variable: 'AcousticSignals' state: 'microwave'"


# Cite Us

Please, cite us if you use this software in your research:

``` 
@article{gines2020depicting,
     title     = {Depicting probabilistic context awareness knowledge in deliberative architectures},
     author    = {Gin{\'e}s, Jonatan and Rodr{\'\i}guez-Lera, Francisco J and Mart{\'\i}n, Francisco and Guerrero, {\'A}ngel Manuel and Matell{\'a}n, Vicente},
     journal   = {Natural Computing},
     pages     = {1--12},
     year      = {2020},
     publisher = {Springer}
}
```


# References

[1] http://www.openmarkov.org/

[2] https://www.py4j.org/install.html
