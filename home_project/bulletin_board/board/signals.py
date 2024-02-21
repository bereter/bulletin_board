from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from django.core.mail import EmailMultiAlternatives
from bulletin_board.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string


@receiver(post_save, sender=Comment)
def send_message_appointment(sender, instance, created, **kwargs):
    if created and instance.post.user.email:
        subject = f'''Пользователь {instance.post.user.email}, откликнулся на ваш пост - '{instance.post.name}' '''

        html_content = render_to_string('email_message.html', {'instance': instance, })

        msg = EmailMultiAlternatives(
            subject=f'Отклик на пост - {instance.post.name}',
            from_email=DEFAULT_FROM_EMAIL,
            to=[instance.post.user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
