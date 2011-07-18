import pickle
import os
import json
from TreeNode import TreeNode
  
input = open('popularRedditData.pkl', 'rb') # "rb" for read binary #
file_data = pickle.load(input) # this will give you the array of subreddit dictionaries back #
input.close()
'''

b = TreeNode({
    "catname" : "b",
    "subnum" : 10,
    "subreddits" : ["c"]
})

d = TreeNode({
    "catname" : "d",
    "subnum" : 15,
    "subreddits" : ["e"]
})

e = TreeNode({
    "catname" : "e",
    "subnum" : 1,
    "subreddits" : ["a"]
})

c = TreeNode({
    "catname" : "c",
    "subnum" : 5, #5
    "subreddits" : ["d"]
})

a = TreeNode({
    "catname" : "a",
    "subnum" : 20,
    "subreddits" : ["b"]
})
'''
#file_data = [a,b,c,d,e]

reddit = TreeNode({
    "catname" : "Reddit",
    "subnum" : 20000000,
    "subreddits" : []
})

nodes = []
dict_names = {}
#parent_list = []


for item in file_data:
   nodes.append(TreeNode(item))

for node in nodes:
    #print node.name#
    dict_names[node.name.lower()] = node

#is oarent> child or the other way around)#
#add child to parents#    
for node in nodes:
   # print "1"#
    for childName in node.suggested_children:
        if childName in dict_names:
            child = dict_names[childName]
            print "Child %s has been appended to the ditionary" % child.name
            if child != node:
                if child.parent is not None and node.subscribers > child.parent.subscribers:
                     child.parent.remove_child(child)
                     node.add_child(child)
                     print "Child %s has been added/removed" % child.name
                if child.parent is None:
                     node.add_child(child)
'''
for node in nodes:
    if node.parent is None:
        reddit.add_child(node)
'''

for node in nodes:
    if node.parent is None:
        top_level = node
        break
    
json_output = open('REDDITS.json', 'wb')
a = "var viz_data = " + json.dumps(top_level.return_json()) + ";"
json_output.write(a)
json_output.close()


    
#for node in nodes:
    #print "NODE NAME IS %s" % node.name
    #node.find_link(dict_names, [])
    
#
#for k,v in dict_names.items():
   # v.testing_1(dict_names)




print "DONE WITH FINDING CHILDREN NODES"
#for item in parent_list:
 #   print item.name
print
print

'''
#dependcy resolve#
resolved_list = []
been_visited = []
for node in nodes:
    node.dep_resolve( resolved_list, been_visited)
   '''     
#for node in resolved_list:
   #print node

#subscribers?#

'''
for node in been_visited:
    print "---------------------------"
    print node.name
    if node.parent is not None:
        print node.parent.name
    for child in node.children:
        if node == child.parent and node.parent == child.parent:
            print "yes"
            if node.subscribers > node.parent.subscribers:
                print child
                node.parent.remove_child(child)
            if node.parent.subscirbers > node.subscribers:
                print child
                node.remove_child(child)
# ^ doesnt do anything
'''
'''            
#random#            
    if node.parent.name == node.name || node.parent.name == node.child
     if node.parent.subscribers >= node



#how to print the resolved list to see how far we've gotten, after rasiing exceptions?
#now that a circular refrence has been detected, what should we do? Base decision off of subscribers?

    for node in nodes:    
    while child.parent is not None: #same thing as node?
        if child.parent.subscribers > node.subscribers:
            node = child.parent
'''
#dependency resoltuinn
#resolve improts
#2 classes improt each other, to figure out which imports firs  or second.

'''
# add parents to reddit#
for node in nodes:
    if node.parent is None:
        reddit.add_child(node)

'''
'''

json_output = open('REDDITS.json', 'wb')
a = "var viz_data = " + json.dumps(reddit.return_json()) + ";"
json_output.write(a)
json_output.close()

'''
# create top level dict = reddit. add children as top level things (no parents such as politics)
#loop through nodes, find parents, add them to "reddit"
#nd then dump it into the json output

