from os import listdir
from os.path import isfile, join
from urllib import request
from urllib.request import Request, urlopen, urlretrieve
import json

url1 = 'https://api.github.com/orgs/Mirantis/repos'
f1 = open('./Mirantis_repos/Mirantis_repos_extraction', "w", encoding='utf-8')
request_gitapi = Request(url1, headers={
                             "authorization": "Bearer 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 "})
url = urlopen(request_gitapi)
data = json.load(url)
f1.write( "id"+ ", "+"name"+", "+"full_name"+", "+ "private"+ ", "+"fork"+ ", "+ "language" + "\n" )
for x in data:
    #f1.write(x["id"])
    f1.write( str(x["id"])+ ", "+ x["name"]+", "+x["full_name"]+", "+ str(x["private"])+ ", "+str(x["fork"])+ ", "+ str(x["language"]) + "\n" )


