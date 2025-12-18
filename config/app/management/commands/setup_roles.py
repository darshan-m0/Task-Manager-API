from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Create Admin and User groups and setup permissions'
    
    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        user_group, created = Group.objects.get_or_create(name='User')
        
        superusers = User.objects.filter(is_superuser=True)
        for superuser in superusers:
            if not superuser.groups.filter(name='Admin').exists():
                superuser.groups.add(admin_group)
                self.stdout.write(
                    self.style.SUCCESS(f'Added superuser {superuser.username} to Admin group')
                )
        
        self.stdout.write(self.style.SUCCESS('Admin and User groups created'))
        self.stdout.write(self.style.SUCCESS('All superusers added to Admin group'))