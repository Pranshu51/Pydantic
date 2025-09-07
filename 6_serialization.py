from pydantic import BaseModel

class Address(BaseModel):
  city : str
  state : str
  pin : str

class Patient(BaseModel):
  name:str
  gender:str ='Male'
  age:int
  address: Address

address_dict = {'city' : 'gurgaon', 'state': 'haryan' , 'pin': '123221'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 34 ,'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) #patient_dic me agr gender nahi diya to wo export bhinhi hoga exclude_unsert = True ki wajah se
print(temp)
print(type(temp))


# temp = patient1.model_dump() #convert pydantic model to a python dictionary

# print(temp)
# print(type(temp))

# temp = patient1.model_dump_json() #same as above but python consider it as string above it is dictinoary

# print(temp)
# print(type(temp))

# temp = patient1.model_dump(include=['name','gender']) #i only want to export particular field then include fucntion is  there
# print(temp)
# print(type(temp))


# temp = patient1.model_dump(exclude=['name','gender']) #i only want to export particular field excluding these params
# print(temp)
# print(type(temp))


# temp = patient1.model_dump(exclude={'address': ['state']}) #want to export state we should use dictionary
# print(temp)
# print(type(temp))


