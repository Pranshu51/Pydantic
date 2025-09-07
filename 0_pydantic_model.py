from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict ,Optional,Annotated

#You can add Metadata by combining Annotated+ Field 

class Patient(BaseModel):
  name: Annotated[str, Field(max_length= 50, title="Name of the patient" , description='Give the name of the patient in less than 50 chars', example= ['Nitesh', 'chirag'] )]#Field(max_length=50)
  age:int = False# if somone not give shows false it can also be defualt
  email: EmailStr #validate email
  linkedin_url: AnyUrl #Validate Url 
  weight: Annotated[float , Field(gt=0, lt=120 , strict = True)]
  married: Annotated[bool, Field(default= None , description = ' whether the pateient is married or not')]
  # Optional[bool] = None#to make optional one should provide a default value if person will not tell whetehr married or not then it would show none
  allergies: List[str] #for two level validaiton like we want List and inside it there should be String
  contact_details: Dict[str, str] #here Dict should be ther re and inside there  key and value also should be string

def insert_patient_data(patient : Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient : Patient):

  print(patient.name)
  print(patient.married)
  print(patient.age)
  print('updated')  

patient_info = {
    'name': 'nitish',
    'age': 30,
    'email': 'junglesh@gmail.com',
    'linkedin_url': 'https://linkedin.com/in/',
    'weight': 56.9,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'email': 'abc@gmail.com', 'phone': '64792837392'}
}
# will give NOne as Marred not mentioned

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)

