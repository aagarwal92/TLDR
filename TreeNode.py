#@property = getter and setter#
'''
- what are the children
- find the children
- if it doesnt have a parent, youll add it as a parent
- if child has 2 parents, the one with > subscribers is the parent
-
'''
import copy

class TreeNode:
    def __init__(self, property_dict):
        self.name = property_dict["catname"]
        self.subscribers = property_dict["subnum"]
        self.suggested_children = property_dict["subreddits"]
        self.parent = None
        self.children = []         
    
    def __str__(self):
        if self.parent is not None:
            parent = self.parent.name
        else:
            parent = self.parent
            parent = "None"
        true_children = ""
        for child in self.children:
            true_children += "%s : " % child.name
        return "Current Node: %s \n Parent Node: %s \n Subscriber Count: %d \n Array of Suggested_ Children: %s \n True Children: %s " % (self.name, parent, self.subscribers, self.suggested_children, true_children)
    
#large for loop to traverse array and ask what sugg children are and then add child#
    def remove_child (self, child_node):
        self.children.remove(child_node)
        child_node.parent = None
        
    def add_child(self, child_node):
        if self==child_node:
            raise Exception(self.name)
        self.children.append(child_node)
        child_node.parent = self               
        
    def dep_resolve(self, parent):
        #print self.name
        been_visited.append(self)
        for child in self.suggested_children:
            if child not in resolved_list:
                if child in been_visited:
                    child.subs(self)
                child.dep_resolve(resolved_list, been_visited) 
        resolved_list.append(self)
        for node in resolved_list:
            self.children.append(node)
        
        #been_visited.remove(self)
        #for node in resolved_list:
            #print node
       
    def subs (self):
        nodes = {}
        node = self.parent
            
        while self.subscribers not in nodes:
            #print "goes into sub"
            #print self.name
            #print "--------------------"
           # try:
                nodes[node.subscribers] = node
               # print "goes into the try"
            #except AttributeError:
              #  print "passed?"
                node = node.parent
        #print "exits the while  "
        temp = []
        returned_array = sorted(nodes)
        link = nodes[returned_array[0]]
        for child in link.children:
            for k,node in nodes.items():
                if child == node:
                    link.remove_child(node)
        
        #print link
        '''
        for e in returned_array:
            temp.append(e)
        for item in temp:
            for e in returned_array:
                if item == e:        
                     print "items %d are %d equal" % (item, e)
                     
                      #get the key from the value and base it off of the   
        '''                
                #for k,v in dict_names.items():
    #v.testing_1(dict_names)

    def find_link (self, dict_names, parent_list):
        if self in parent_list:
            #print "if self is in parent_list %s" % self
            #if self.subscribers is not None:
            self.subs()
            #self.testing_1(dict_names)
            
        if self.parent is not None:
            #print "if self parent is not none"
            #if len(parent_list) == 0:
                #print self.parent.name
            parent_list.append(self.parent)
            #        parent_list.append(self.parent)
        for child in self.children:
            #print child
            child.find_link(dict_names, copy.copy(parent_list))
            
            #dict_names[child_name].find_link(dict_names, copy.copy(parent_list))
        

    def testing_1(self, dict_names):
        print self
    
    def sortDict (dict_names):
        items = []
        items = dict_names
        
            
    def return_json(self):
        json_children = []
        #print self.name
        for child in self.children:
            json_children.append(child.return_json())
        if len(self.children) == 0:
            return {
                "name" : self.name,
                "size" : self.subscribers    
            }
        else:
            return {
                    "name" : self.name,
                    "size" : self.subscribers,
                    "children" : json_children
            }
            
            # write to file#
                
    '''        
        if len(self.children) >= 0:
            for child in self.suggested_children:
                if node.parent == node.child.:
                    #subs (self,parent_node)
                    if node.parent.subscribers > node.child.children[0].subscribers:
                        print children[0] + "was removed"
                        node.child.remove_child(children[0])
                    if node.parent.subscirbers > node.subscribers:
                        print child + "was removed"
                        node.parent.remove_child(child)    

            for item in parent_list:
                if item.name != self.parent.name:
                    print "item in parent list name: " + item.name
                    print "self.parent: " + self.parent.name
                    #print "item being added to parent_list   " + item.name


    '''            
            