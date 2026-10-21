# To use this file,
## 1. Go to your terminal.
###2.Run:   pip install tavily-python
####3.Run:   pip install dotenv

from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()
myfirstClient = TavilyClient()
userInput = input("Search:")
response = myfirstClient.search(userInput)
print(response)
#And there you have it! You just allowed a user to execute a "terminal" web search!
