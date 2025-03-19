from django.shortcuts import redirect



class LoginRequiredMiddleware:
    """Middleware to enforce login for all views except specified public views."""

    def __init__(self, get_response):
        print("middleware start...!")                     #This method runs only once when Django starts.
        self.get_response = get_response

    def __call__(self, request):                                     
        # List of paths that don't require authentication     #This method is called for every request.              
        public_paths = ['/login/', '/public/']

        # Check if the request path is not in the public paths
        if request.path not in public_paths:
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                # Redirect to login page if not authenticated
                return redirect('/login/')

        # Continue processing the request
        response = self.get_response(request)                          
        return response
    
    # Calls self.get_response(request), which passes the request to the next middleware  