from rest_framework import routers

class DefoultRouter(routers.DefaultRouter):

    def extend(self, router):
        self.registry.extend(router.registry)