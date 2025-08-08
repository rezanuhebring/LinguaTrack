from rest_framework import serializers
from .models import User, Client, Order, Task, Notification, Invoice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'hourly_rate_usd', 'hourly_rate_idr')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'user', 'name', 'email')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'title', 'received_date', 'due_date', 'description', 'original_file', 'final_file', 'status')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'order', 'assigned_to', 'task_type', 'assigned_date', 'start_time', 'end_time', 'draft_file', 'edited_file', 'status', 'duration_in_hours')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'message', 'url', 'created_at', 'is_read')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'order', 'amount_usd', 'amount_idr', 'pdf_file', 'issued_date')
