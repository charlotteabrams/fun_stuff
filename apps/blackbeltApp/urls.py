from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new_item$', views.new, name="new_item"),
	url(r'^(?P<id>\d+)$', views.show, name="show_item"),
	url(r'^item_add/(?P<id>\d+)$', views.add_to_wishlist, name="item_add"),
	url(r'^delete_item/(?P<id>\d+)$', views.delete, name="item_delete"),
	url(r'^remove_item/(?P<id>\d+)$', views.remove, name="item_remove"),
	url(r'^create', views.create, name="create_item"),

]