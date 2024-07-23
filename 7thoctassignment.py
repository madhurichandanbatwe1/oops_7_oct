# Problem 1: Bank Account Create a class representing a bank account with attributes like account number, account holder name, and balance. Implement methods 
# to deposit and withdraw money from the account.


class bank_account:
    def __init__(self,acc_no,name,bal):
        self.acc_no=acc_no
        self.name=name
        self.bal=bal
        
        
    def deposit(self,amt):
        self.amt=amt
        self.bal=self.bal+self.amt
        return self.bal
    
    def withdraw(self,amt):
        self.amt=amt
        self.bal=self.bal-self.amt
        return self.bal
    
bc=bank_account(101,'madhuri',5000)
print(bc.deposit(100))
print(bc.withdraw(100))



# Problem 2: Employee Management Create a class representing an employee with attributes like employee ID, name, and salary. Implement methods to 
# calculate the yearly bonus and display employee details.

class employee:
    def  __init__(self,emp_id,name,sal) :
        self.emp_id=emp_id
        self.name=name
        self.sal=sal
    
    def yearly_bonus(self,bonus):
        self.bonus=bonus
        return (self.sal*self.bonus)/100
    
    def  emp_details(self):
        print("emp_id",self.emp_id)
        print("name",self.name)
        print("salary",self.sal)

emp=employee(200,'rishi',160000)
print(emp.yearly_bonus(28))
print(emp.emp_details())

# Problem 3: Vehicle Rental Create a class representing a vehicle rental system. Implement methods to rent a vehicle, return a vehicle, 
# and display available vehicles.

class vehicles:
    def __init__(self):
        self.available_vehicles={
            'car':4,
            'bike':2,
            'bicycle':10,
            'jeep':2
        }
        self.rented_vehicles={
            'car':0,
            'bike':0,
            'bicycle':0,
            'jeep':0    
        }
        
    def display_available_vehicles(self):
        for vehicle,count in self.available_vehicles.items():
            print(f'{vehicle}:{count}')
            
    def rent_vehicle(self,vehicle):
        if vehicle in self.available_vehicles and self.available_vehicles[vehicle]>0:
            self.available_vehicles[vehicle]-=1
            self.rented_vehicles[vehicle]+=1
        return self.available_vehicles[vehicle],self.rented_vehicles[vehicle]
    
    def return_vehicle(self,vehicle):
        if vehicle in self.rented_vehicles and self.rented_vehicles[vehicle]>0:
            self.rented_vehicles[vehicle]-=1
            self.available_vehicles[vehicle]+=1
        return self.rented_vehicles[vehicle],self.available_vehicles[vehicle]
    
vehicle= vehicles()
vehicle.display_available_vehicles()

vehicle.rent_vehicle('car')
vehicle.display_available_vehicles()
        
vehicle.rent_vehicle('bicycle')
vehicle.display_available_vehicles()

vehicle.return_vehicle('car')
vehicle.display_available_vehicles() 
           


# Problem 4: Library Catalog Create classes representing a library and a book. Implement methods to add books to the 
# library, borrow books, and display available books.

class library:
    def __init__(self):
        self.books={
           'Wings of fire':5,
           'Rich Dad Poor Dad':7,
           'The Mocking Bird':10,
           '2 states_new':4,
           'do Epic shits':15
        }
        
    def display_available_books(self):
        for book,count in self.books.items():
            print(f'{book}:{count}')
            
    def add_book(self,book,count=1):
        
        if book in self.books and self.books[book]>0:
            self.books[book]+=count
        else:
            self.books[book]=count
        return self.books
    
    def borrow_book(self,book):
        if book in self.books and self.books[book]>0:
            self.books[book]-=1
        return self.books.get(book,0)
    
lib=library()
lib.display_available_books()

lib.add_book('Shyamchi aai')
lib.display_available_books()

lib.borrow_book('Wings of fire')
lib.display_available_books()



#Problem 5: Product Inventory Create classes representing a product and an inventory system. 
# Implement methods to add products to the inventory, update product quantity, and display available products.


class product_inventory_system:
    def __init__(self):
        self.products={
            'books':4,
            'pen':1,
            'stapler':2,
            'cello tape':7
        }
    def display_available_products(self):
        for product,count in self.products.items():
            print(f'{product}:{count}')
            
    def add_products(self,product,count):
        if product in self.products and self.products[product]>0:
            self.products[product]+=count
        else:
            self.products[product]=count
        return self.products

