from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from .models import Task

class SimpleTest(APITestCase):
    def setUp(self):

        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        self.regular_user = User.objects.create_user(username='user', password='user123')
        
        admin_group = Group.objects.create(name='Admin')
        user_group = Group.objects.create(name='User')
        
        self.admin_user.groups.add(admin_group)
        self.regular_user.groups.add(user_group)
        
        self.admin_task = Task.objects.create(
            title='Admin Task',
            owner=self.admin_user
        )
        self.user_task = Task.objects.create(
            title='User Task', 
            owner=self.regular_user
        )
    
    def test_admin_sees_all_tasks(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(len(response.data), 2)
    
    def test_user_sees_only_own_tasks(self):
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get('/api/tasks/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'User Task')