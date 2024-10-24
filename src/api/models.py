from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
    #Funcion que genera el hash para codificar la contraseña
    def generate_password_hash(self, password):
        return bcrypt.generate_password_hash(password).decode("utf-8")
    #Funcion para comparar la contraseña que reciba con el hash de la base de datos
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)
    
    #Funcion para crear un usuario, la usaremos en la ruta de registro
    def create_user(self,email, password):
        self.email= email
        self.password= self.generate_password_hash(password)
        self.is_active= True
        db.session.add(self)
        db.session.commit()



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }