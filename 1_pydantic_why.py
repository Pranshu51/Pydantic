##1.Problem-TYPE VALIDATION
# There isno type validation in python so  pydantic solve this problem here below there are two problems and here repetetion is happening and also if someone wants to add something it should be updated in all the function one by one manually which is not good
#2.PROBLEM 2- (DATA VALIDATION)CONDITIONS CANT BE APPLLIED I.E INTERVALIDATION
####THAT'S HOW PYDANTIC INTRODUCED

def insert_patient_data(name:str ,age: int):

  if type(name)== str and type(age)==int:
    if age < 0:
      raise ValueError('Age cant be negative')
    else:
      print(name)
      print(age)
      print("Inserted into database")    
  else:
    raise TypeError('Incorrect data type')

insert_patient_data('nitish',30)   

# this logic is correct but it is not scalable

def update_patient_data(name:str ,age: int):

  if type(name)== str and type(age)==int:
    print(name)
    print(age)
    print("Updated")
  else:
    raise TypeError('Incorrect data type')

insert_patient_data('nitish',30)   