from .models import RequestLog

class CaptureRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        origin = request.META.get('HTTP_ORIGIN')
        # get the origin path
        # request.META.get('HTTP_REFERER')
        print("-------path---", request.get_full_path())
        # print("request.META: ", request.META)
        print("request.META.get('HTTP_REFERER'): ", request.META.get('HTTP_REFERER'))
        print("================================================")
        print("origin: ", origin)
        print("path: ", request.method)
        print("path: ", request.path)
        
        # print("data: ", request.body.decode('utf-8') if request.body else "No body")
        if (origin == 'http://127.0.0.1:5173'\
            or origin == 'http://127.0.0.1:5173/'\
                or origin == 'https://rainbow-sports.vercel.app'\
                    or origin == 'https://rainbow-sports.vercel.app/')\
                    and request.path != '/api/logs/':  
            # Log request or perform desired action
            
            obj = RequestLog.objects.create(
                method=request.method,
                path=request.path,
                source=origin
            )
            print("you're the expected client and log has been saved")
            print(obj)
        else:
            print("================================================")
            print("you're not from home page or you're not the expected client");
        #     print("================================================")

        return response
