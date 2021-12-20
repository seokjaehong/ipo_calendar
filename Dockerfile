FROM play_ground_base
ADD . /srv

RUN cp /srv/deploy/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN python manage.py collectstatic --no-input
EXPOSE 8000
#CMD exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
CMD ["supervisord"]