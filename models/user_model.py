from default_settings import db 


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(length=100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(length=100), nullable=False)
    

    def  __init__(self,name,  password,type):

       
        
        self.name = name,
        self.password = password
        self.type = type
        
      

    

 

   
