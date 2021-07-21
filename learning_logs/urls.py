# Defines URL patterns for learaning_logs.

from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),

    # Page that show all topic
    path("topics/", views.topics, name="topics"),

    # Detail page of single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),

    # page for adding new topics
    path("new_topic/", views.new_topic, name="new_topic"),

    # Page for adding new Entries
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),

    # Page for editing an entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),

    # Path to delete a topic
    path("delete/<int:topic_id>/", views.delete_topic, name="delete_topic"),
]
