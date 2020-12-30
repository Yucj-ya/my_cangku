from django.utils.deprecation import MiddlewareMixin


# MiddlewareMixin
class BookMiddlewareMixin(MiddlewareMixin):

    # 每次请求前 都会调用
    def process_request(self, request):
        print("request 每次请求前 都会调用1111111111")

    # 每次响应前 都会调用
    def process_response(self, response):
        print("request 每次响应前 都会调用111111111111111")

        return response


class BookMiddlewareMixin2(MiddlewareMixin):

    # 每次请求前 都会调用
    def process_request(self, request):
        print("request 每次请求前 都会调用2222222222")

    # 每次响应前 都会调用
    def process_response(self, request,response):
        print("request 每次响应前 都会调用222222222222222")

        # 记得响应返回
        return response
