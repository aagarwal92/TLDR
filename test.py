import urllib2
import json
import re
import pickle 

'''data = urllib2.urlopen("http://www.reddit.com/reddits/new/.json")
test = data.read();
result = json.loads(test);
'''
after = "--"

#result["data"]["after"]#
my_dict = []

regex = re.compile("/r/([a-zA-Z0-9]+)/?\)")

def cat_description(result):
    for subcat in result["data"]["children"]:
        catname = subcat["data"]["display_name"]
        if catname != "reddit.com":
            subnum = subcat["data"]["subscribers"]
            subreddits = subcat["data"]["description"]
            if subreddits != None:
                subreddits1 = regex.findall(subreddits)
                my_dict.append({
                    "catname" : catname,
                    "subnum" : subnum,
                    "subreddits" : subreddits1
                })

            
def next_page(after):
    data = urllib2.urlopen("http://www.reddit.com/reddits/new/.json?after=" + after)
    test = data.read();
    result = json.loads(test);
    return result

pagenum = 1

while after!= None:
    try:
        print "Page Number: " + str(pagenum)
        result = next_page(after)
        cat_description(result)
        after = result["data"]["after"]
        pagenum += 1
        print after
    except:
        pass
    if after == "":
        break
    
print "finished"

output1 = open('popularRedditData.pkl', 'wb')
pickle.dump(my_dict, output1)
output1.close()