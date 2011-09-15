import pickle
import os
import json
from TreeNode import TreeNode
  
input = open('popularRedditData.pkl', 'rb') # "rb" for read binary #
file_data = pickle.load(input) # this will give you the array of subreddit dictionaries back #
input.close()

reddit = TreeNode({
    "catname" : "Reddit",
    "subnum" : 200000,
    "subreddits" : []
})

nodes = []
useful_nodes = []
dict_names = {}
txt2=0  
nodecount = 0
origcount = 0
tt = 0

for item in file_data:
    nodes.append(TreeNode(item))

for node in nodes:
    origcount = origcount + 1
    dict_names[node.name.lower()] = node
    if node.subscribers >= 1000:
        useful_nodes.append(node)
        txt2 = txt2+1
        
print origcount
print "nodes after removing useless one %d" % txt2
for node in useful_nodes:
    nodecount = nodecount + 1
print "node count of those over 1000 subs. %d " % nodecount

#add child to parents...essentially creates a tree with parents and children of sub-reddits#    
for node in nodes:
    for childName in node.suggested_children:
        if childName in dict_names:
            child = dict_names[childName]
            #print "Child %s has been appended to the ditionary" % child.name
            if child != node:
                if child.parent is not None and node.subscribers > child.parent.subscribers:
                     child.parent.remove_child(child)
                     node.add_child(child)
                     #print "Child %s has been added/removed" % child.name
                if child.parent is None:
                     node.add_child(child)




''' dumps the data into a pkl
output2 = open('UsefulRedditsTest.pkl', 'wb')
pickle.dump(useful_nodes, output2)
output2.close()
'''

txt = 0
nodecount = 0

output2 = open('UsefulRedditsTest2.pkl', 'wb')
pickle.dump(nodes, output2)
output2.close()

#opens the useful reddits and appends them to a dictionary#
input2 = open('UsefulRedditsTest2.pkl', 'rb') # "rb" for read binary #
file_data2 = pickle.load(input2) # this will give you the array of subreddit dictionaries back #
input2.close()

nodes2 = []
dict_names2 = []
nodecount = 0

fileCount = 0
for item in file_data2:
    fileCount = fileCount + 1    
    nodes2.append(item)

print "number of reddits in the new dictionary %d " % fileCount


nodecount = 0
for node in nodes2:
        if node.subscribers < 1000:
            nodecount = nodecount+1
        if node.subscribers is None:
            print "There is a subreddit with no subscribers"
print "total nodes with less than 1000 subscribers % d " % nodecount

count = 0
reddit500 = []
for node in nodes2:
        reddit500.append(node)
        count = count + 1
print count

for node in reddit500:
    if node.parent is None:
        reddit.add_child(node)
    
# dump the data into a json file to create viz#    
json_output = open('REDDITS4.json', 'wb')
a = "var viz_data = " + json.dumps(reddit.return_json()) + ";"
json_output.write(a)
json_output.close()