from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict
# it is   a  kind of derived field which user can't privide it you have to derive it like BMI you can calcultae this using height and weight

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float #kg
    height: float #meter
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 

    @computed_field
    @property #both are  decorator
    def calcultae_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.married)
    print(patient.age)
    print(patient.email)
    print('BMI', patient.calcultae_bmi)
    print('updated')


patient_info = {
    'name': 'tingu',
    'age': '30',
    'email': 'junglesh@hdfc.com',  #  Will fail validation if no hdfc or icici
    'linkedin_url': 'https://linkedin.com/in/',
    'weight': 56.9,
    'height': 1.82,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'email': 'abc@gmail.com', 'phone': '64792837392'}
}

# This will raise ValidationError because domain is not hdfc.com or icici.com
patient1 = Patient(**patient_info) # checking type coersion

update_patient_data(patient1)
