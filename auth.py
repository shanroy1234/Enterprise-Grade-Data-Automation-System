from jose import jwt
SECRET='secret'

def create_token(data):
    return jwt.encode(data,SECRET,'HS256')

def verify(token):
    return jwt.decode(token,SECRET,['HS256'])
