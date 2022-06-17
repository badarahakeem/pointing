from distutils.command.upload import upload
from email.policy import default
import secrets, string
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
import qrcode
from PIL import Image, ImageDraw

from io import BytesIO
from django.core.files import File

# Create your models here.
class Employee(models.Model):
    employee_code = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=(("Male","Male"), ("Female","Female")), default="Male")
    dob = models.DateField(max)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=250, blank=True)
    address = models.TextField(null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    position = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to = "employee-avatars/",null=True, blank=True)
    qr_code = models.ImageField(upload_to = 'qr_code', blank=True, null=True)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(f"{self.employee_code} - {self.first_name} "+ f"{self.last_name}")
    def name(self):
        return str(f"{self.first_name} "+ f"{self.last_name}")


    def save(self, *args, **kwargs):
        
        # if not self.employee_code or len(self.employee_code) is None:
        #     alphabet = string.digits
        #     password = ''.join(secrets.choice(alphabet) for i in range(8))
        #     self.employee_code  = password

        qr_image = qrcode.make(self.employee_code)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        draw_img = ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        file_name = f'{self.employee_code}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_field.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
        # imag = Image.open(self.avatar.path)
        # if imag.width > 200 or imag.height > 200:
        #     output_size = (200, 200)
        #     imag.thumbnail(output_size)
        #     imag.save(self.avatar.path)
        


    

class Pointing(models.Model):
    STATUS = (
        ("absent","absent"),
        ("retard","retard"),
        ("regle","en regle"),
    )
    employee = models.ForeignKey("Employee", verbose_name=("Employé"), on_delete=models.CASCADE)
    clock_time = models.DateTimeField(("pointage debut"))
    clock_out = models.DateTimeField(("pointage fin"), blank=True, null=True)
    status = models.CharField(("Status"), max_length=50, choices=STATUS, blank=True)
    created = models.DateTimeField(("Fait le"), auto_now_add=True)
    updated = models.DateTimeField(("mise a jour le"), auto_now=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return " ".join([self.employee.employee_code,"- heure de debut:", self.clock_time.strftime("%x %X")])


