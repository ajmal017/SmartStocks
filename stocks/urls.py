from django.urls import path
from . import views
from .views import *

urlpatterns = [
   

    path('', StockListView.as_view(), name='stock_list'),
    path('<slug:stock_name>', StockDetailView.as_view(), name='stock_detail'),
    #path('/chart/api/data/<slug:stock_name>',StockDetailView.as_view(),name='stock_detail'),
    #path('api/data',views.get_data, name='api-data'),
    path('api/chart/data', ChartData.as_view()),

]