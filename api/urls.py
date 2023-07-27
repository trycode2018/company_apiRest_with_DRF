from django.urls import path
from .views import CompanyViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('companies',CompanyViewSet)



