from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, email, password):
        '''
            Function for creating a user
        '''

        if not email: ## NOTE This means if a user leaves it empty
            raise ValueError('Users must have an email')
        if not first_name: ## NOTE This means if a user leaves it empty
            raise ValueError('Users must have a first name')
        if not last_name: ## NOTE This means if a user leaves it empty
            raise ValueError('Users must have a last name')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email=email),
        )

        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, first_name, last_name, email, password):
        '''
            Create a super user
        '''

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''
        Creating a custom user model
    '''

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['first_name', 'last_name']
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return self.email

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()


class Profile(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='Profile/', blank=True, null=True) ## NOTE create folders for each user