from django.db import models
from django.utils import timezone
import random, string

# ── College GPS (Center point) ──────────────────────────────
COLLEGE_LAT = 11.663372
COLLEGE_LNG = 78.258265
ALLOWED_RADIUS_METERS = 5  # student must be within 5m

class Student(models.Model):
    roll_number  = models.CharField(max_length=20, unique=True)
    name         = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

class AdminProfile(models.Model):
    name         = models.CharField(max_length=100, default="Satyamoorthy BCA")
    phone_number = models.CharField(max_length=15, default="+919043198508")
    section      = models.CharField(max_length=50, default="III BCA - D Section")

    def __str__(self):
        return self.name

class AdminOTP(models.Model):
    otp_code   = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used    = models.BooleanField(default=False)

    def is_valid(self):
        elapsed = (timezone.now() - self.created_at).seconds
        return elapsed < 600 and not self.is_used

class DailyCode(models.Model):
    date = models.DateField(unique=True)
    code = models.CharField(max_length=6)

    @classmethod
    def get_or_create_today(cls):
        today = timezone.now().date()
        obj, _ = cls.objects.get_or_create(
            date=today,
            defaults={'code': ''.join(random.choices(string.digits, k=6))}
        )
        return obj

    def __str__(self):
        return f"{self.date} - {self.code}"

class OTP(models.Model):
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    otp_code   = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used    = models.BooleanField(default=False)

    def is_valid(self):
        elapsed = (timezone.now() - self.created_at).seconds
        return elapsed < 600 and not self.is_used

class Attendance(models.Model):
    STATUS_CHOICES = [('Present','Present'),('Absent','Absent')]
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    date       = models.DateField(default=timezone.now)
    daily_code = models.ForeignKey(DailyCode, on_delete=models.CASCADE)
    latitude   = models.FloatField(null=True, blank=True)
    longitude  = models.FloatField(null=True, blank=True)
    distance_m = models.FloatField(null=True, blank=True)
    photo      = models.ImageField(upload_to='attendance_photos/', null=True, blank=True)
    marked_at  = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(max_length=10, default='Present', choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
