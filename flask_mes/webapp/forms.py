from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length


class Loginform(Form):
    username = StringField('User')
    passwd = StringField('Password')

    def validate(self):
        from .models import User
        check_validate = super(Loginform, self).validate()
        if self.username.data=='' or self.passwd.data=='':
            self.username.errors.append('can not be null')
            return False
        user = User.query.filter_by(username = self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False
        if self.passwd.data != user.passwd:
            self.username.errors.append('Invalid username or password')
            return False
        return True

class Regform(Form):
    username = StringField('User',validators=[InputRequired()])
    passwd = StringField('Password',validators=[InputRequired()])

    def validate(self):
        from .models import User
        check_validate = super(Regform, self).validate()
        if self.username.data=='' or self.passwd.data=='':
            self.username.errors.append('can not be null')
            return False
        user = User.query.filter_by(username = self.username.data).first()
        if user:
            self.username.errors.append('username has been used')
            return False
        return True


class Publish(Form):
    title = StringField('Title')
    text = TextAreaField('Input the text')

    def validate(self):
        check_validate = super(Publish, self).validate()
        if self.title.data=='' or self.text.data=='':
            self.username.errors.append('can not be null')
            return False
        return True
