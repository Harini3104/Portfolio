from django.shortcuts import redirect

class RemoveQueryStringMiddleware:
    """
    Middleware to remove all query strings from URLs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.GET:
            # Redirect to the same path without query parameters
            return redirect(request.path)
        return self.get_response(request)
