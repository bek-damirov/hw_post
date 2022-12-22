from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.author}-{self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.text}'


marks = (
    ('like', 'LIKE'),
    ('dizlake', 'DIZLAKE')
)


class Mark(models.Model):
    mark_value = models.CharField(max_length=20, choices=marks)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.mark_value
