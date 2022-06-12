import jwt
from blog.settings.base import SECRET_KEY

def user_token(request):

    tokenJWT = request.headers['Authorization'].split()[1]
    tokenDecoded = jwt.decode(tokenJWT, SECRET_KEY, algorithms=["HS256"])
    user = tokenDecoded['user_id']

    return user