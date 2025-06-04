from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
#데이터베이스를 통틀어서 모델이라고 합니다
#최근 개발에 트랜드는 MVC패턴 Model View Controller mvc => java spring
#모델은 뭔가요? 데이터가 모델이라는 Object
#Django에서는 데이터가 모델이라는 객체로 생성되고 실제로는 데이테베이스의 테이블 입니다

# Create your models here.
