class project_2():
    def log_review (self):
        stop=""
        i = 0
        self.master_list=[] 
        expense = 0.0
        category = " 0"
        permission=input("do you wish to log?(y/n):")
        if permission == 'n':
             stop = True
             return
        else:
             stop = False
        
        while stop==False :
            new_expense=float(input("enter the expense: "))
            expense = new_expense
        
            new_category = input("enter category: ")
            category=new_category
            i=i+1 
            self.master_list.append({'index':i, 'category':category,'expense':expense})
                         
            end=input('would you like to stop?(T/F): ')
            if end == 'T':
                break
            i=i+1 
        
    def calculator(self):
                formatted_list =[]
                checked_indices=[]
                for element in  self.master_list:
                    if element['index'] not in checked_indices: 
                        final_expense = element['expense']
                        number_ofLogs=1
                        for word in self.master_list :
                           if element['category'] == word['category'] and element['index'] != word['index']:
                              final_expense = final_expense + word['expense']
                              number_ofLogs = number_ofLogs+1 
                              checked_indices.append(word['index'])
                   
                        formatted_list.append({'category':element['category'],'total_expense':final_expense,'Logs':number_ofLogs})

                for word in formatted_list:
                    print(word)

# 1. Create a living instance of your class
my_tracker = project_2()

# 2. Trigger the logger (passing in dummy variables to satisfy your requirements)
my_tracker.log_review()

# 3. Trigger the calculator to see your results!
my_tracker.calculator()
                   
               
    



