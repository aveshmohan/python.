from django.urls import path
from app import views, admin_views, nurse_views, user_views

urlpatterns=[

    path('',views.demo,name='demo'),
    path('user_reg', views.user, name='uuser'),
    path('reg_nurse', views.Nurse_reg, name='nurse_reg'),
    path('loginview', views.login_view, name='login'),
    path('logout', views.log_out,name='llogout'),




    path('admin_page',admin_views.adminpage,name='admin'),
    path('hospital_add', admin_views.hospital_add, name='h_add'),
    path('formview', admin_views.formview, name='h_view'),
    path('edit/<int:id>', admin_views.formedit, name='edit'),
    path('del/<int:id>', admin_views.form_del, name='del'),
    path('nurseview', admin_views.nurseview, name='nnurseview'),
    path('nurseedit/<int:id>',admin_views.nurseedit,name='nnurse_edit'),  # doubt int
    path('nursedel/<int:id>',admin_views.nursedel,name='nurse_del'),
    path('userview',admin_views.userview,name='uuserview'),
    path('useredit/<int:id>',admin_views.useredit,name='uuseredit'),
    path('userdel/<int:id>',admin_views.userdel,name='uuserdel'),
    path('admincomplaintsview', admin_views.admincomplaintview, name='admin_comp_view'),
   # path('reply/<int:id>', admin_views.comp_reply, name='reply'),
    path('replycomp/<int:id>', admin_views.reply_complaint, name='reply_comp'),
    path('vaccine_add', admin_views.vaccine_add, name='Vaccine'),
    path('vaccineview', admin_views.vaccine_view, name='Vaccine_view'),
    path('vaccineedit/<int:id>', admin_views.vaccine_edit, name='Vaccine_edit'),
    path('vaccinedel/<int:id>', admin_views.vaccine_del, name='Vaccine_del'),
    path('admin_schedule_view', admin_views.admin_scheduleview, name='admin_sched_view'),
    path('schedule/approve/<int:id>', admin_views.schedule_approve, name='schedule_approved'),
    path('schedule/reject/<int:id>', admin_views.schedule_reject, name='schedule_rejected'),
    path('schedulepending/<int:id>', admin_views.schedule_pending, name='schedule_pend'),
    path('admin_appoinmentview', admin_views.admin_appoinmentview, name='admin_appoinment_view'),
    path('appoinmentapprove/<int:id>', admin_views.appoinment_approve, name='appoinment_approved'),
    path('appoinmentreject/<int:id>', admin_views.appoinment_reject, name='appoinment_rejected'),

    path('nursedash', nurse_views.nurse_dash, name='nursedashboard'),
    path(' nursecomplaints', nurse_views. nursecomplaints, name='nurse_complaints_add'),
    path('nursecomplaintsview', nurse_views.nursecomplaintsview, name='nursecomplaints_view'),
    path('nursecomplaintsedit/<int:id>', nurse_views.nursecomplaintsedit, name='nursecomplaints_edit'),
    path('nursecomplaintsdel/<int:id>', nurse_views.nursecomplaintsdel, name='nursecomplaints_del'),
    path('scheduleadd', nurse_views.scheduleadd, name='schedule_add'),
    path('scheduleview', nurse_views.scheduleview, name='schedule_view'),
    path('scheduleedit/<int:id>', nurse_views.scheduleedit, name='schedule_edit'),
    path('scheduledel/<int:id>', nurse_views.scheduledel, name='schedule_del'),

    path('userdash', user_views.user_dash, name='userdashboard'),
    path('usercomplaints',user_views.usercomplaints,name='usercomplaints_add'),
    path('usercomplaintview',user_views.usercomplaintsview, name='usercomplaint_view'),
    path('usercomplaintsedit/<int:id>', user_views.usercomplaintsedit, name='usercomplaint_edit'),
    path('usercomplaintsdelete/<int:id>', user_views.usercomplaintsdel, name='usercomplaint_del'),
    path('userschedule/view', user_views.userschedule_view, name='user_schedule_view'),
    path('bookappoinment/<int:id>', user_views.bookappoinment, name='book_appoinment'),
    # path('userschedule/view', user_views.userschedule_view, name='userschedule_view'),
    path('userschedule/view', user_views.userschedule_view, name='user_schedule_view'),
    path('userappoinmentview/view', user_views.userappoinment_view, name='userappoinment_vie'),

]