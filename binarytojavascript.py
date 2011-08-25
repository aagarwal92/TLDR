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
dict_names = {}

for item in file_data:
   nodes.append(TreeNode(item))

for node in nodes:
    dict_names[node.name.lower()] = node

#add child to parents#    
for node in nodes:
   # print "1"#
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

   
txt = 0
nodecount = 0


for node in nodes:
    txt = txt+1
print "total nodes before removing useless subreddits %d " % txt


#dumps the nodes with >1000 subscribers into a separate json file#
'''
txt2=0
for node in nodes:
    if node.subscribers >= 1000:
        #print node.name
        #nodes.remove(node)
        useful_nodes.append(node)
        txt2 = txt2+1
print "nodes after removing useless one %d" % txt2
for node in useful_nodes:
    nodecount = nodecount + 1
print "node count %d " % nodecount

output2 = open('UsefulReddits.pkl', 'wb')
pickle.dump(useful_nodes, output2)
output2.close()
'''

#opens the useful reddits and appends them to a dictionary#
input2 = open('UsefulReddits.pkl', 'rb') # "rb" for read binary #
file_data2 = pickle.load(input2) # this will give you the array of subreddit dictionaries back #
input2.close()

nodes2 = []
dict_names2 = []


fileCount = 0
for item in file_data2:
    fileCount = fileCount + 1    
    nodes2.append(item)

print "number of reddits in the new dictionary %d " % fileCount


nodecount = 0
for node in nodes2:
    if node.subscribers < 1000:
        #nodes2.remove(node)
        nodecount = nodecount+1
    if node.subscribers is None:
        print "wow"
print "blah % d " % nodecount

#for node in nodes2:
    #print node.name#
    #dict_names2[node.name.lower()] = node

count = 0
for node in nodes2:
    if count < 900:
        reddit500.append(node)
        count = count + 1
print count

for node in reddit500:
    if node.parent is None:
        reddit.add_child(node)
        
json_output = open('REDDITS.json', 'wb')
a = "var viz_data = " + json.dumps(reddit.return_json()) + ";"
json_output.write(a)
json_output.close()

print "DONE WITH FINDING CHILDREN NODES"   