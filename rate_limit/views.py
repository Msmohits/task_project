from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RateLimitedView(APIView):
    """
    A rate-limited API endpoint that restricts requests based on user IP.
    Allows 5 requests per minute.
    """
    permission_classes = [IsAuthenticated]

    RATE_LIMIT = 5
    TIME_WINDOW = 60  

    def get_client_ip(self, request):
        """Retrieve the client IP address."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        ip = self.get_client_ip(request)

        cache_key = f"rate_limit:{user_id or ip}"
        request_count = cache.get(cache_key, 0)

        if request_count >= self.RATE_LIMIT:
            return JsonResponse(
                {"error": "Rate limit exceeded. Try again later."},
                status=429
            )

        cache.set(cache_key, request_count + 1, timeout=self.TIME_WINDOW)

        return JsonResponse({"message": "Request successful!, pending requests: " + str(self.RATE_LIMIT - request_count - 1)})
