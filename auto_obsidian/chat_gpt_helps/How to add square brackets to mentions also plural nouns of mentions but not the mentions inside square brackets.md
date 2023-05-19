How to add square brackets to mentions also plural nouns of mentions but not the mentions inside square brackets
You can detect plural using library such as inflect
Example:
mentions=["car"]
Input="I go to school by [car], but I don't like car. Yet cars are good."
Output="I go to school by [car], but I don't like [car]. Yet [cars] are good."