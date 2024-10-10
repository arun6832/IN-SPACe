from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)  # Ensure this is a float and has a default value
    group = models.ForeignKey(Group, related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Split(models.Model):
    group = models.ForeignKey(Group, related_name='splits', on_delete=models.CASCADE)
    total_amount = models.FloatField()

    def __str__(self):
        return f'Split for {self.group.name}'
