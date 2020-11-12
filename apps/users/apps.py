from django.apps import AppConfig

# 在每一个app的apps.py中修改：
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户信息'
