# valid style importing

# direct importing
import django.http.HttpResponse as HttpResponse
import django.http.JsonResponse as JsonResponse

# one line multi importing
from   django.http  import HttpResponse, JsonResponse

# direct import dari directory yang sama
# contoh akan mengimport file database.py
import .database.Mongod as Mongod
import .database.MySQL  as MySQL

# one line import dari dir yang sama
from .database import Mongod, MySQL

#...
