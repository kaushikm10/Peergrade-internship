from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name="signup"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.home, name='homepage'),
    path('cur_notice/<notice_id>', views.cur_notice, name="cur_notice"),
    path('cur_class/<class_id>', views.cur_class, name='cur_class'),
    path('joinclass/', views.joinclass, name='joinclass'),
    path('join_cur_class/<class_id>', views.join_cur_class, name='join_cur_class'),
    path('cur_assignment_join/<assignment_id>', views.cur_assignment_join, name='cur_assignment_join'),
    path('cur_assignment_create/<assignment_id>/', views.cur_assignment_create, name='cur_assignment_create'),
    path('cur_student_submission/<submission_id>/', views.cur_student_submission, name='cur_student_submission'),
    path('peers_assigned/<assignment_id>/', views.peers_assigned, name='peers_assigned'),
    path('cur_peer_submission/<submission_id>/', views.cur_peer_submission, name='cur_peer_submission'),
    path('assign_peers/<assignment_id>/<class_id>/', views.assign_peers, name='assign_peers'),
    path('view_feedback/<assignment_id>', views.view_feedback, name='view_feedback'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
