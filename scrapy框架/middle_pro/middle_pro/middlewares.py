class MiddleProDownloaderMiddleware:

    def process_request(self, request, spider):
        print('这里是请求拦截')
        return None

    def process_response(self, request, response, spider):
        print('这里是响应拦截')
        return response

    def process_exception(self, request, exception, spider):
        print('这里是异常拦截')
        pass
