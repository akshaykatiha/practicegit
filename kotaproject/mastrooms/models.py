from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('Please Enter a Valid Phone Number')

        user = self.model(
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(validators=[RegexValidator(regex=r'^[9876]\d{9}$', message="Number must be of 10 digits, starting with either 6,7,8 or 9 with no prefix(+91 or 0)", code='nomatch')],max_length=10,unique=True)
    name = models.CharField(max_length=124,blank=True,default='Mastrooms User')
    email = models.EmailField(blank=True, null=True)
    is_owner = models.BooleanField('Owner',default=True)
    is_tenant = models.BooleanField('Tenant',default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'user'


class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    number_of_rooms = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
       return self.user.name

    class Meta:
        db_table = 'owner'


class Room(models.Model):
    name = models.CharField(max_length = 255, blank= True)
    #slug = models.SlugField(max_length=124)
    ADDRESS_CHOICE = (
        ('Army Area','Army Area'),
        ('AnantPura','AnantPura'),
        ('Bajrang Nagar','Bajrang Nagar'),
        ('Ballabh Nagar','Ballabh Nagar'),
        ('Borkhera','Borkhera'),
        ('Bhimganj Mandi','Bhimganj Mandi'),
        ('Chawani','Chawani') ,
        ('Dadawadi','Dadawadi'),
        ('Dhanmandi','Dhanmandi'),
        ('Ganesh Nagar','Ganesh Nagar'),
        ('Girdharpura','Girdharpura'),
        ('Gordhanpura','Gordhanpura'),
        ('Gumanpura','Gumanpura'),
        ('Indra Vihar','Indra Vihar'),
        ('JK Colony','JK Colony'),
        ('Keshav Pura','Keshav Pura'),
        ('Kunhari','Kunhari'),
        ('Mahavir Nagar Ist','Mahavir Nagar Ist'),
        ('Mahavir Nagar IInd','Mahavir Nagar IInd'),
        ('Mahavir Nagar IIIrd','Mahavir Nagar IIIrd'),
        ('Mokhapura','Mokhapura'),
        ('NayaPura','NayaPura'),
        ('Narcotics Colony','Narcotics Colony'),
        ('Rajeev Gandhi Nagar','Rajeev Gandhi Nagar'),
        ('Old Rajeev Gandhi Nagar','Old Rajeev Gandhi Nagar'),
        ('Parijat Colony','Parijat Colony'),
        ('Poonam Colony','Poonam Colony'),
        ('Prem Nagar','Prem Nagar'),
        ('Ramganj Mandi','Ramganj Mandi'),
        ('Rampura','Rampura'),
        ('Rangbari','Rangbari'),
        ('R.K Puram','R.K Puram'),
        ('Sanjay Nagar','Sanjay Nagar'),
        ('Shivpura','Shivpura'),
        ('Shubhash Nagar','Shubhash Nagar'),
        ('Srinath Puram','Srinath Puram'),
        ('Swami Vivekanand Nagar','Swami Vivekanand Nagar'),
        ('Talwandi','Talwandi'),
        ('Transport Nagar','Transport Nagar'),
        ('Vigyan Nagar','Vigyan Nagar'),
        ('Other','Other'),
        
    )

    house_number = models.CharField(max_length=24, blank=True)
    address = models.CharField(max_length=50, choices=ADDRESS_CHOICE)

    CATEGORY_CHOICE = (
        ("Boys' Hostel","Boys' Hostel"),
        ("Boys' PG","Boys' PG"),
        ("Girls' Hostel","Girl's Hostel"),
        ("Girls' PG","Girl's PG"),
        ("Family Room","Family Room"),
        ("Flats","Flats"),
    )

    OCCUPANCY = (
        ('Single','Single Seater'),
        ('Double','Double Seater'),
        ('Dormitory','Dormitory'),
    )
    
    category = models.CharField(max_length=13, choices=CATEGORY_CHOICE)
    occupancy = models.CharField(max_length=9, choices=OCCUPANCY, default='Single')
    landmark = models.CharField(max_length=124, blank="True",)
    rent = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to='static/media',blank=True,null=True)
    image2 = models.ImageField(upload_to='static/media',blank=True,null=True)
    image3 = models.ImageField(upload_to='static/media',blank=True,null=True)
    image4 = models.ImageField(upload_to='static/media',blank=True,null=True)
    bed = models.BooleanField(default=True)
    table= models.BooleanField(default=True)
    fan = models.BooleanField(default=True)
    ro_water = models.BooleanField(default=False)
    mess = models.BooleanField(default=False)
    cctv= models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    power_backup = models.BooleanField(default=False)
    attached_bathroom = models.BooleanField(default=False)
    geyser = models.BooleanField(default=False)    
    other_amenities = models.TextField(blank=True)
    description = models.TextField(blank=True)#Placeholder
    other_contact_number = models.TextField(blank=True)
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^[9876]\d{9}$' , code='nomatch')],max_length=10)
    is_active = models.BooleanField('Available',default=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    room_key = models.CharField(max_length=10,editable='False',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'room'


class Tenant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICE = (
        ('Male','Male'),
        ('Female','Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, null=True, blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    COACHING_CHOICE=(
        ('Aakash','Aakash Institute'),
        ('Allen', 'ALLEN Career Institute'),
        ('Bansal','Bansal Classes'),
        ('Career Point','Career Point'),
        ('Motion','Motion Education'),
        ('Nucleus','Nucleus Education'),
        ('Rao','RaoIIT'),
        ('Reso','Resonance'),
        ('Sarvottam','Sarvottam'),
        ('Vibrant','Vibrant'),
        ('Other','Other'),
    )
    coaching = models.CharField(max_length = 50, choices=COACHING_CHOICE, default='Kota Coaching')
    home_address = models.CharField(max_length = 255, blank= True)
    room_key = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    class Meta:
        db_table = 'tenant'
