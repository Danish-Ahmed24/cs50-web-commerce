from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing",views.createListing,name="createListing"),
    path('addWishlist',views.addWishlist,name="addWishlist"),
    path('delWishlist',views.delWishlist,name="delWishlist"),
    path('placeBid',views.placeBid,name="placeBid"),
    path("listing/<int:id>",views.listing,name="listing")
]
 