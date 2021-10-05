from django.db import models

class Result(models.Model):
    intensity_sum = models.IntegerField(default=0)
    serial_num = models.IntegerField(default=0)
    belong = models.IntegerField(default=0)

    def __str__(self):
        return str(self.intensity_sum)


class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}. {self.content}'


class Choice(models.Model):
    content = models.CharField(max_length=100)
    intensity = models.IntegerField(default=0)
    question = models.ForeignKey(to='mlic.Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Feedback(models.Model):
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content