from django.db import models


# Create your models here.

class user_info_one(models.Model):
    man = "男"
    women = "女"
    sex_choices = (
        (man, "男"),
        (women, "女"),
    )

    user_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    memo = models.TextField(blank=True)
    sex = models.CharField(
        max_length=2,
        choices=sex_choices,
        default=man,
    )

    def __str__(self):
        return self.user_id


class Author(models.Model):
    man = "男"
    women = "女"
    sex_choices = (
        (man, "男"),
        (women, "女"),
    )

    author_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    memo = models.TextField(blank=True)
    sex = models.CharField(
        max_length=2,
        choices=sex_choices,
        default=man,
    )

    def __str__(self):
        return self.author_id


class Book(models.Model):
    XH = "玄幻小说"
    XX = "仙侠小说"
    KH = "科幻小说"
    BookType_choices = (
        (XH, "玄幻"),
        (XX, "仙侠"),
        (KH, "科幻"),
    )

    Ongoing = "更新中"
    TheEnd = "已完结"
    Status_choices = (
        (Ongoing, "更新"),
        (TheEnd, "完结"),
    )

    book_name = models.CharField(max_length=30, unique=True)
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_type = models.CharField(
        max_length=8,
        choices=BookType_choices,
        default=XH,
    )
    book_sum = models.IntegerField()
    book_memo = models.CharField(max_length=200, blank=True)
    book_start_time = models.DateTimeField(auto_now_add=True)
    book_update_time = models.DateTimeField(auto_now=True)
    book_status = models.CharField(
        max_length=6,
        choices=Status_choices,
        default=Ongoing,
    )
    book_img = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.book_name


class Book_Detail(models.Model):
    book_name = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_num = models.IntegerField()
    book_file = models.FileField(upload_to='book/')

    def __str__(self):
        return f'{self.book_name}_{self.book_num}'


class Forum(models.Model):
    book_name = models.ForeignKey('Book', on_delete=models.CASCADE)
    user_name = models.ForeignKey('user_info_one', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

