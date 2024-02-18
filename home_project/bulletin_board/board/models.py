from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Post(models.Model):

    tanks = 'TN'
    healers = 'HL'
    dd = 'DD'
    merchants = 'MR'
    guild_masters = 'GM'
    quest_givers = 'QG'
    blacksmiths = 'BS'
    tanners = 'TA'
    potion_makers = 'PM'
    spell_masters = 'SM'

    CATEGORY = [
        (tanks, 'Танки'),
        (healers, 'Хилы'),
        (dd, 'ДД'),
        (merchants, 'Торговцы'),
        (guild_masters, 'Гилдмастеры'),
        (quest_givers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (potion_makers, 'Зельевары'),
        (spell_masters, 'Мастер заклинаний')
    ]

    name = models.CharField(max_length=255)
    text = RichTextUploadingField()
    category = models.CharField(max_length=2, choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def comment(self):
        return Comment.objects.filter(post_id=self.pk)

    def len_comment(self):
        return len(Comment.objects.filter(post_id=self.pk))

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}: {self.category}'


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])

    def __str__(self):
        return f'{self.post} : {self.text[0:50]}...'

