from django.urls import path 

from . import views

urlpatterns = [
    path("all/", views.ListAllPropertyAPIView.as_view(), name="all_properties"),
    path("agent/",views.ListAgentPropertyAPIView.as_view(), name="agent_properties"),
    path("create/", views.create_property_api_view, name="create_property_api_view"),
    path("details/<slug:slug>/", views.PropertyDetailView.as_view(), name="details"),
    path("update/<slug:slug>/", views.update_property_api_view, name="update_property_api_view"),
    path("delete/<slug:slug>/", views.delete_property_api_view, name="delete_property_api_view"),
    path("search", views.PropertySearchAPIView.as_view(), name="property_search"),
]