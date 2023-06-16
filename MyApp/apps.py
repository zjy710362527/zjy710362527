from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MyApp'


class TasksConfig(AppConfig):
    name = 'tasks'
    verbose_name = '任务管理'
