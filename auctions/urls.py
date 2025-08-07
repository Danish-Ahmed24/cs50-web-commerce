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
    path('closeAuction',views.closeAuction,name="closeAuction"),
    path('addComment',views.addComment,name="addComment"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('categories',views.categories,name="categories"),
    path('category/<str:category>',views.category,name="category"),
    path("listing/<int:id>",views.listing,name="listing")
]
 