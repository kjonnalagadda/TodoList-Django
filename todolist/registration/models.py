from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.hashers import make_password

# Define validators separately
password_length_validator = MinLengthValidator(8, message='Password must be at least 8 characters long')
password_complexity_validator = RegexValidator(
    regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
    message='Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character'
)

class UserRegister(models.Model):
    Username = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=254, unique=True)
    Password = models.CharField(max_length=255, validators=[password_length_validator, password_complexity_validator])
    Confirm_Password = models.CharField(max_length=255, validators=[password_length_validator, password_complexity_validator])
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        db_table = 'UserRegistration'


class UserTodoList(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    Task = models.CharField(max_length=250)
    Description = models.CharField(max_length=300, blank=True, null=True)
    DueDate = models.DateTimeField()
    Status = models.CharField(max_length=100)
    Created_On = models.DateTimeField(auto_now_add=True)
    Updated_On = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        db_table = 'UserTodoLists'
        



# from django.db import models
# from django.contrib.auth.hashers import make_password
# from django.core.validators import MinLengthValidator, RegexValidator
# from django.core.exceptions import ValidationError

# # Define validators separately
# password_length_validator = MinLengthValidator(8, message='Password must be at least 8 characters long')
# password_complexity_validator = RegexValidator(
#     regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
#     message='Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character'
# )

# # Create your models here.
# class UserRegister(models.Model):
#     Username = models.CharField(max_length=100)
#     Firstname = models.CharField(max_length=100)
#     Lastname = models.CharField(max_length=100)
#     Age = models.IntegerField()
#     Email = models.EmailField(max_length=254, unique=True)
#     Password = models.CharField(max_length=255, validators=[password_length_validator, password_complexity_validator])
#     Confirm_Password = None  # Transient field for confirmation password
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.confirm_password = None  # Initialize confirm_password field
    
#     def save(self, *args, **kwargs):
#         # Exclude confirm_password field when saving to the database
#         if self.confirm_password is not None:
#             delattr(self, 'confirm_password')
#         super().save(*args, **kwargs)
        
#     def clean(self):
#         # Check if password and confirm_password match
#         if self.Password != self.confirm_password:
#             raise ValidationError("The passwords do not match.")

#     class Meta:
#         db_table = 'UserRegistration'