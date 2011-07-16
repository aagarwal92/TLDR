#@property = getter and setter#
'''
- what are the children
- find the children
- if it doesnt have a parent, youll add it as a parent
- if child has 2 parents, the one with > subscribers is the parent
-
'''

class TreeNode:
    def __init__(self, property_dict):
        self.name = property_dict["catname"]
        self.subscribers = property_dict["subnum"]
        self.suggested_children = property_dict["subreddits"]
        self.parent = None
        self.children = []         
        
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
            
        while self.name not in nodes:
            print self.name
            print "--------------------"
            nodes[node.name] = node.subscribers
            node = node.parent
        print nodes




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
    '''

# pare    
    def find_link (self, dict_names, parent_list):
        if self in parent_list:
            print self.name
            self.subs()
            #print self.name #dep-resol
            return
        if self.parent is not None:    
            parent_list.append(self.parent)
        for child_name in self.suggested_children:
            #print child_name    
            dict_names[child_name].find_link(dict_names, parent_list)
        

    def return_json(self):
        json_children = []
        print self.name
        for child in self.children:
            json_children.append(child.return_json())
            
        return {
                "name" : self.name,
                "size" : self.subscribers,
                "children" : json_children
        }
            
            
            # write to file#
                
        
            
            
            
    