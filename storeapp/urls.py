from . import views
from rest_framework import routers



router=routers.DefaultRouter()

router.register('bannertop',views.BannerTopViewSet)
router.register('bannerdown',views.BannerDownViewSet)
router.register('category',views.CategoryViewSet)
router.register('products',views.ProductViewSet)

urlpatterns = router.urls
