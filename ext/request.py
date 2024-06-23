from rest_framework.request import Request


class MyRequest(Request):
    def __init__(self, *args, **kwargs):
        super(MyRequest, self).__init__(*args, **kwargs)

    def get(self, url, **kwargs):
        return super(MyRequest, self).get(url, **kwargs)

    def post(self, url, **kwargs):
        return super(MyRequest, self).post(url, **kwargs)

    def put(self, url, **kwargs):
        return super(MyRequest, self).put(url, **kwargs)

    def delete(self, url, **kwargs):
        return super(MyRequest, self).delete(url, **kwargs)

    def head(self, url, **kwargs):
        return super(MyRequest, self).head(url, **kwargs)

    def options(self, url, **kwargs):
        return super(MyRequest, self).options(url, **kwargs)

    def patch(self, url, **kwargs):
        return super(MyRequest, self).patch(url, **kwargs)