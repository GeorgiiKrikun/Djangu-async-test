# Djangu-async-test

Just a test repo that I made to help somebody from reddit to understand async requests in Django: https://www.reddit.com/r/django/comments/14gx750/will_a_slow_api_slow_down_my_app_for_everyone/jp83v0z/?context=3

To start it, you need to use uvicorn to allow for async views:

`uvicorn core.asgi:application --port 8000 --host 0.0.0.0 --workers 13`
