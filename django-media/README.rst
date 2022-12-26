=================
django-media
=================

MEDIA is a simple Django app to conduct Web-based MEDIA.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "media" to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (
          ...
          'media',
      )

2. Include the media URLconf in your project urls.py like this:

      url(r'^media/', include('media.urls')),

3. Run `python manage.py makemigrations` to create the media models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
  to create items (you'll need the Admin app enabled).


