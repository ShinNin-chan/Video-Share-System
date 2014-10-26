from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()
import se.views
import video.views
import friendpair.views


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", se.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/settings/$", se.views.SettingsView.as_view(), name="account_settings"),
    url(r"^account/", include("account.urls")),
#    url(r"^ratings/", include("agon_ratings.urls")),

    url(r"^upload/$",video.views.upload),
    url(r"^upload/success/$",video.views.uploadSuccess),
    
    url(r"^videoplay/(\d+)$",video.views.video_play),
 
        
    url(r"^homepage$",se.views.personalPage),
    url(r"^personalPage/(\d+)$",se.views.personalPage, name="personalPage"),
    
    url(r"^timeline$",se.views.timeline,name="timeLine"),
    url(r"^timeline/all$",se.views.timelineall,name="timeLine"),
    
    url(r"friend-manage",friendpair.views.friendManage, name="friend-manage")
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

