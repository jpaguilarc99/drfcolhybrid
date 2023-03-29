from django.contrib.auth.models import User

superuser = User.objects.create_user(username='jpaguilarc', email='jpaguilarc99@gmail.com', is_superuser=True)
superuser.set_password('984597mce')
superuser.save()