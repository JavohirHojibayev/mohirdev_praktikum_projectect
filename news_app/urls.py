from django.urls import path
from .views import HomePageView, news_list, news_detail,ContactPageView, HomePageView, \
    LocalNewsPageView, ForignNewsPageView, TechnologyNewsPageView, SportNewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),  # Homepage URL
    path('news/', news_list, name='all_news_list'),  # URL for all news
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),  # URL for contact page
    path('local/', LocalNewsPageView.as_view(), name='local_news_page'),
    path('forign/', ForignNewsPageView.as_view(), name='forign_news_page'),  # Fixed syntax
    path('technology/', TechnologyNewsPageView.as_view(), name='technology_news_page'),  # Fixed syntax
    path('sport/', SportNewsPageView.as_view(), name='sport_news_page')
]