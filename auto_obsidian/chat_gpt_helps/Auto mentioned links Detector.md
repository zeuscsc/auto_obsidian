### Auto mentioned links Detector
I would like to make a bot that detects when a user mentions a link and automatically links it for them. 
I want the longest link to be linked.
The way to link a link is to put it in 2 square brackets.
Please write the program in Python.
Here is an example of what I mean:
~~~python
article="""
###### But is this the most likely weather that happened?
From the argmax of the Transition matrix above, we know that the most likely event that will happen will be Sunny Sunny Cloudy 0.04105
"""
mentions=["Transition Matrix", "Matrix"]
output_article=auto_mentioned_links_detector(article, mentions)
~~~
output_article:
###### But is this the most likely weather that happened?
From the argmax of the [[Transition matrix]] above, we know that the most likely event that will happen will be Sunny Sunny Cloudy 0.04105


### Detect if sentence is wrapped in 