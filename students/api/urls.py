from rest_framework import routers
from students.api.api import StudentsViewSet

routerApi = routers.DefaultRouter()
routerApi.register('api/students', StudentsViewSet, 'students')

urlpatterns = routerApi.urls
