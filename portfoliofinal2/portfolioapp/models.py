from django.db import models
from django.db import models
import datetime
# from PILlow import Image
import io
from django.core.mail import send_mail
from django import forms
class about(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    birthdate = models.DateField()
    linkedin = models.URLField()
    phone_number = models.CharField(max_length=20)
    city = models.TextField()
    Degree = models.TextField()
    email = models.EmailField(unique=True)
    summary = models.TextField(null='True')
    image = models.ImageField(upload_to='projects/')


    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
    def __str__(self):
        return self.title
class fact(models.Model):
    title=models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    clients_no=models.CharField(max_length=50)
    project_no=models.CharField(max_length=50)
    support_hour=models.CharField(max_length=50)
    staff_no=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class skills (models.Model):
    title=models.CharField(max_length=30)
    summary = models.CharField(max_length=100)
    skill=models.CharField(max_length=30)
    rating = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Resumes(models.Model):
    # Fields for storing personal information
    full_name = models.CharField(max_length=30)
    summary=models.TextField(null='True')
    individual_summary = models.TextField(null='True')
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    # Fields for storing skills and education information
    experience_in= models.TextField()
    education = models.TextField()
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    college_name = models.CharField(max_length=255)
    collge_summary=models.TextField()

    # Fields for storing work history


    def __str__(self):
        return f"{self.full_name}"

class workhistory(models.Model):
    Role=models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField()
    end_year = models.CharField(max_length=50)
    responsibilities=models.TextField(max_length=200,blank='True')
    def __str__(self):
        return self.Role
class webresponsibilities(models.Model):
    title='webseveloper'
    responsibility1 = models.TextField(max_length=200, blank='True')
    responsibility2 = models.TextField(max_length=200, blank='True')
    responsibility3 = models.TextField(max_length=200, blank='True')
    def __str__(self):
        return self.title

class designer_responsibilities(models.Model):
    title='Designer'
    responsibility1 = models.TextField(max_length=200, blank='True')
    responsibility2 = models.TextField(max_length=200, blank='True')
    responsibility3 = models.TextField(max_length=200, blank='True')
    def __str__(self):
        return self.title


class portfolio(models.Model):
    title='portfolio'
    summary=models.CharField(max_length=200)
    image=models.ImageField(upload_to='projects/')
    link=models.URLField(null=True)

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        image = Image.open(self.image)

        # resize the image to the desired dimensions
        image = image.resize(( 400, 400))

        # Save the cropped image to a buffer
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)

        # Save the buffer to the ImageField
        self.image.save(self.image.name, buffer, save=False)

        # Save the rest of the model
        super().save(*args, **kwargs)
    def __str__ (self):
     return self.title;

class services (models.Model):
    title='Our service'
    summary=models.CharField(max_length=200)
    service_name=models.CharField(max_length=100)
    icon_name=models.CharField(max_length=20, null=True)
    service_summary = models.CharField(max_length=200)
    def __str__ (self):
     return self.title;


class testimonial(models.Model):
    title='Testimonials'
    summary=models.CharField(max_length=200)
    Full_name = models.CharField(max_length=50,null=True)

    profession=models.CharField(max_length=30)
    Testimony_Photo=models.ImageField(upload_to='projects/',null=True)
    comments=models.CharField(max_length=200)
    def __str__ (self):
     return self.title;

class contact(models.Model):
    name = models.CharField(max_length=255,null=True)
    summary=models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    map_url = models.URLField(null=True)

    def __str__(self):
        return self.name

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)


