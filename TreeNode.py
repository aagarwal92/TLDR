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
    
    def remove_child (self, child_node):
        self.children.remove(child_node)
        child_node.parent = None
        
    def add_child(self, child_node):
        if self==child_node:
            raise Exception(self.name)
        self.children.append(child_node)
        child_node.parent = self               
        
    def dep_resolve(self, parent):
        been_visited.append(self)
        for child in self.suggested_children:
            if child not in resolved_list:
                if child in been_visited:
                    child.subs(self)
                child.dep_resolve(resolved_list, been_visited) 
        resolved_list.append(self)
        for node in resolved_list:
            self.children.append(node)
       
    def subs (self):
        nodes = {}
        node = self.parent
            
        while self.subscribers not in nodes:
                nodes[node.subscribers] = node
                node = node.parent
        temp = []
        returned_array = sorted(nodes)
        link = nodes[returned_array[0]]
        for child in link.children:
            for k,node in nodes.items():
                if child == node:
                    link.remove_child(node)

    def find_link (self, dict_names, parent_list):
        if self in parent_list:
            self.subs()
            
        if self.parent is not None:
            parent_list.append(self.parent)
        for child in self.children:
            child.find_link(dict_names, copy.copy(parent_list))        

    def testing_1(self, dict_names):
        print self
    
    def sortDict (dict_names):
        items = []
        items = dict_names
        
            
    def return_json(self):
        json_children = []
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