prod=product_inventory_system()
prod.display_available_products()

prod.add_products('medicine',30)
prod.display_available_products()

prod.add_products('files',1000)
prod.display_available_products()

prod.add_products('cello tape',2)
prod.display_available_products()

# Problem 6: Shape Calculation Create a class representing a shape with 
# attributes like length, width, and height. Implement methods to calculate the area and perimeter of the shape.
            
class shape:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
        
    def area(self,side):
        if side==4 and self.length==self.width==self.height:
            return self.length**2
        elif side==3 and self.length!=self.height:
            return 0.5*self.length*self.height
        elif side==4 and self.length!=self.height:
            return self.length*self.height
        
    def perimeter(self,side):
        if side==4 and self.length==self.width==self.height:
            return self.length*4
        elif side==3 and self.length!=self.height!=self.width:
            return self.length+self.width+self.height
        
square=shape(24,24,24)
print(square.area(4))
print(square.perimeter(4))
        
# Problem 7: Student Management Create a class representing a student with attributes like student ID, name, and grades.
# Implement methods to calculate the average grade and display student details.        
            
            
class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name 
        self.grade=[]
    def add_grade(self,grade):
        self.grade.append(grade)
        return self.grade
    def average_grade(self):
        if len(self.grade)>0:
            self.avg=sum(self.grade)/len(self.grade)
        return self.avg
    def display_details(self):
        print(f'Student info is {self.name},{self.id},{self.grade},{self.avg}')
        
nishi=student(10,'nishi')
nishi.add_grade(45)
nishi.add_grade(50)
nishi.add_grade(49)

nishi.average_grade()
nishi.display_details()
   
   
# Problem 8: Email Management Create a class representing an email with attributes like sender, recipient, and subject.
# Implement methods to send an email and display email details.

class email:
    def __init__(self,sender,recipient,subject):
        self.sender=sender
        self.recipient=recipient
        self.subject=subject
        self.sent=False
        
    def sending_email(self):
        self.sent=True
        print(f"Email sent to {self.recipient} from {self.sender}")
    
    def display_email_details(self):
        print(f"Info of enail is {self.sender},{self.recipient},{self.subject}")
        
remembrance=email('Deshpande','Deshmukh','remembrance')
remembrance.sending_email()
remembrance.display_email_details()

# Problem 9: Social Media Profile Create a class representing a social media profile with attributes like username and posts.
# Implement methods to add posts, display posts, and search for posts by keyword.

class media:
    def __init__(self,username):
        self.username=username
        self.posts=[]
    
    def add_posts(self,posts):
        self.posts.append(posts)
        return self.posts
    
    def display_posts(self):
        print(f'{self.username}')
        for posts in self.posts:
            print(posts)
              
    def search(self,keyword):
        for posts in self.posts:
            if f'{keyword}' in posts:
                print(posts)
priyavsmriti=media('priyav09')
priyavsmriti.add_posts('Not all days are bad')
priyavsmriti.add_posts("Keep calm and play hard")
priyavsmriti.add_posts('Word hard play hard')

priyavsmriti.display_posts()
priyavsmriti.search('hard')


# Problem 10: ToDo List Create a class representing a ToDo list with attributes like tasks and due dates. 
# Implement methods to add tasks, mark tasks as completed, and display pending tasks.

class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = {
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task added: {description}, due by {due_date}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            print(f"Task marked as completed: {self.tasks[task_index]['description']}")
        else:
            print("Invalid task index.")

    def display_pending_tasks(self):
        print("Pending Tasks:")
        for index, task in enumerate(self.tasks):
            if not task['completed']:
                print(f"{index + 1}. {task['description']} (Due: {task['due_date']})")

# Example usage
todo_list = ToDo()
todo_list.add_task("Buy groceries", "2024-07-25")
todo_list.add_task("Finish project report", "2024-07-27")
todo_list.add_task("Call Alice", "2024-07-24")

todo_list.display_pending_tasks()

todo_list.mark_task_completed(1)
todo_list.display_pending_tasks()

        
        
            
        



        

        
     
        
        
            
       