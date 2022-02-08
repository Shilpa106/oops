# importing dataclass module
from dataclasses import dataclass

@dataclass
class GfgArticle():
    '''A class fo holding an article content'''

    # attributes declaration
    title:str
    author:str
    language:str
    upvotes:int


# A DataClass object
article = GfgArticle("DataClasses","vagr","python",9)
print(article)
