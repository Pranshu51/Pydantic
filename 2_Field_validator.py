from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
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

    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not in Valid Domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')#give error mode="before" because it takes input as string of age '30' before value in   AFTER it  takes value after type coersion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            return ValueError('Age hould be in between 0 and 100')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.married)
    print(patient.age)
    print(patient.email)
    print('updated')


patient_info = {
    'name': 'tingu',
    'age': '30',
    'email': 'junglesh@hdfc.com',  #  Will fail validation if no hdfc or icici
    'linkedin_url': 'https://linkedin.com/in/',
    'weight': 56.9,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'email': 'abc@gmail.com', 'phone': '64792837392'}
}

# This will raise ValidationError because domain is not hdfc.com or icici.com
patient1 = Patient(**patient_info) # checking type coersion

update_patient_data(patient1)
