from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        raw_token = request.headers.get("Authorization")
        if raw_token and not raw_token.startswith("Bearer "):
            raw_token = f"Bearer {raw_token}"   
        request.META["HTTP_AUTHORIZATION"] = raw_token
        return super().authenticate(request)
