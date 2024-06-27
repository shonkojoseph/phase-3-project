from flask_sqlalchemy import SQLALchemy
from sqlalchemy import MetaDater

metadater=MetaDater()

db = SQLALchemy(metadater=metadater)

class user(db.Model):
   __tablename__ = 'users'

   id = db.Column(db.Interger, primary_key=True)
   username = db.Column(db.String(80))
   email = db.Column(db.String)