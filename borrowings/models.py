from django.template.defaultfilters import default
from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Borrowing(models.Model):
    class Status(models.TextChoices):
        PENDING_RENT='PENDING RENT'
        RENTED='RENTED'
        PENDING_RETURN='PENDING RETURN'
        RETURNED='RETURNED'
        REJECTED='REJECTED'

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=Status.choices ,
        default=Status.PENDING_RENT
    )

    requested_at = models.DateTimeField(auto_now_add=True)
    approve_at = models.DateTimeField(null=True , blank=True)
    returned_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.user} -> {self.book} ({self.status})"
