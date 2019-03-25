from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'exam_app'
urlpatterns = [
    url(r'^$', views.test_tableList.as_view(), name='list'),
    url(r'^new/$', views.test_tableCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.test_tableDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.test_tableUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.test_tableDelete.as_view(), name='delete'),

	path('question_one/', views.line_chart, name='question_one'),    
	path('line_chart_json/', views.line_chart_json, name='line_chart_json'),    

    path('question_one_gma/', views.line_chart_gma, name='question_one_gma'),    
    path('line_chart_json_gma/', views.line_chart_json_gma, name='line_chart_json_gma'),  

    path('line_chart_package_major_region/', views.line_chart_package_major_region, name='line_chart_package_major_region'),   
    path('line_chart_json_package_major_region/', views.line_chart_json_package_major_region, name='line_chart_json_package_major_region'),   

    path('line_chart_package_major_region_avg/', views.line_chart_package_major_region_avg, name='line_chart_package_major_region_avg'),   
    path('line_chart_json_package_major_region_avg/', views.line_chart_json_package_major_region_avg, name='line_chart_json_package_major_region_avg'),  
    path('line_chart_json_package_major_region_avg_time/', views.line_chart_json_package_major_region_avg_time, name='line_chart_json_package_major_region_avg_time'),    
]
