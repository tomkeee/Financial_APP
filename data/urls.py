from django.urls import path
from .views import InstrumentInvestments,RegionInvestments,SectorInvestments,InstrumentsAPI,InstrumentAPI,ClientsData

urlpatterns =[
    path('',InstrumentInvestments.as_view(),name="instrumentInvestment"),
    path('regions/',RegionInvestments,name="regionInvestments"),
    path('sectors/',SectorInvestments,name="sectorInvestments"),
    path('api/',InstrumentsAPI),
    path('api/<int:pk>/',InstrumentAPI),
    path("users/",ClientsData)
]