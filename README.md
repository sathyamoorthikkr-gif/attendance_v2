# SmartAttend — Student Attendance Tracker

## How to Run

```bash
pip install django pillow
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

## Test Students (already loaded)
| Roll Number   | Name        | Phone      |
|---------------|-------------|------------|
| BCA2024001    | A1VIP       | 9876543210 |
| BCA2024002    | Arun Kumar  | 9876543211 |
| BCA2024003    | Priya S     | 9876543212 |
| BCA2024004    | Karthik M   | 9876543213 |

## Flow
1. Student enters Roll Number → OTP sent to phone
2. Student enters OTP (shown on screen in demo mode)
3. Student enters Today's Daily Code (from Admin Dashboard)
4. GPS auto-captured, Selfie taken → Attendance Marked!

## Admin Dashboard
http://127.0.0.1:8000/admin-dashboard/
- See today's Daily Code
- Present/Absent list with GPS links & photos

## Add More Students
```bash
python manage.py shell
from attendance.models import Student
Student.objects.create(roll_number='BCA2024005', name='Name', phone_number='9999999999')
```
