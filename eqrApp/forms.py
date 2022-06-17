from django import forms
from eqrApp import models

class SaveEmployee(forms.ModelForm):
    # employee_code = forms.CharField(max_length=250, label="Company ID")
    first_name = forms.CharField(max_length=250, label="First Name")
    last_name = forms.CharField(max_length=250, label="Last Name")
    dob = forms.DateField(label="Birthday")
    gender = forms.ChoiceField(choices=[("Male","Male"), ("Female","Female")], label="Gender")
    contact = forms.CharField(max_length=250, label="Contact #")
    email = forms.CharField(max_length=250, label="Email")
    address = forms.Textarea()
    department = forms.CharField(max_length=250, label="Department")
    position = forms.CharField(max_length=250, label="Position")
    avatar = forms.ImageField(label="Avatar")

    class Meta():
        model = models.Employee
        fields = (#'employee_code',
                  'first_name',
                  'last_name',
                  'dob',
                  'gender',
                  'contact',
                  'email',
                  'address',
                  'department',
                  'position',
                  'avatar', )

    # def clean_employee_code(self):
    #     id = self.data['id'] if self.data['id'] != '' else 0
    #     employee_code = self.cleaned_data['employee_code']
    #     try:
    #         if id > 0:
    #             employee = models.Employee.exclude(id=id).get(employee_code = employee_code)
    #         else:
    #             employee = models.Employee.get(employee_code = employee_code)
    #     except:
    #         return employee_code
    #     return forms.ValidationError(f"{employee_code} already exists.")




class IDForm(forms.Form):
    id = forms.CharField(max_length=8, required=True)