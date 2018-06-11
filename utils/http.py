import requests


def requests_noauth(method, *args, **kwargs):
    if not kwargs:
        kwargs = {}
    headers = {'content-type': 'application/json', 'Accept': 'application/json'}
    if "headers" in kwargs:
        headers.update(kwargs["headers"])
        del kwargs["headers"]
    if method == "POST":
        return requests.post(*args, headers=headers, **kwargs)
    elif method == "GET":
        return requests.get(*args, headers=headers, **kwargs)
    elif method == "PUT":
        return requests.put(*args, headers=headers, **kwargs)
    elif method == "DELETE":
        return requests.delete(*args, headers=headers, **kwargs)
    elif method == "PATCH":
        return requests.patch(*args, headers=headers, **kwargs)
    else:
        raise Exception("invalid http method")