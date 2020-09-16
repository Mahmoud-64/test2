from rest_framework import routers
from coffeMacine import views as myapp_views

router = routers.DefaultRouter()
router.register(r'machines', myapp_views.CoffeeMachineViewset)
router.register(r'pods', myapp_views.CoffeePodViewset)
