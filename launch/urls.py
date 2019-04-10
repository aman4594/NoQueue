from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RestaurantDetailView, MenuDetailView,ItemCreateView,ItemDetailView,ItemUpdateView, ItemDeleteView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView
from launch.forms import CustomAuthForm

app_name = "launch"

urlpatterns = [

    # Initial page when app launches
    path('', views.home, name='launch-home'),

    #Navbar limks
    path('about/', views.about, name='launch-about'), 
    path('contact/', views.contact, name='launch-contact'),
    path('blog-home/', views.blog_home, name='launch-bloghome'),
    path('blog-details/', views.blog_details, name='launch-blogdetails'), 

    # Page that loads when the user registers
    path('register/', views.register, name='register'),

    # Page that aks how to register. As a customer or register
    path('register-owner/', views.register_owner, name='register-owner'),
    path('register-customer/', views.register_customer, name='register-customer'),

    # Page that asks how to launch the page when logged in. As a customer or register
    path('owner-register/', views.owner_profile_view, name='launch-register-owner'),
    path('customer-register/', views.customer_profile_view, name='launch-register-customer'),
    
    # Paths to redirect towards log in and log out pages
    path('login/', auth_views.LoginView.as_view(template_name='launch/login.html', authentication_form=CustomAuthForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='launch/logout.html'), name='logout'),

    # Path that shows the profile for customers or owner
    path('profile/', views.show_profile, name='profile'),

    #shows detail of restuarant using class based views
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'), 

    #creates restuarant using class based views
    path('restaurant/new/', RestaurantCreateView.as_view(), name='restaurant-create'),

    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),

    path('restaurant/<int:pk>/menu/', MenuDetailView.as_view(), name='restaurant-menu'),


    path('restaurant/<int:pk>/menu/add', ItemCreateView.as_view(), name='item-create'),
    path('restaurant/<int:rk>/menu/<int:pk>', ItemDetailView.as_view(), name='item-detail'), 
    path('restaurant/<int:rk>/menu/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('restaurant/<int:rk>/menu/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('profile/', views.my_profile, name='my_profile'),
    
 
    path('restaurant/<int:rk>/menu/<int:pk>/addtocart/', views.add_to_cart, name='add-to-cart'),   
    path('order-summary/', views.order_details, name="order-summary"),
    path('item/<int:pk>/deletefromcart', views.delete_from_cart, name='delete-item'),
    path('/order_summary/', views.order_details, name="order-summary"),
    path('item/<int:pk>/deletefromcart/', views.delete_from_cart, name='delete-item'),
    path('update-transactions/', views.update_transaction_records, name='update_records'),
    path('order-summary/checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.success, name='purchase_success'),
    path('search-results/', views.search, name='searchbar'),
    path('test/', views.insertTransaction, name='Trans')
    

    





]	
