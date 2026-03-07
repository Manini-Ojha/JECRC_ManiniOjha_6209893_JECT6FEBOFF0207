import time
#int(time.time()) #to find milisecs that will be written in id

class TODO:
    todos = [] #every todo will have individual dictionaries: {'id':'','desc':'','is_completed':False}
    
    def add_todo(self, desc):
        #1. take the desc from the user
        #2. create a dictionary in which we will add to do desc
        #3. append dictionary in todos[]
        
        dict={'id':int(time.time()),
              'desc':desc,
              'is_completed':False}
        self.todos.append(dict)
    
    def remove_todo(self, id):
        if len(self.todos)==0:return
        for i in self.todos:
            if i['id']==id:
                self.todos.remove(i)
    
    def display_todos(self):
        if len(self.todos)==0:return

        for i in self.todos:
            if i['is_completed']:
                print(f'--->{i["desc"]}, {i["id"]},(completed)')
            else:
                print(f'--->{i["desc"]},{i["id"]},(incompleted)')
        # print(self.todos)
    
    def update_todo(self, id, new_desc):

        if len(self.todos)==0:return
        for i in self.todos:
            if i['id']==id:
                i['desc']=new_desc
    
    def toggle_mark_as_completed(self, id):
        if len(self.todos)==0:return
        for i in self.todos:
            if i['id']==id:
                i['is_completed']=True
    
    def completed_todos(self):
        # comp=[]
        if len(self.todos)==0:return
        for i in self.todos:
            if i['is_completed']==True:
                print(f'-->{i['desc']}')
            #    comp.append(i)
        # return comp 
    
    def incompleted_todos(self):
        # incomp=[]
        if len(self.todos)==0:return
        for i in self.todos:
            if i['is_completed']==False:
                print(f'--->{i['desc']}')
                # incomp.append(i)
        # return incomp
    
obj=TODO()
# obj.add_todo('washing clothes')
# print(obj.todos)