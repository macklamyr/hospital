from django.urls import path
from .views import AppointmentList, AppointmentView, AppointmentDetail, AppointmentCreate, AppointmentUpdate, AppointmentDelete


urlpatterns = [
   path('list/', AppointmentList.as_view(), name='appointments'),
   path('<int:pk>', AppointmentDetail.as_view(), name='appointment'),
   path('', AppointmentView.as_view()),
   path('create/', AppointmentCreate.as_view(), name='appointment_add'),
   path('<int:pk>/update/', AppointmentUpdate.as_view(), name='appointment_update'),
   path('<int:pk>/delete/', AppointmentDelete.as_view(), name='appointment_delete'),
]
