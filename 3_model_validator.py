from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]  

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in mode.contact_details:
          raise ValueError('Pateint older than 60 must have an emergency contatct ')
        return model


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.married)
    print(patient.age)
    print(patient.email)
    print('updated')


patient_info = {
    'name': 'tingu',
    'age': '60',
    'email': 'junglesh@hdfc.com',  #  Will fail validation if no hdfc or icici
    'linkedin_url': 'https://linkedin.com/in/',
    'weight': 56.9,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'email': 'abc@gmail.com', 'phone': '64792837392' , 'emergency':'269838'}
}

# This will raise ValidationError because domain is not hdfc.com or icici.com
patient1 = Patient(**patient_info) # checking type coersion

update_patient_data(patient1)
