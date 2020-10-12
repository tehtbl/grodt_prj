from django.urls import path

from .. import views

urlpatterns_mycheckermodel = [
    path('mycheckermodels/', views.MyCheckerModelListView.as_view(), name="mycheckermodels_list"),

    path('mycheckermodel/new/', views.MyCheckerModelCreateView.as_view(), name="mycheckermodel_create"),
    path('mycheckermodel/<uuid:uuidpk>/edit/', views.MyCheckerModelUpdateView.as_view(), name="mycheckermodel_edit"),
    path('mycheckermodel/<uuid:uuidpk>/delete/', views.MyCheckerModelDeleteView.as_view(), name="mycheckermodel_delete"),
    path('mycheckermodel/<uuid:uuidpk>/', views.MyCheckerModelDetailView.as_view(), name="mycheckermodel_detail"),
]
