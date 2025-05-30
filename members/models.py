from django.db import models  # Django가 제공하는 DB모델 기능 불러옴


class Member(models.Model):  # 모델이름: Member
    firstname = models.CharField(max_length=255)  # 이름
    lastname = models.CharField(max_length=255)  # 성
    phone = models.IntegerField()
    joined_date = models.DateField()


# Create your models here.


'''
개발 트랜드에는 MVC(Model View Controller) → java string
model: 데이터가 모델이라는 object
django에서는 데이터가 모델이라는 객체로 생성되고 실제로는 데이터베이스의 테이블
'''