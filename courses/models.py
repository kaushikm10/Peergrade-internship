from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.
User._meta.get_field('email')._unique = True


class CreatedClasses(models.Model):
    class_code = models.CharField(max_length=6)
    class_name = models.CharField(max_length=100)
    class_description = models.TextField(max_length=1000)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name



class JoinedClasses(models.Model):
    class_id = models.ForeignKey(CreatedClasses, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_id.class_name


class Assignments(models.Model):
    assignment_name = models.CharField(max_length=100, )
    points = models.IntegerField()
    due_date = models.DateTimeField()
    class_id = models.ForeignKey(CreatedClasses, on_delete=models.CASCADE)
    grading_type = models.BooleanField(default=True)
    teacher_ratio = models.FloatField(blank=True, null=True)
    student_ratio = models.FloatField(blank=True, null=True)
    no_of_peers = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.assignment_name

# for notices and uploads from the student side
class notices(models.Model):
    notice_name = models.CharField(max_length=100)
#    points = models.IntegerField()
#    due_date = models.DateTimeField()
    class_id = models.ForeignKey(CreatedClasses, on_delete=models.CASCADE)
#    grading_type = models.BooleanField(default=True)
#    teacher_ratio = models.FloatField(blank=True, null=True)
#    student_ratio = models.FloatField(blank=True, null=True)
#    no_of_peers = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(default = datetime.now, blank = True)


    def __str__(self):
        return self.notice_name

class noticeFile(models.Model):
    files = models.FileField(upload_to='subs/files/')
    notice_id = models.ForeignKey(notices, on_delete= models.CASCADE)

class Submission(models.Model):
    sub_date = models.DateTimeField(default=timezone.now)
    assignment_id = models.ForeignKey(Assignments, on_delete=models.CASCADE, default=None)
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    marks = models.IntegerField(blank=True, default=0)
    remark = models.CharField(default="Submitted on Time", max_length=100)

    def __str__(self):
        return self.assignment_id.assignment_name + " " + self.student.username

    # def delete(self, *args, **kwargs):
    #   self.delete()
    #   super().delete(*args, **kwargs)


class SubmittedFiles(models.Model):
    sub = models.FileField(upload_to='subs/files/')
    submission_id = models.ForeignKey(Submission, on_delete=models.CASCADE)


class AssignedPeers(models.Model):
    peer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='peer')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    student_marks = models.IntegerField(blank=True, null=True)
    question1 = models.TextField(max_length=1000, blank=True)
    question2 = models.TextField(max_length=1000, blank=True)
    question3 = models.TextField(max_length=1000, blank=True)

class Comments(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)











