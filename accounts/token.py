# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.signals import user_logged_in, user_logged_out
 
 
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
 
 
# #
# # [Signal] After user logged in, create new user's token
# #
# def create_api_token(sender, user, request, **kwargs):
#     Token.objects.get_or_create(user=user)
 
 
# user_logged_in.connect(create_api_token)
 
 
# #
# # [Signal] After user logged out, remove user's token
# #
# def delete_api_token(sender, user, request, **kwargs):
#     Token.objects.filter(user=user).delete()
 
# user_logged_out.connect(delete_api_token)
 