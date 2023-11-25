from django.urls import path

from brit_test.app.views import (
    ItemsView,
    summary,
    add_to_summary
)

app_name = "app"
urlpatterns = [
     path("", view=ItemsView.as_view(), name="items"),
     path("summary/", view=summary, name="summary"),
     path("add/", view=add_to_summary, name="add"),
]



