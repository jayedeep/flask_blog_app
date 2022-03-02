import secrets
import os
from PIL import Image
from flask_mail import Message
from flaskblog import create_app,mail
from flask import url_for

def save_profile(profile_pic):
    random_hex=secrets.token_hex(8)
    _,f_ext=os.path.splitext(profile_pic.filename)
    profile_fn=random_hex+f_ext
    picture_path=os.path.join(create_app.root_path,'static/profile_pic',profile_fn)
    # profile_pic.save(picture_path)

    output_size=(125,125)
    i=Image.open(profile_pic)
    i.thumbnail(output_size)
    i.save(picture_path)
    return profile_fn



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)