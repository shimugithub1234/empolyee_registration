from django.conf.urls import url
from.views import EmployeeListView, EmployeeCreate, EmployeeDetail, EmployeeUpdate

app_name = 'employee'

urlpatterns = [
            url(r'^list/', EmployeeListView.as_view(), name='list'),
            url(r'^create/', EmployeeCreate.as_view(), name='create'),
            url(r'^(?P<pk>\d+)/update/$', EmployeeUpdate.as_view(), name='update'),
            url(r'^detail/(?P<pk>\d+)/$', EmployeeDetail.as_view(), name='detail'),
]