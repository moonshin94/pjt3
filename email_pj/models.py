from django.db import models
# from django.db.backends.postgresql.base import DatabaseWrapper
# DatabaseWrapper.data_types['DataTimeField'] = 'timestamp'
# Create your models here.
class USER_ID(models.Model):
    USER_ID = models.IntegerField(max_length = 9, primary_key=True, null=False)
    USER_EMAIL = models.CharField(max_length=200, null=False, null=False)
    USER_PW = models.CharField(max_length=100, null=False)
    USER_NAME = models.CharField(max_length=50, null=False)
    USER_EMAIL_TYPE = models.ForeignKey(MAIL_SERVER_INFO.MAIL_ID,on_delete=models.CASCADE, null=False)  # 최대길이 설정x

class MAIL_SERVER_INFO(models.Model):
    MAIL_SERVER_ID = models.CharField(max_length = 10, primary_key=True, null=False)
    MAIL_SERVER_NAME = models.CharField(max_length = 50, null=False)
    IMAP_DOMAIN = models.CharField (max_length=100, null=False)
    IMAP_PORT = models.IntegerField (max_length=100, null=False)
    SMTP_DOMAIN = models.CharField(max_length = 100, null=False)
    SMTP_PORT = models.IntegerField(max_length=5, null=False)

class ORDERS(models.Model):
    MAIL_ID = models.IntegerField(max_length = 10, primary_key=True, null=False)
    SENDER_ID = models.ForeignKey(USER.USER_ID,on_delete=models.CASCADE, null=False) # 최대길이 설정x
    SENDER_EMAIL = models.ForeignKey(USER.USER_EMAIL,on_delete=models.CASCADE, null=False) # 최대길이 설정x
    RECEIVER_ADRESS = ArrayField(models.TextField(), null=False)
    REFER_ADRESS = ArrayField(models.TextField())
    ME_FLAG = models.BooleanField(null=True)
    TITLE = models.CharField(max_length=200, null=False)
    CONTENT = models.TextField()
    ATTACHMENTS = ArrayField(ArrayField(models.TextField())
    SEND_DT = models.DateTimeField(auto_now_add=True, null=False)
    IMP_FLAG = models.BooleanField(null=True)

class FILE(models.Model):
    FILE_ID = models.IntegerField(max_length = 10, primary_key=True, null=False)
    UPLOADER = models.ForeignKey(USER.USER_ID,on_delete=models.CASCADE, null=False) # 최대길이 설정x
    UPLOAD_DT = models.DateTimeField(auto_now_add=True, null=False)
    FILE_NAME = models.CharField(max_length=200, null=False)
    FILE_PATH = models.TextField(null=False)

class USER_SIGN(models.Model):
    SIGN_ID = models.IntegerField(max_length = 10, primary_key=True, null=False)
    USER_ID = models.ForeignKey(USER.USER_ID,on_delete=models.CASCADE, null=False) # 최대길이 설정x
    SIGN_NAME = models.CharField(max_length=50, null=False)
    SIGN_CONT = models.TextField(null=False)

class LOG(models.Model):
    LOG_ID = models.IntegerField(max_length = 10, primary_key=True, null=False)
    LOG_TYPE = models.CharField (max_length=10, null=False)
    USER_ID = models.ForeignKey(USER.USER_ID,on_delete=models.CASCADE, null=False) # 최대길이 설정x
    DT = models.DateTimeField(auto_now_add=True, null=False)
    STATUS = models.CharField (max_length=10, null=False)
    DETAIL = models.TextField()

class SENTENCE(models.Model):
    Category_ID =  models.IntegerField(primary_key=True, null=False)
    Upper_Category = models.TextField(null=False)
    Lower_Category = models.TextField(null=False)
    Sentence = models.TextField(null=False)
