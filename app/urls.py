from app import views
from django.urls import path


urlpatterns = [
    
    # Index #
    path('',views.indexview,name='index'),
    path('search',views.search,name='search'),
    path('vehicles',views.vehicles,name='vehicles'),
    path('vehicle_details/<int:id>/',views.vehicle_details,name='vehicle_details'),
    path('companies',views.companies,name='companies'),
    path('services',views.services,name='services'),
    path('service_payment/<int:id>/',views.service_payment,name='service_payment'),
    path('memberships',views.memberships,name='memberships'),
    path('payment_gateway/<int:id>/',views.payment_gateway,name='payment_gateway'),
    path('already_subscribed/<int:id>/',views.already_subscribed,name='already_subscribed'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('blog_details/<int:id>/', views.blog_details, name='blog_details'),
    path('book/<int:id>', views.book, name='book'),
    path('book_details/<int:id>', views.book_details, name='book_details'),
    path('already_booked_service/<int:id>/',views.already_booked_service,name='already_booked_service'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('login', views.LoginView.as_view(), name='login'),


    # Buyer #
    path('home',views.home,name='home'),
    path('buyer_register', views.RegisterBuyerView.as_view(), name='buyer-register'),
    path('buying/<int:id>/',views.buying,name='buying'),
    path('success_page/<int:id>/',views.success_page,name='success_page'),


    # Seller #
    path('dashboard',views.dashboard,name='dashboard'),
    path('seller_register', views.RegisterSellerView.as_view(), name='seller-register'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),


    # Profile #
    path('profile',views.profile,name='profile'),
    path('add_profile',views.add_profile,name='add_profile'),

    # Admin #
    path('admin_page',views.admin_page,name='admin_page'),
    path('manage',views.manage_data,name='manage'),

    # Blog #
    path('add_blog',views.add_blog,name='add_blog'),
    path('edit_blog/<int:id>',views.edit_blog),
    path('update_blog/<int:id>',views.update_blog),
    path('delete_blog/<int:id>',views.destroy_blog),

    # Vehicle #
    path('edit_vehicle/<int:id>',views.edit_vehicle),
    path('update_vehicle/<int:id>',views.update_vehicle),
    path('delete_vehicle/<int:id>',views.destroy_vehicle),

    # Contact #
    path('all_contacts',views.all_contacts,name='all_contacts'),
    path('edit_contact/<int:id>',views.edit_contact),
    path('update_contact/<int:id>',views.update_contact),
    path('delete_contact/<int:id>',views.destroy_contact),

    # Subscribers #
    path('all_memberships_applicants',views.all_memberships_applicants,name='all_memberships_applicants'),
    path('edit_memberships_applicants/<int:id>',views.edit_memberships_applicants),
    path('update_memberships_applicants/<int:id>',views.update_memberships_applicants),
    path('delete_memberships_applicants/<int:id>',views.destroy_memberships_applicants),

    # Buyers #
    path('all_buyers_applicants',views.all_buyers_applicants,name='all_buyers_applicants'),
    path('edit_buyers_applicants/<int:id>',views.edit_buyers_applicants),
    path('update_buyers_applicants/<int:id>',views.update_buyers_applicants),
    path('delete_buyers_applicants/<int:id>',views.destroy_buyers_applicants),

    # Service Slots #
    path('all_service_slots',views.all_service_slots,name='all_service_slots'),

    # Users #
    path('user_data',views.user_data,name='user_data'),

]