from django.urls import path

from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('Add_cat/', views.Add_cat, name="Add_cat"),
    path('saveCategory/', views.saveCategory, name="saveCategory"),
    path('cdetails/', views.cdetails, name="cdetails"),
    path('cdetails/', views.cdetails, name="cdetails"),
    path('updatec/<int:Id>', views.updatec, name="updatec"),
    path('edit/<int:Id>', views.edit, name="edit"),
    path('delc/<int:Id>', views.delc, name="delc"),
    path('add_products/', views.product_page, name="add_products"),
    path('productsave/', views.productsave, name="productsave"),
    path('pdetails/', views.pdetails, name="pdetails"),
    path('edit_product/<int:p_id>', views.pedit, name="edit_product"),
    path('updatep/<int:p_id>', views.updatep, name="updatep"),
    path('delete/<int:p_id>', views.delp, name="delete"),
    path('', views.loginpage, name="login"),
    path('adminlog/', views.adminlog, name="adminlog"),
    path('contactDet/', views.contactDet, name="contactDet"),
    path('delContact/<int:Id>', views.delContact, name="delContact"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
]