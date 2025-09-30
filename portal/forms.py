from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message="Por favor, insira seu nome.")])
    email = StringField('E-mail', validators=[DataRequired(message="Por favor, insira seu e-mail."), Email(message="Endereço de e-mail inválido.")])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired(message="Por favor, escreva uma mensagem.")])
    enviar = SubmitField('Enviar Mensagem')