from django.shortcuts import render
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import asyncio
# Create your views here.

def long_running_function(request):
    print("Starting long_running_function...")
    start_time = datetime.datetime.now()
    
    while True:
        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time.total_seconds() >= 15:  # Wait for 15 seconds
            break
    return HttpResponse("finished long_running_function")

async def async_sleep(request):
    await asyncio.sleep(15)
    return HttpResponse("Hello, async Django!")

def sleep_function(request):
    print("Starting sleep_function...")
    import time
    time.sleep(15)
    return HttpResponse("finished sleep_function")

def quick_function(request):
    print("Starting quick_function...")
    return HttpResponse("finished quick_function")