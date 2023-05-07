To run code:
python manage.py runserver

After adding new images to static folder to store in staticFiles folder for Heroku
python manage.py collectstatic --noinput

When adding images adjust to the following
width: 5.56
height: 5.56
resolution 150 pixel/image **use 100 or 125 pixels/image 如果可以不损坏图片清晰度