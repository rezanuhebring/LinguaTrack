from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('translator', 'Translator'),
        ('editor', 'Editor'),
        ('manager', 'Manager'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    hourly_rate_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourly_rate_idr = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('received', 'Received'),
        ('drafting', 'Drafting'),
        ('editing', 'Editing'),
        ('finalizing', 'Finalizing'),
        ('completed', 'Completed'),
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    received_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    description = models.TextField()
    original_file = models.FileField(upload_to='orders/original/')
    final_file = models.FileField(upload_to='orders/final/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')

    def __str__(self):
        return self.title

class Task(models.Model):
    TYPE_CHOICES = (
        ('drafting', 'Drafting'),
        ('editing', 'Editing'),
        ('finalizing', 'Finalizing'),
    )
    STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    assigned_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    draft_file = models.FileField(upload_to='tasks/draft/', null=True, blank=True)
    edited_file = models.FileField(upload_to='tasks/edited/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')

    def __str__(self):
        return f'{self.get_task_type_display()} for {self.order.title}'

    @property
    def duration_in_hours(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 3600
        return 0

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class Invoice(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount_usd = models.DecimalField(max_digits=10, decimal_places=2)
    amount_idr = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to='invoices/')
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Invoice for {self.order.title}'