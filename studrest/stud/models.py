from django.db import models

class Student(models.Model):
    gender_choices=(
        ('m','male'),
        ('f','female'),
    )
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6,choices=gender_choices)
    skill = models.BooleanField()
    country = models.CharField(max_length=10)
    remark = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

