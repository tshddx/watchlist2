#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# ./manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1.save()

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2.save()

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3.save()

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4.save()

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = u'change_group'
    auth_permission_5.save()

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = u'delete_group'
    auth_permission_6.save()

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add message'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_7.codename = u'add_message'
    auth_permission_7.save()

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change message'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_8.codename = u'change_message'
    auth_permission_8.save()

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete message'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="message")
    auth_permission_9.codename = u'delete_message'
    auth_permission_9.save()

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add permission'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_10.codename = u'add_permission'
    auth_permission_10.save()

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change permission'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_11.codename = u'change_permission'
    auth_permission_11.save()

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete permission'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_12.codename = u'delete_permission'
    auth_permission_12.save()

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add user'
    auth_permission_13.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_13.codename = u'add_user'
    auth_permission_13.save()

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change user'
    auth_permission_14.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_14.codename = u'change_user'
    auth_permission_14.save()

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete user'
    auth_permission_15.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_15.codename = u'delete_user'
    auth_permission_15.save()

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add content type'
    auth_permission_16.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_16.codename = u'add_contenttype'
    auth_permission_16.save()

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change content type'
    auth_permission_17.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_17.codename = u'change_contenttype'
    auth_permission_17.save()

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete content type'
    auth_permission_18.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_18.codename = u'delete_contenttype'
    auth_permission_18.save()

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add session'
    auth_permission_19.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_19.codename = u'add_session'
    auth_permission_19.save()

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change session'
    auth_permission_20.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_20.codename = u'change_session'
    auth_permission_20.save()

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete session'
    auth_permission_21.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_21.codename = u'delete_session'
    auth_permission_21.save()

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add site'
    auth_permission_22.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_22.codename = u'add_site'
    auth_permission_22.save()

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change site'
    auth_permission_23.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_23.codename = u'change_site'
    auth_permission_23.save()

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete site'
    auth_permission_24.content_type = ContentType.objects.get(app_label="sites", model="site")
    auth_permission_24.codename = u'delete_site'
    auth_permission_24.save()

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add migration history'
    auth_permission_25.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_25.codename = u'add_migrationhistory'
    auth_permission_25.save()

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change migration history'
    auth_permission_26.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_26.codename = u'change_migrationhistory'
    auth_permission_26.save()

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete migration history'
    auth_permission_27.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_27.codename = u'delete_migrationhistory'
    auth_permission_27.save()

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add movie'
    auth_permission_28.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    auth_permission_28.codename = u'add_movie'
    auth_permission_28.save()

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change movie'
    auth_permission_29.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    auth_permission_29.codename = u'change_movie'
    auth_permission_29.save()

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete movie'
    auth_permission_30.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    auth_permission_30.codename = u'delete_movie'
    auth_permission_30.save()

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add person'
    auth_permission_31.content_type = ContentType.objects.get(app_label="watchlist", model="person")
    auth_permission_31.codename = u'add_person'
    auth_permission_31.save()

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change person'
    auth_permission_32.content_type = ContentType.objects.get(app_label="watchlist", model="person")
    auth_permission_32.codename = u'change_person'
    auth_permission_32.save()

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete person'
    auth_permission_33.content_type = ContentType.objects.get(app_label="watchlist", model="person")
    auth_permission_33.codename = u'delete_person'
    auth_permission_33.save()

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add viewing'
    auth_permission_34.content_type = ContentType.objects.get(app_label="watchlist", model="viewing")
    auth_permission_34.codename = u'add_viewing'
    auth_permission_34.save()

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change viewing'
    auth_permission_35.content_type = ContentType.objects.get(app_label="watchlist", model="viewing")
    auth_permission_35.codename = u'change_viewing'
    auth_permission_35.save()

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete viewing'
    auth_permission_36.content_type = ContentType.objects.get(app_label="watchlist", model="viewing")
    auth_permission_36.codename = u'delete_viewing'
    auth_permission_36.save()

    from django.contrib.auth.models import Group


    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'wediddoit@gmail.com'
    auth_user_1.password = u'sha1$ec59d$52652e1386992600d5a0c1c5c7f1c621aaa269af'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2010, 12, 21, 0, 2, 27, 872077)
    auth_user_1.date_joined = datetime.datetime(2010, 12, 20, 23, 51, 59, 210684)
    auth_user_1.save()

    from django.contrib.auth.models import Message


    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'12f977111e0b7d3164adb2a8ab3107ee'
    django_session_1.session_data = u'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwF1LmU3ODFjMTM3MzUwYjljM2ViNTQ4\nYzExZWFlYmUwYzE0\n'
    django_session_1.expire_date = datetime.datetime(2011, 1, 4, 0, 2, 27, 917865)
    django_session_1.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'example.com'
    django_site_1.name = u'example.com'
    django_site_1.save()

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2010, 12, 24, 1, 9, 12, 691882)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_1.object_id = u'12'
    django_admin_log_1.object_repr = u'Who Framed Roger Rabbit (1988)'
    django_admin_log_1.action_flag = 3
    django_admin_log_1.change_message = u''
    django_admin_log_1.save()

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2010, 12, 24, 0, 9, 8, 930541)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_2.object_id = u'11'
    django_admin_log_2.object_repr = u'Funny People (2009)'
    django_admin_log_2.action_flag = 3
    django_admin_log_2.change_message = u''
    django_admin_log_2.save()

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2010, 12, 23, 23, 59, 52, 480567)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_3.object_id = u'11'
    django_admin_log_3.object_repr = u' (None)'
    django_admin_log_3.action_flag = 3
    django_admin_log_3.change_message = u''
    django_admin_log_3.save()

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2010, 12, 23, 22, 12, 56, 249811)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_4.object_id = u'5'
    django_admin_log_4.object_repr = u' (None)'
    django_admin_log_4.action_flag = 3
    django_admin_log_4.change_message = u''
    django_admin_log_4.save()

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2010, 12, 23, 17, 21, 51, 948151)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="watchlist", model="person")
    django_admin_log_5.object_id = u'1'
    django_admin_log_5.object_repr = u'Brad Pitt'
    django_admin_log_5.action_flag = 3
    django_admin_log_5.change_message = u''
    django_admin_log_5.save()

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2010, 12, 21, 4, 43, 1, 663869)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_6.object_id = u'2'
    django_admin_log_6.object_repr = u'Fight Club (None)'
    django_admin_log_6.action_flag = 1
    django_admin_log_6.change_message = u''
    django_admin_log_6.save()

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2010, 12, 21, 0, 12, 12, 212569)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="watchlist", model="viewing")
    django_admin_log_7.object_id = u'1'
    django_admin_log_7.object_repr = u'"Silly Film" on Dec 13, 2010'
    django_admin_log_7.action_flag = 1
    django_admin_log_7.change_message = u''
    django_admin_log_7.save()

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2010, 12, 21, 0, 10, 5, 732652)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_8.object_id = u'1'
    django_admin_log_8.object_repr = u'Silly Film (2010)'
    django_admin_log_8.action_flag = 2
    django_admin_log_8.change_message = u'Changed release_date.'
    django_admin_log_8.save()

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2010, 12, 21, 0, 9, 44, 669753)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="watchlist", model="movie")
    django_admin_log_9.object_id = u'1'
    django_admin_log_9.object_repr = u'Silly Film (None)'
    django_admin_log_9.action_flag = 1
    django_admin_log_9.change_message = u''
    django_admin_log_9.save()

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2010, 12, 21, 0, 8, 16, 906183)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="watchlist", model="person")
    django_admin_log_10.object_id = u'1'
    django_admin_log_10.object_repr = u'Not One Director'
    django_admin_log_10.action_flag = 1
    django_admin_log_10.change_message = u''
    django_admin_log_10.save()

    from south.models import MigrationHistory

    south_migrationhistory_1 = MigrationHistory()
    south_migrationhistory_1.app_name = u'watchlist'
    south_migrationhistory_1.migration = u'0001_initial'
    south_migrationhistory_1.applied = datetime.datetime(2010, 12, 21, 6, 11, 45, 975765)
    south_migrationhistory_1.save()

    from watchlist2.watchlist.models import Person

    watchlist_person_1 = Person()
    watchlist_person_1.name = u'Wes Anderson'
    watchlist_person_1.tmdb_id = u'5655'
    watchlist_person_1.save()

    watchlist_person_2 = Person()
    watchlist_person_2.name = u'Woody Allen'
    watchlist_person_2.tmdb_id = u'1243'
    watchlist_person_2.save()

    watchlist_person_3 = Person()
    watchlist_person_3.name = u'Alexander Mackendrick'
    watchlist_person_3.tmdb_id = u'14566'
    watchlist_person_3.save()

    watchlist_person_4 = Person()
    watchlist_person_4.name = u'Jim Jarmusch'
    watchlist_person_4.tmdb_id = u'4429'
    watchlist_person_4.save()

    watchlist_person_5 = Person()
    watchlist_person_5.name = u'David Mamet'
    watchlist_person_5.tmdb_id = u'1255'
    watchlist_person_5.save()

    watchlist_person_6 = Person()
    watchlist_person_6.name = u'Sidney Lumet'
    watchlist_person_6.tmdb_id = u'39996'
    watchlist_person_6.save()

    watchlist_person_7 = Person()
    watchlist_person_7.name = u'Courtney Hunt'
    watchlist_person_7.tmdb_id = u'64131'
    watchlist_person_7.save()

    watchlist_person_8 = Person()
    watchlist_person_8.name = u'Aki Kaurism\xe4ki'
    watchlist_person_8.tmdb_id = u'16767'
    watchlist_person_8.save()

    watchlist_person_9 = Person()
    watchlist_person_9.name = u'Duncan Jones'
    watchlist_person_9.tmdb_id = u'81850'
    watchlist_person_9.save()

    watchlist_person_10 = Person()
    watchlist_person_10.name = u'Robert Bresson'
    watchlist_person_10.tmdb_id = u'10346'
    watchlist_person_10.save()

    watchlist_person_11 = Person()
    watchlist_person_11.name = u'John August'
    watchlist_person_11.tmdb_id = u'1300'
    watchlist_person_11.save()

    watchlist_person_12 = Person()
    watchlist_person_12.name = u'Todd Phillips'
    watchlist_person_12.tmdb_id = u'57130'
    watchlist_person_12.save()

    watchlist_person_13 = Person()
    watchlist_person_13.name = u'Ingmar Bergman'
    watchlist_person_13.tmdb_id = u'6648'
    watchlist_person_13.save()

    watchlist_person_14 = Person()
    watchlist_person_14.name = u'Chris Kentis'
    watchlist_person_14.tmdb_id = u'640'
    watchlist_person_14.save()

    watchlist_person_15 = Person()
    watchlist_person_15.name = u'Louis Malle'
    watchlist_person_15.tmdb_id = u'15389'
    watchlist_person_15.save()

    watchlist_person_16 = Person()
    watchlist_person_16.name = u'Yasujir\xf4 Ozu'
    watchlist_person_16.tmdb_id = u'95501'
    watchlist_person_16.save()

    watchlist_person_17 = Person()
    watchlist_person_17.name = u'Steven Spielberg'
    watchlist_person_17.tmdb_id = u'488'
    watchlist_person_17.save()

    watchlist_person_18 = Person()
    watchlist_person_18.name = u'Errol Morris'
    watchlist_person_18.tmdb_id = u'18533'
    watchlist_person_18.save()

    watchlist_person_19 = Person()
    watchlist_person_19.name = u'Steven Soderbergh'
    watchlist_person_19.tmdb_id = u'1884'
    watchlist_person_19.save()

    watchlist_person_20 = Person()
    watchlist_person_20.name = u'Ben Stiller'
    watchlist_person_20.tmdb_id = u'7399'
    watchlist_person_20.save()

    watchlist_person_21 = Person()
    watchlist_person_21.name = u'John Hamburg'
    watchlist_person_21.tmdb_id = u'17871'
    watchlist_person_21.save()

    watchlist_person_22 = Person()
    watchlist_person_22.name = u'Mike Leigh'
    watchlist_person_22.tmdb_id = u'65452'
    watchlist_person_22.save()

    watchlist_person_23 = Person()
    watchlist_person_23.name = u'Rian Johnson'
    watchlist_person_23.tmdb_id = u'67367'
    watchlist_person_23.save()

    watchlist_person_24 = Person()
    watchlist_person_24.name = u'Noah Baumbach'
    watchlist_person_24.tmdb_id = u'5656'
    watchlist_person_24.save()

    watchlist_person_25 = Person()
    watchlist_person_25.name = u'Peter Weir'
    watchlist_person_25.tmdb_id = u'2690'
    watchlist_person_25.save()

    watchlist_person_26 = Person()
    watchlist_person_26.name = u'Jonathan Demme'
    watchlist_person_26.tmdb_id = u'16294'
    watchlist_person_26.save()

    watchlist_person_27 = Person()
    watchlist_person_27.name = u'Neill Blomkamp'
    watchlist_person_27.tmdb_id = u'82194'
    watchlist_person_27.save()

    watchlist_person_28 = Person()
    watchlist_person_28.name = u'Mark Neveldine'
    watchlist_person_28.tmdb_id = u'20193'
    watchlist_person_28.save()

    watchlist_person_29 = Person()
    watchlist_person_29.name = u'Ron Howard'
    watchlist_person_29.tmdb_id = u'6159'
    watchlist_person_29.save()

    watchlist_person_30 = Person()
    watchlist_person_30.name = u'Kathryn Bigelow'
    watchlist_person_30.tmdb_id = u'14392'
    watchlist_person_30.save()

    watchlist_person_31 = Person()
    watchlist_person_31.name = u'Paul Greengrass'
    watchlist_person_31.tmdb_id = u'25598'
    watchlist_person_31.save()

    watchlist_person_32 = Person()
    watchlist_person_32.name = u'Chris Columbus'
    watchlist_person_32.tmdb_id = u'10965'
    watchlist_person_32.save()

    watchlist_person_33 = Person()
    watchlist_person_33.name = u'Alfonso Cuar\xf3n'
    watchlist_person_33.tmdb_id = u'11218'
    watchlist_person_33.save()

    watchlist_person_34 = Person()
    watchlist_person_34.name = u'Mike Newell'
    watchlist_person_34.tmdb_id = u'10723'
    watchlist_person_34.save()

    watchlist_person_35 = Person()
    watchlist_person_35.name = u'David Yates'
    watchlist_person_35.tmdb_id = u'11343'
    watchlist_person_35.save()

    watchlist_person_36 = Person()
    watchlist_person_36.name = u'Sam Raimi'
    watchlist_person_36.tmdb_id = u'7623'
    watchlist_person_36.save()

    watchlist_person_37 = Person()
    watchlist_person_37.name = u'Judd Apatow'
    watchlist_person_37.tmdb_id = u'41039'
    watchlist_person_37.save()

    watchlist_person_38 = Person()
    watchlist_person_38.name = u'Marc Webb'
    watchlist_person_38.tmdb_id = u'87742'
    watchlist_person_38.save()

    watchlist_person_39 = Person()
    watchlist_person_39.name = u'Mike Judge'
    watchlist_person_39.tmdb_id = u'17403'
    watchlist_person_39.save()

    watchlist_person_40 = Person()
    watchlist_person_40.name = u'Luc Besson'
    watchlist_person_40.tmdb_id = u'59'
    watchlist_person_40.save()

    watchlist_person_41 = Person()
    watchlist_person_41.name = u'Quentin Tarantino'
    watchlist_person_41.tmdb_id = u'138'
    watchlist_person_41.save()

    watchlist_person_42 = Person()
    watchlist_person_42.name = u'Kevin Macdonald'
    watchlist_person_42.tmdb_id = u'17350'
    watchlist_person_42.save()

    watchlist_person_43 = Person()
    watchlist_person_43.name = u'Jason Reitman'
    watchlist_person_43.tmdb_id = u'52443'
    watchlist_person_43.save()

    watchlist_person_44 = Person()
    watchlist_person_44.name = u'Armando Iannucci'
    watchlist_person_44.tmdb_id = u'88926'
    watchlist_person_44.save()

    watchlist_person_45 = Person()
    watchlist_person_45.name = u'Roland Emmerich'
    watchlist_person_45.tmdb_id = u'6046'
    watchlist_person_45.save()

    watchlist_person_46 = Person()
    watchlist_person_46.name = u'Bobcat Goldthwait'
    watchlist_person_46.tmdb_id = u'95024'
    watchlist_person_46.save()

    watchlist_person_47 = Person()
    watchlist_person_47.name = u'Boaz Yakin'
    watchlist_person_47.tmdb_id = u'52358'
    watchlist_person_47.save()

    watchlist_person_48 = Person()
    watchlist_person_48.name = u'Guy Ritchie'
    watchlist_person_48.tmdb_id = u'956'
    watchlist_person_48.save()

    watchlist_person_49 = Person()
    watchlist_person_49.name = u'Robert Kenner'
    watchlist_person_49.tmdb_id = u'95687'
    watchlist_person_49.save()

    watchlist_person_50 = Person()
    watchlist_person_50.name = u'James McTeigue'
    watchlist_person_50.tmdb_id = u'11266'
    watchlist_person_50.save()

    watchlist_person_51 = Person()
    watchlist_person_51.name = u'Vincenzo Natali'
    watchlist_person_51.tmdb_id = u'5877'
    watchlist_person_51.save()

    watchlist_person_52 = Person()
    watchlist_person_52.name = u'Luke Greenfield'
    watchlist_person_52.tmdb_id = u'65734'
    watchlist_person_52.save()

    watchlist_person_53 = Person()
    watchlist_person_53.name = u'Clark Gregg'
    watchlist_person_53.tmdb_id = u'9048'
    watchlist_person_53.save()

    watchlist_person_54 = Person()
    watchlist_person_54.name = u'Matthew Vaughn'
    watchlist_person_54.tmdb_id = u'957'
    watchlist_person_54.save()

    watchlist_person_55 = Person()
    watchlist_person_55.name = u'Louis Leterrier'
    watchlist_person_55.tmdb_id = u'18865'
    watchlist_person_55.save()

    watchlist_person_56 = Person()
    watchlist_person_56.name = u'Karyn Kusama'
    watchlist_person_56.tmdb_id = u'54025'
    watchlist_person_56.save()

    watchlist_person_57 = Person()
    watchlist_person_57.name = u'Steve Shill'
    watchlist_person_57.tmdb_id = u'80747'
    watchlist_person_57.save()

    watchlist_person_58 = Person()
    watchlist_person_58.name = u'Roman Polanski'
    watchlist_person_58.tmdb_id = u'3556'
    watchlist_person_58.save()

    watchlist_person_59 = Person()
    watchlist_person_59.name = u'Ridley Scott'
    watchlist_person_59.tmdb_id = u'578'
    watchlist_person_59.save()

    watchlist_person_60 = Person()
    watchlist_person_60.name = u'Sydney Pollack'
    watchlist_person_60.tmdb_id = u'2226'
    watchlist_person_60.save()

    watchlist_person_61 = Person()
    watchlist_person_61.name = u'Richard Donner'
    watchlist_person_61.tmdb_id = u'7187'
    watchlist_person_61.save()

    watchlist_person_62 = Person()
    watchlist_person_62.name = u'Dean DeBlois'
    watchlist_person_62.tmdb_id = u'69797'
    watchlist_person_62.save()

    watchlist_person_63 = Person()
    watchlist_person_63.name = u'Debra Granik'
    watchlist_person_63.tmdb_id = u'121873'
    watchlist_person_63.save()

    watchlist_person_64 = Person()
    watchlist_person_64.name = u'David Fincher'
    watchlist_person_64.tmdb_id = u'7467'
    watchlist_person_64.save()

    watchlist_person_65 = Person()
    watchlist_person_65.name = u'Henry Joost'
    watchlist_person_65.tmdb_id = u'142272'
    watchlist_person_65.save()

    watchlist_person_66 = Person()
    watchlist_person_66.name = u'Banksy'
    watchlist_person_66.tmdb_id = u'131617'
    watchlist_person_66.save()

    watchlist_person_67 = Person()
    watchlist_person_67.name = u'Edgar Wright'
    watchlist_person_67.tmdb_id = u'11090'
    watchlist_person_67.save()

    watchlist_person_68 = Person()
    watchlist_person_68.name = u'Martin Brest'
    watchlist_person_68.tmdb_id = u'769'
    watchlist_person_68.save()

    watchlist_person_69 = Person()
    watchlist_person_69.name = u'Christopher Nolan'
    watchlist_person_69.tmdb_id = u'525'
    watchlist_person_69.save()

    from watchlist2.watchlist.models import Movie

    watchlist_movie_1 = Movie()
    watchlist_movie_1.title = u'Rushmore'
    watchlist_movie_1.release_date = datetime.date(1998, 9, 17)
    watchlist_movie_1.runtime = 93
    watchlist_movie_1.director = watchlist_person_1
    watchlist_movie_1.nationality = u'USA'
    watchlist_movie_1.comments = None
    watchlist_movie_1.tmdb_id = u'11545'
    watchlist_movie_1.save()

    watchlist_movie_2 = Movie()
    watchlist_movie_2.title = u'Bottle Rocket'
    watchlist_movie_2.release_date = datetime.date(1996, 2, 21)
    watchlist_movie_2.runtime = 91
    watchlist_movie_2.director = watchlist_person_1
    watchlist_movie_2.nationality = u'USA'
    watchlist_movie_2.comments = None
    watchlist_movie_2.tmdb_id = u'13685'
    watchlist_movie_2.save()

    watchlist_movie_3 = Movie()
    watchlist_movie_3.title = u'Crimes and Misdemeanors'
    watchlist_movie_3.release_date = datetime.date(1989, 10, 13)
    watchlist_movie_3.runtime = 107
    watchlist_movie_3.director = watchlist_person_2
    watchlist_movie_3.nationality = u'USA'
    watchlist_movie_3.comments = None
    watchlist_movie_3.tmdb_id = u'11562'
    watchlist_movie_3.save()

    watchlist_movie_4 = Movie()
    watchlist_movie_4.title = u'Sweet Smell of Success'
    watchlist_movie_4.release_date = datetime.date(1957, 6, 27)
    watchlist_movie_4.runtime = 96
    watchlist_movie_4.director = watchlist_person_3
    watchlist_movie_4.nationality = u'USA'
    watchlist_movie_4.comments = None
    watchlist_movie_4.tmdb_id = u'976'
    watchlist_movie_4.save()

    watchlist_movie_5 = Movie()
    watchlist_movie_5.title = u"Cassandra's Dream"
    watchlist_movie_5.release_date = datetime.date(2007, 6, 18)
    watchlist_movie_5.runtime = 108
    watchlist_movie_5.director = watchlist_person_2
    watchlist_movie_5.nationality = u'USA'
    watchlist_movie_5.comments = None
    watchlist_movie_5.tmdb_id = u'4787'
    watchlist_movie_5.save()

    watchlist_movie_6 = Movie()
    watchlist_movie_6.title = u'Deconstructing Harry'
    watchlist_movie_6.release_date = datetime.date(1997, 8, 26)
    watchlist_movie_6.runtime = 96
    watchlist_movie_6.director = watchlist_person_2
    watchlist_movie_6.nationality = u'USA'
    watchlist_movie_6.comments = None
    watchlist_movie_6.tmdb_id = u'2639'
    watchlist_movie_6.save()

    watchlist_movie_7 = Movie()
    watchlist_movie_7.title = u'Stranger Than Paradise'
    watchlist_movie_7.release_date = datetime.date(1984, 1, 1)
    watchlist_movie_7.runtime = 89
    watchlist_movie_7.director = watchlist_person_4
    watchlist_movie_7.nationality = u'USA'
    watchlist_movie_7.comments = None
    watchlist_movie_7.tmdb_id = u'469'
    watchlist_movie_7.save()

    watchlist_movie_8 = Movie()
    watchlist_movie_8.title = u'The Royal Tenenbaums'
    watchlist_movie_8.release_date = datetime.date(2001, 10, 5)
    watchlist_movie_8.runtime = 110
    watchlist_movie_8.director = watchlist_person_1
    watchlist_movie_8.nationality = u'USA'
    watchlist_movie_8.comments = None
    watchlist_movie_8.tmdb_id = u'9428'
    watchlist_movie_8.save()

    watchlist_movie_9 = Movie()
    watchlist_movie_9.title = u'House of Games'
    watchlist_movie_9.release_date = datetime.date(1987, 10, 11)
    watchlist_movie_9.runtime = 102
    watchlist_movie_9.director = watchlist_person_5
    watchlist_movie_9.nationality = u'USA'
    watchlist_movie_9.comments = None
    watchlist_movie_9.tmdb_id = u'26719'
    watchlist_movie_9.save()

    watchlist_movie_10 = Movie()
    watchlist_movie_10.title = u'The Spanish Prisoner'
    watchlist_movie_10.release_date = datetime.date(1998, 4, 3)
    watchlist_movie_10.runtime = 110
    watchlist_movie_10.director = watchlist_person_5
    watchlist_movie_10.nationality = u'USA'
    watchlist_movie_10.comments = None
    watchlist_movie_10.tmdb_id = u'29193'
    watchlist_movie_10.save()

    watchlist_movie_11 = Movie()
    watchlist_movie_11.title = u"Before the Devil Knows You're Dead"
    watchlist_movie_11.release_date = datetime.date(2007, 9, 6)
    watchlist_movie_11.runtime = 117
    watchlist_movie_11.director = watchlist_person_6
    watchlist_movie_11.nationality = u'USA'
    watchlist_movie_11.comments = None
    watchlist_movie_11.tmdb_id = u'7972'
    watchlist_movie_11.save()

    watchlist_movie_12 = Movie()
    watchlist_movie_12.title = u'Interiors'
    watchlist_movie_12.release_date = datetime.date(1978, 8, 2)
    watchlist_movie_12.runtime = 0
    watchlist_movie_12.director = None
    watchlist_movie_12.nationality = u'USA'
    watchlist_movie_12.comments = None
    watchlist_movie_12.tmdb_id = u'15867'
    watchlist_movie_12.save()

    watchlist_movie_13 = Movie()
    watchlist_movie_13.title = u'Frozen River'
    watchlist_movie_13.release_date = datetime.date(2008, 8, 1)
    watchlist_movie_13.runtime = 97
    watchlist_movie_13.director = watchlist_person_7
    watchlist_movie_13.nationality = u'USA'
    watchlist_movie_13.comments = None
    watchlist_movie_13.tmdb_id = u'10183'
    watchlist_movie_13.save()

    watchlist_movie_14 = Movie()
    watchlist_movie_14.title = u'Annie Hall'
    watchlist_movie_14.release_date = datetime.date(1977, 4, 20)
    watchlist_movie_14.runtime = 93
    watchlist_movie_14.director = watchlist_person_2
    watchlist_movie_14.nationality = u'USA'
    watchlist_movie_14.comments = None
    watchlist_movie_14.tmdb_id = u'703'
    watchlist_movie_14.save()

    watchlist_movie_15 = Movie()
    watchlist_movie_15.title = u"L'argent"
    watchlist_movie_15.release_date = datetime.date(1983, 1, 1)
    watchlist_movie_15.runtime = 85
    watchlist_movie_15.director = None
    watchlist_movie_15.nationality = u'France'
    watchlist_movie_15.comments = None
    watchlist_movie_15.tmdb_id = u'42112'
    watchlist_movie_15.save()

    watchlist_movie_16 = Movie()
    watchlist_movie_16.title = u'Shadows in Paradise'
    watchlist_movie_16.release_date = datetime.date(1986, 10, 17)
    watchlist_movie_16.runtime = 76
    watchlist_movie_16.director = watchlist_person_8
    watchlist_movie_16.nationality = u'Finland'
    watchlist_movie_16.comments = None
    watchlist_movie_16.tmdb_id = u'3'
    watchlist_movie_16.save()

    watchlist_movie_17 = Movie()
    watchlist_movie_17.title = u'Moon'
    watchlist_movie_17.release_date = datetime.date(2009, 6, 12)
    watchlist_movie_17.runtime = 97
    watchlist_movie_17.director = watchlist_person_9
    watchlist_movie_17.nationality = u'USA'
    watchlist_movie_17.comments = None
    watchlist_movie_17.tmdb_id = u'17431'
    watchlist_movie_17.save()

    watchlist_movie_18 = Movie()
    watchlist_movie_18.title = u'Pickpocket'
    watchlist_movie_18.release_date = datetime.date(1959, 12, 1)
    watchlist_movie_18.runtime = 75
    watchlist_movie_18.director = watchlist_person_10
    watchlist_movie_18.nationality = u'France'
    watchlist_movie_18.comments = None
    watchlist_movie_18.tmdb_id = u'690'
    watchlist_movie_18.save()

    watchlist_movie_19 = Movie()
    watchlist_movie_19.title = u'Scoop'
    watchlist_movie_19.release_date = datetime.date(2006, 7, 28)
    watchlist_movie_19.runtime = 96
    watchlist_movie_19.director = watchlist_person_2
    watchlist_movie_19.nationality = u'USA'
    watchlist_movie_19.comments = None
    watchlist_movie_19.tmdb_id = u'512'
    watchlist_movie_19.save()

    watchlist_movie_20 = Movie()
    watchlist_movie_20.title = u'The Match Factory Girl'
    watchlist_movie_20.release_date = datetime.date(1990, 1, 12)
    watchlist_movie_20.runtime = 66
    watchlist_movie_20.director = watchlist_person_8
    watchlist_movie_20.nationality = u'Finland'
    watchlist_movie_20.comments = None
    watchlist_movie_20.tmdb_id = u'7974'
    watchlist_movie_20.save()

    watchlist_movie_21 = Movie()
    watchlist_movie_21.title = u'The Nines'
    watchlist_movie_21.release_date = datetime.date(2007, 11, 30)
    watchlist_movie_21.runtime = 100
    watchlist_movie_21.director = watchlist_person_11
    watchlist_movie_21.nationality = u'USA'
    watchlist_movie_21.comments = None
    watchlist_movie_21.tmdb_id = u'12994'
    watchlist_movie_21.save()

    watchlist_movie_22 = Movie()
    watchlist_movie_22.title = u'The Purple Rose of Cairo'
    watchlist_movie_22.release_date = datetime.date(1985, 3, 1)
    watchlist_movie_22.runtime = 82
    watchlist_movie_22.director = watchlist_person_2
    watchlist_movie_22.nationality = u'USA'
    watchlist_movie_22.comments = None
    watchlist_movie_22.tmdb_id = u'10849'
    watchlist_movie_22.save()

    watchlist_movie_23 = Movie()
    watchlist_movie_23.title = u'The Hangover'
    watchlist_movie_23.release_date = datetime.date(2009, 6, 5)
    watchlist_movie_23.runtime = 100
    watchlist_movie_23.director = watchlist_person_12
    watchlist_movie_23.nationality = u'USA'
    watchlist_movie_23.comments = None
    watchlist_movie_23.tmdb_id = u'18785'
    watchlist_movie_23.save()

    watchlist_movie_24 = Movie()
    watchlist_movie_24.title = u'Through a Glass Darkly'
    watchlist_movie_24.release_date = datetime.date(1961, 10, 16)
    watchlist_movie_24.runtime = 89
    watchlist_movie_24.director = watchlist_person_13
    watchlist_movie_24.nationality = u'Sweden'
    watchlist_movie_24.comments = None
    watchlist_movie_24.tmdb_id = u'11602'
    watchlist_movie_24.save()

    watchlist_movie_25 = Movie()
    watchlist_movie_25.title = u'Manhattan'
    watchlist_movie_25.release_date = datetime.date(1979, 3, 14)
    watchlist_movie_25.runtime = 96
    watchlist_movie_25.director = watchlist_person_2
    watchlist_movie_25.nationality = u'USA'
    watchlist_movie_25.comments = u"56:00 You're a coward. -Only in actuality"
    watchlist_movie_25.tmdb_id = u'696'
    watchlist_movie_25.save()

    watchlist_movie_26 = Movie()
    watchlist_movie_26.title = u'Mighty Aphrodite'
    watchlist_movie_26.release_date = datetime.date(1995, 9, 13)
    watchlist_movie_26.runtime = 95
    watchlist_movie_26.director = watchlist_person_2
    watchlist_movie_26.nationality = u'USA'
    watchlist_movie_26.comments = None
    watchlist_movie_26.tmdb_id = u'11448'
    watchlist_movie_26.save()

    watchlist_movie_27 = Movie()
    watchlist_movie_27.title = u'Laitakaupungin valot'
    watchlist_movie_27.release_date = datetime.date(2006, 2, 3)
    watchlist_movie_27.runtime = 78
    watchlist_movie_27.director = watchlist_person_8
    watchlist_movie_27.nationality = u'Finland'
    watchlist_movie_27.comments = None
    watchlist_movie_27.tmdb_id = u'1379'
    watchlist_movie_27.save()

    watchlist_movie_28 = Movie()
    watchlist_movie_28.title = u'Winter Light'
    watchlist_movie_28.release_date = datetime.date(1963, 1, 1)
    watchlist_movie_28.runtime = 81
    watchlist_movie_28.director = watchlist_person_13
    watchlist_movie_28.nationality = u'Sweden'
    watchlist_movie_28.comments = None
    watchlist_movie_28.tmdb_id = u'29455'
    watchlist_movie_28.save()

    watchlist_movie_29 = Movie()
    watchlist_movie_29.title = u'Open Water'
    watchlist_movie_29.release_date = datetime.date(2004, 8, 20)
    watchlist_movie_29.runtime = 79
    watchlist_movie_29.director = watchlist_person_14
    watchlist_movie_29.nationality = u'USA'
    watchlist_movie_29.comments = None
    watchlist_movie_29.tmdb_id = u'83'
    watchlist_movie_29.save()

    watchlist_movie_30 = Movie()
    watchlist_movie_30.title = u'Zelig'
    watchlist_movie_30.release_date = datetime.date(1983, 7, 15)
    watchlist_movie_30.runtime = 79
    watchlist_movie_30.director = watchlist_person_2
    watchlist_movie_30.nationality = u'USA'
    watchlist_movie_30.comments = None
    watchlist_movie_30.tmdb_id = u'11030'
    watchlist_movie_30.save()

    watchlist_movie_31 = Movie()
    watchlist_movie_31.title = u'Hannah And Her Sisters'
    watchlist_movie_31.release_date = datetime.date(1986, 2, 7)
    watchlist_movie_31.runtime = 103
    watchlist_movie_31.director = watchlist_person_2
    watchlist_movie_31.nationality = u'USA'
    watchlist_movie_31.comments = None
    watchlist_movie_31.tmdb_id = u'5143'
    watchlist_movie_31.save()

    watchlist_movie_32 = Movie()
    watchlist_movie_32.title = u'Bananas'
    watchlist_movie_32.release_date = datetime.date(1971, 4, 28)
    watchlist_movie_32.runtime = 82
    watchlist_movie_32.director = watchlist_person_2
    watchlist_movie_32.nationality = u'USA'
    watchlist_movie_32.comments = None
    watchlist_movie_32.tmdb_id = u'11302'
    watchlist_movie_32.save()

    watchlist_movie_33 = Movie()
    watchlist_movie_33.title = u'Melinda and Melinda'
    watchlist_movie_33.release_date = datetime.date(2004, 10, 29)
    watchlist_movie_33.runtime = 100
    watchlist_movie_33.director = watchlist_person_2
    watchlist_movie_33.nationality = u'USA'
    watchlist_movie_33.comments = None
    watchlist_movie_33.tmdb_id = u'9688'
    watchlist_movie_33.save()

    watchlist_movie_34 = Movie()
    watchlist_movie_34.title = u'My Dinner With Andre'
    watchlist_movie_34.release_date = datetime.date(1981, 10, 11)
    watchlist_movie_34.runtime = 110
    watchlist_movie_34.director = watchlist_person_15
    watchlist_movie_34.nationality = u'USA'
    watchlist_movie_34.comments = None
    watchlist_movie_34.tmdb_id = u'25468'
    watchlist_movie_34.save()

    watchlist_movie_35 = Movie()
    watchlist_movie_35.title = u'The End of Summer'
    watchlist_movie_35.release_date = datetime.date(1961, 10, 29)
    watchlist_movie_35.runtime = 103
    watchlist_movie_35.director = watchlist_person_16
    watchlist_movie_35.nationality = u'Japan'
    watchlist_movie_35.comments = None
    watchlist_movie_35.tmdb_id = u'28273'
    watchlist_movie_35.save()

    watchlist_movie_36 = Movie()
    watchlist_movie_36.title = u'A.I. Artificial Intelligence'
    watchlist_movie_36.release_date = datetime.date(2001, 6, 29)
    watchlist_movie_36.runtime = 145
    watchlist_movie_36.director = watchlist_person_17
    watchlist_movie_36.nationality = u'USA'
    watchlist_movie_36.comments = None
    watchlist_movie_36.tmdb_id = u'644'
    watchlist_movie_36.save()

    watchlist_movie_37 = Movie()
    watchlist_movie_37.title = u'The Fog of War: Eleven Lessons from the Life of Robert S. McNamara'
    watchlist_movie_37.release_date = datetime.date(2003, 5, 21)
    watchlist_movie_37.runtime = 95
    watchlist_movie_37.director = watchlist_person_18
    watchlist_movie_37.nationality = u'USA'
    watchlist_movie_37.comments = None
    watchlist_movie_37.tmdb_id = u'12698'
    watchlist_movie_37.save()

    watchlist_movie_38 = Movie()
    watchlist_movie_38.title = u'The Girlfriend Experience'
    watchlist_movie_38.release_date = datetime.date(2009, 1, 20)
    watchlist_movie_38.runtime = 77
    watchlist_movie_38.director = watchlist_person_19
    watchlist_movie_38.nationality = u'USA'
    watchlist_movie_38.comments = None
    watchlist_movie_38.tmdb_id = u'17680'
    watchlist_movie_38.save()

    watchlist_movie_39 = Movie()
    watchlist_movie_39.title = u'The Cable Guy'
    watchlist_movie_39.release_date = datetime.date(1996, 6, 10)
    watchlist_movie_39.runtime = 91
    watchlist_movie_39.director = watchlist_person_20
    watchlist_movie_39.nationality = u'USA'
    watchlist_movie_39.comments = None
    watchlist_movie_39.tmdb_id = u'9894'
    watchlist_movie_39.save()

    watchlist_movie_40 = Movie()
    watchlist_movie_40.title = u'I Love You, Man'
    watchlist_movie_40.release_date = datetime.date(2009, 3, 20)
    watchlist_movie_40.runtime = 105
    watchlist_movie_40.director = watchlist_person_21
    watchlist_movie_40.nationality = u'USA'
    watchlist_movie_40.comments = None
    watchlist_movie_40.tmdb_id = u'16538'
    watchlist_movie_40.save()

    watchlist_movie_41 = Movie()
    watchlist_movie_41.title = u'Husbands and Wives'
    watchlist_movie_41.release_date = datetime.date(1992, 1, 1)
    watchlist_movie_41.runtime = 108
    watchlist_movie_41.director = watchlist_person_2
    watchlist_movie_41.nationality = u'USA'
    watchlist_movie_41.comments = u'Shaky cam, jump cuts, zooms'
    watchlist_movie_41.tmdb_id = u'28384'
    watchlist_movie_41.save()

    watchlist_movie_42 = Movie()
    watchlist_movie_42.title = u'Naked'
    watchlist_movie_42.release_date = datetime.date(1993, 9, 14)
    watchlist_movie_42.runtime = 131
    watchlist_movie_42.director = watchlist_person_22
    watchlist_movie_42.nationality = u'UK'
    watchlist_movie_42.comments = None
    watchlist_movie_42.tmdb_id = u'21450'
    watchlist_movie_42.save()

    watchlist_movie_43 = Movie()
    watchlist_movie_43.title = u'The Brothers Bloom'
    watchlist_movie_43.release_date = datetime.date(2008, 9, 9)
    watchlist_movie_43.runtime = 113
    watchlist_movie_43.director = watchlist_person_23
    watchlist_movie_43.nationality = u'USA'
    watchlist_movie_43.comments = None
    watchlist_movie_43.tmdb_id = u'21755'
    watchlist_movie_43.save()

    watchlist_movie_44 = Movie()
    watchlist_movie_44.title = u'The Darjeeling Limited'
    watchlist_movie_44.release_date = datetime.date(2007, 9, 3)
    watchlist_movie_44.runtime = 91
    watchlist_movie_44.director = watchlist_person_1
    watchlist_movie_44.nationality = u'USA'
    watchlist_movie_44.comments = None
    watchlist_movie_44.tmdb_id = u'4538'
    watchlist_movie_44.save()

    watchlist_movie_45 = Movie()
    watchlist_movie_45.title = u'The Squid and the Whale'
    watchlist_movie_45.release_date = datetime.date(2005, 1, 23)
    watchlist_movie_45.runtime = 81
    watchlist_movie_45.director = watchlist_person_24
    watchlist_movie_45.nationality = u'USA'
    watchlist_movie_45.comments = None
    watchlist_movie_45.tmdb_id = u'10707'
    watchlist_movie_45.save()

    watchlist_movie_46 = Movie()
    watchlist_movie_46.title = u'The Seventh Seal'
    watchlist_movie_46.release_date = datetime.date(1957, 2, 16)
    watchlist_movie_46.runtime = 92
    watchlist_movie_46.director = watchlist_person_13
    watchlist_movie_46.nationality = u'Sweden'
    watchlist_movie_46.comments = None
    watchlist_movie_46.tmdb_id = u'490'
    watchlist_movie_46.save()

    watchlist_movie_47 = Movie()
    watchlist_movie_47.title = u'Celebrity'
    watchlist_movie_47.release_date = datetime.date(1998, 9, 7)
    watchlist_movie_47.runtime = 113
    watchlist_movie_47.director = watchlist_person_2
    watchlist_movie_47.nationality = u'USA'
    watchlist_movie_47.comments = u'Black and white'
    watchlist_movie_47.tmdb_id = u'9466'
    watchlist_movie_47.save()

    watchlist_movie_48 = Movie()
    watchlist_movie_48.title = u'Mouchette'
    watchlist_movie_48.release_date = datetime.date(1967, 1, 1)
    watchlist_movie_48.runtime = 81
    watchlist_movie_48.director = watchlist_person_10
    watchlist_movie_48.nationality = u'France'
    watchlist_movie_48.comments = None
    watchlist_movie_48.tmdb_id = u'1561'
    watchlist_movie_48.save()

    watchlist_movie_49 = Movie()
    watchlist_movie_49.title = u'Master And Commander: The Far Side Of The World'
    watchlist_movie_49.release_date = datetime.date(2003, 11, 14)
    watchlist_movie_49.runtime = 138
    watchlist_movie_49.director = watchlist_person_25
    watchlist_movie_49.nationality = u'USA'
    watchlist_movie_49.comments = None
    watchlist_movie_49.tmdb_id = u'8619'
    watchlist_movie_49.save()

    watchlist_movie_50 = Movie()
    watchlist_movie_50.title = u'Vicky Christina Barcelona'
    watchlist_movie_50.release_date = datetime.date(2008, 8, 15)
    watchlist_movie_50.runtime = 96
    watchlist_movie_50.director = watchlist_person_2
    watchlist_movie_50.nationality = u'USA'
    watchlist_movie_50.comments = None
    watchlist_movie_50.tmdb_id = u'49371'
    watchlist_movie_50.save()

    watchlist_movie_51 = Movie()
    watchlist_movie_51.title = u'Broadway Danny Rose'
    watchlist_movie_51.release_date = datetime.date(1984, 1, 27)
    watchlist_movie_51.runtime = 84
    watchlist_movie_51.director = watchlist_person_2
    watchlist_movie_51.nationality = u'USA'
    watchlist_movie_51.comments = u'Black and white'
    watchlist_movie_51.tmdb_id = u'12762'
    watchlist_movie_51.save()

    watchlist_movie_52 = Movie()
    watchlist_movie_52.title = u'Sleeper'
    watchlist_movie_52.release_date = datetime.date(1973, 12, 17)
    watchlist_movie_52.runtime = 89
    watchlist_movie_52.director = watchlist_person_2
    watchlist_movie_52.nationality = u'USA'
    watchlist_movie_52.comments = u'50:00 "My father was black and my mother was white, and vice versa."'
    watchlist_movie_52.tmdb_id = u'11561'
    watchlist_movie_52.save()

    watchlist_movie_53 = Movie()
    watchlist_movie_53.title = u'Autumn Sonata'
    watchlist_movie_53.release_date = datetime.date(1978, 10, 8)
    watchlist_movie_53.runtime = 99
    watchlist_movie_53.director = watchlist_person_13
    watchlist_movie_53.nationality = u'Sweden'
    watchlist_movie_53.comments = u"I don't like zooms, even subtle ones"
    watchlist_movie_53.tmdb_id = u'12761'
    watchlist_movie_53.save()

    watchlist_movie_54 = Movie()
    watchlist_movie_54.title = u'Rachel Getting Married'
    watchlist_movie_54.release_date = datetime.date(2008, 9, 3)
    watchlist_movie_54.runtime = 113
    watchlist_movie_54.director = watchlist_person_26
    watchlist_movie_54.nationality = u'USA'
    watchlist_movie_54.comments = None
    watchlist_movie_54.tmdb_id = u'14976'
    watchlist_movie_54.save()

    watchlist_movie_55 = Movie()
    watchlist_movie_55.title = u'District 9'
    watchlist_movie_55.release_date = datetime.date(2009, 8, 13)
    watchlist_movie_55.runtime = 112
    watchlist_movie_55.director = watchlist_person_27
    watchlist_movie_55.nationality = u'USA'
    watchlist_movie_55.comments = None
    watchlist_movie_55.tmdb_id = u'17654'
    watchlist_movie_55.save()

    watchlist_movie_56 = Movie()
    watchlist_movie_56.title = u'Sweet and Lowdown'
    watchlist_movie_56.release_date = datetime.date(1999, 12, 3)
    watchlist_movie_56.runtime = 95
    watchlist_movie_56.director = watchlist_person_2
    watchlist_movie_56.nationality = u'USA'
    watchlist_movie_56.comments = None
    watchlist_movie_56.tmdb_id = u'9684'
    watchlist_movie_56.save()

    watchlist_movie_57 = Movie()
    watchlist_movie_57.title = u'Close Encounters of the Third Kind'
    watchlist_movie_57.release_date = datetime.date(1977, 11, 15)
    watchlist_movie_57.runtime = 135
    watchlist_movie_57.director = watchlist_person_17
    watchlist_movie_57.nationality = u'USA'
    watchlist_movie_57.comments = None
    watchlist_movie_57.tmdb_id = u'840'
    watchlist_movie_57.save()

    watchlist_movie_58 = Movie()
    watchlist_movie_58.title = u'Crank: High Voltage'
    watchlist_movie_58.release_date = datetime.date(2009, 4, 17)
    watchlist_movie_58.runtime = 96
    watchlist_movie_58.director = watchlist_person_28
    watchlist_movie_58.nationality = u'USA'
    watchlist_movie_58.comments = None
    watchlist_movie_58.tmdb_id = u'15092'
    watchlist_movie_58.save()

    watchlist_movie_59 = Movie()
    watchlist_movie_59.title = u'Cinderella Man'
    watchlist_movie_59.release_date = datetime.date(2005, 5, 23)
    watchlist_movie_59.runtime = 144
    watchlist_movie_59.director = watchlist_person_29
    watchlist_movie_59.nationality = u'USA'
    watchlist_movie_59.comments = None
    watchlist_movie_59.tmdb_id = u'921'
    watchlist_movie_59.save()

    watchlist_movie_60 = Movie()
    watchlist_movie_60.title = u'Good Morning'
    watchlist_movie_60.release_date = datetime.date(1959, 5, 12)
    watchlist_movie_60.runtime = 94
    watchlist_movie_60.director = watchlist_person_16
    watchlist_movie_60.nationality = u'Japan'
    watchlist_movie_60.comments = None
    watchlist_movie_60.tmdb_id = u'28276'
    watchlist_movie_60.save()

    watchlist_movie_61 = Movie()
    watchlist_movie_61.title = u'Manhattan Murder Mystery'
    watchlist_movie_61.release_date = datetime.date(1993, 8, 18)
    watchlist_movie_61.runtime = 104
    watchlist_movie_61.director = watchlist_person_2
    watchlist_movie_61.nationality = u'USA'
    watchlist_movie_61.comments = None
    watchlist_movie_61.tmdb_id = u'10440'
    watchlist_movie_61.save()

    watchlist_movie_62 = Movie()
    watchlist_movie_62.title = u'Ju Dou'
    watchlist_movie_62.release_date = datetime.date(1990, 1, 1)
    watchlist_movie_62.runtime = 95
    watchlist_movie_62.director = None
    watchlist_movie_62.nationality = u'China'
    watchlist_movie_62.comments = None
    watchlist_movie_62.tmdb_id = u'41821'
    watchlist_movie_62.save()

    watchlist_movie_63 = Movie()
    watchlist_movie_63.title = u'The Hurt Locker'
    watchlist_movie_63.release_date = datetime.date(2008, 9, 4)
    watchlist_movie_63.runtime = 130
    watchlist_movie_63.director = watchlist_person_30
    watchlist_movie_63.nationality = u'USA'
    watchlist_movie_63.comments = None
    watchlist_movie_63.tmdb_id = u'12162'
    watchlist_movie_63.save()

    watchlist_movie_64 = Movie()
    watchlist_movie_64.title = u'United 93'
    watchlist_movie_64.release_date = datetime.date(2006, 4, 28)
    watchlist_movie_64.runtime = 111
    watchlist_movie_64.director = watchlist_person_31
    watchlist_movie_64.nationality = u'USA'
    watchlist_movie_64.comments = None
    watchlist_movie_64.tmdb_id = u'9829'
    watchlist_movie_64.save()

    watchlist_movie_65 = Movie()
    watchlist_movie_65.title = u'Whatever Works'
    watchlist_movie_65.release_date = datetime.date(2009, 6, 19)
    watchlist_movie_65.runtime = 92
    watchlist_movie_65.director = watchlist_person_2
    watchlist_movie_65.nationality = u'USA'
    watchlist_movie_65.comments = None
    watchlist_movie_65.tmdb_id = u'19265'
    watchlist_movie_65.save()

    watchlist_movie_66 = Movie()
    watchlist_movie_66.title = u"Harry Potter and the Sorcerer's Stone"
    watchlist_movie_66.release_date = datetime.date(2001, 11, 4)
    watchlist_movie_66.runtime = 152
    watchlist_movie_66.director = watchlist_person_32
    watchlist_movie_66.nationality = u'USA'
    watchlist_movie_66.comments = None
    watchlist_movie_66.tmdb_id = u'671'
    watchlist_movie_66.save()

    watchlist_movie_67 = Movie()
    watchlist_movie_67.title = u'Harry Potter and the Chamber Of Secrets'
    watchlist_movie_67.release_date = datetime.date(2002, 11, 3)
    watchlist_movie_67.runtime = 161
    watchlist_movie_67.director = watchlist_person_32
    watchlist_movie_67.nationality = u'USA'
    watchlist_movie_67.comments = None
    watchlist_movie_67.tmdb_id = u'672'
    watchlist_movie_67.save()

    watchlist_movie_68 = Movie()
    watchlist_movie_68.title = u'Harry Potter and the Prisoner Of Azkaban'
    watchlist_movie_68.release_date = datetime.date(2004, 5, 31)
    watchlist_movie_68.runtime = 141
    watchlist_movie_68.director = watchlist_person_33
    watchlist_movie_68.nationality = u'USA'
    watchlist_movie_68.comments = None
    watchlist_movie_68.tmdb_id = u'673'
    watchlist_movie_68.save()

    watchlist_movie_69 = Movie()
    watchlist_movie_69.title = u'Harry Potter and the Goblet Of Fire'
    watchlist_movie_69.release_date = datetime.date(2005, 11, 6)
    watchlist_movie_69.runtime = 157
    watchlist_movie_69.director = watchlist_person_34
    watchlist_movie_69.nationality = u'USA'
    watchlist_movie_69.comments = None
    watchlist_movie_69.tmdb_id = u'674'
    watchlist_movie_69.save()

    watchlist_movie_70 = Movie()
    watchlist_movie_70.title = u'Harry Potter and the Order of the Phoenix'
    watchlist_movie_70.release_date = datetime.date(2007, 7, 11)
    watchlist_movie_70.runtime = 130
    watchlist_movie_70.director = watchlist_person_35
    watchlist_movie_70.nationality = u'USA'
    watchlist_movie_70.comments = None
    watchlist_movie_70.tmdb_id = u'675'
    watchlist_movie_70.save()

    watchlist_movie_71 = Movie()
    watchlist_movie_71.title = u'Harry Potter and the Half-Blood Prince'
    watchlist_movie_71.release_date = datetime.date(2009, 7, 17)
    watchlist_movie_71.runtime = 153
    watchlist_movie_71.director = watchlist_person_35
    watchlist_movie_71.nationality = u'USA'
    watchlist_movie_71.comments = None
    watchlist_movie_71.tmdb_id = u'767'
    watchlist_movie_71.save()

    watchlist_movie_72 = Movie()
    watchlist_movie_72.title = u'Drag Me to Hell'
    watchlist_movie_72.release_date = datetime.date(2009, 5, 29)
    watchlist_movie_72.runtime = 139
    watchlist_movie_72.director = watchlist_person_36
    watchlist_movie_72.nationality = u'USA'
    watchlist_movie_72.comments = None
    watchlist_movie_72.tmdb_id = u'16871'
    watchlist_movie_72.save()

    watchlist_movie_73 = Movie()
    watchlist_movie_73.title = u'Funny People'
    watchlist_movie_73.release_date = datetime.date(2009, 7, 31)
    watchlist_movie_73.runtime = 146
    watchlist_movie_73.director = watchlist_person_37
    watchlist_movie_73.nationality = u'USA'
    watchlist_movie_73.comments = None
    watchlist_movie_73.tmdb_id = u'20829'
    watchlist_movie_73.save()

    watchlist_movie_74 = Movie()
    watchlist_movie_74.title = u'(500) Days of Summer'
    watchlist_movie_74.release_date = datetime.date(2009, 1, 12)
    watchlist_movie_74.runtime = 95
    watchlist_movie_74.director = watchlist_person_38
    watchlist_movie_74.nationality = u'USA'
    watchlist_movie_74.comments = None
    watchlist_movie_74.tmdb_id = u'19913'
    watchlist_movie_74.save()

    watchlist_movie_75 = Movie()
    watchlist_movie_75.title = u'Extract'
    watchlist_movie_75.release_date = datetime.date(2009, 9, 4)
    watchlist_movie_75.runtime = 92
    watchlist_movie_75.director = watchlist_person_39
    watchlist_movie_75.nationality = u'USA'
    watchlist_movie_75.comments = None
    watchlist_movie_75.tmdb_id = u'12569'
    watchlist_movie_75.save()

    watchlist_movie_76 = Movie()
    watchlist_movie_76.title = u'Leon: The Professional'
    watchlist_movie_76.release_date = datetime.date(1994, 11, 18)
    watchlist_movie_76.runtime = 110
    watchlist_movie_76.director = watchlist_person_40
    watchlist_movie_76.nationality = u'France'
    watchlist_movie_76.comments = None
    watchlist_movie_76.tmdb_id = u'101'
    watchlist_movie_76.save()

    watchlist_movie_77 = Movie()
    watchlist_movie_77.title = u'Inglourious Basterds'
    watchlist_movie_77.release_date = datetime.date(2009, 8, 21)
    watchlist_movie_77.runtime = 153
    watchlist_movie_77.director = watchlist_person_41
    watchlist_movie_77.nationality = u'USA'
    watchlist_movie_77.comments = None
    watchlist_movie_77.tmdb_id = u'16869'
    watchlist_movie_77.save()

    watchlist_movie_78 = Movie()
    watchlist_movie_78.title = u'State of Play'
    watchlist_movie_78.release_date = datetime.date(2009, 4, 17)
    watchlist_movie_78.runtime = 127
    watchlist_movie_78.director = watchlist_person_42
    watchlist_movie_78.nationality = u'USA'
    watchlist_movie_78.comments = None
    watchlist_movie_78.tmdb_id = u'16995'
    watchlist_movie_78.save()

    watchlist_movie_79 = Movie()
    watchlist_movie_79.title = u'Up in the Air'
    watchlist_movie_79.release_date = datetime.date(2009, 12, 4)
    watchlist_movie_79.runtime = 109
    watchlist_movie_79.director = watchlist_person_43
    watchlist_movie_79.nationality = u'USA'
    watchlist_movie_79.comments = None
    watchlist_movie_79.tmdb_id = u'22947'
    watchlist_movie_79.save()

    watchlist_movie_80 = Movie()
    watchlist_movie_80.title = u'In the Loop'
    watchlist_movie_80.release_date = datetime.date(2009, 1, 22)
    watchlist_movie_80.runtime = 106
    watchlist_movie_80.director = watchlist_person_44
    watchlist_movie_80.nationality = u'UK'
    watchlist_movie_80.comments = None
    watchlist_movie_80.tmdb_id = u'19833'
    watchlist_movie_80.save()

    watchlist_movie_81 = Movie()
    watchlist_movie_81.title = u'2012'
    watchlist_movie_81.release_date = datetime.date(2009, 11, 13)
    watchlist_movie_81.runtime = 158
    watchlist_movie_81.director = watchlist_person_45
    watchlist_movie_81.nationality = u'USA'
    watchlist_movie_81.comments = None
    watchlist_movie_81.tmdb_id = u'14161'
    watchlist_movie_81.save()

    watchlist_movie_82 = Movie()
    watchlist_movie_82.title = u"World's Greatest Dad"
    watchlist_movie_82.release_date = datetime.date(2009, 8, 21)
    watchlist_movie_82.runtime = 99
    watchlist_movie_82.director = watchlist_person_46
    watchlist_movie_82.nationality = u'USA'
    watchlist_movie_82.comments = None
    watchlist_movie_82.tmdb_id = u'20178'
    watchlist_movie_82.save()

    watchlist_movie_83 = Movie()
    watchlist_movie_83.title = u'The Informant!'
    watchlist_movie_83.release_date = datetime.date(2009, 9, 18)
    watchlist_movie_83.runtime = 108
    watchlist_movie_83.director = watchlist_person_19
    watchlist_movie_83.nationality = u'USA'
    watchlist_movie_83.comments = None
    watchlist_movie_83.tmdb_id = u'11323'
    watchlist_movie_83.save()

    watchlist_movie_84 = Movie()
    watchlist_movie_84.title = u'Remember the Titans'
    watchlist_movie_84.release_date = datetime.date(2000, 9, 29)
    watchlist_movie_84.runtime = 119
    watchlist_movie_84.director = watchlist_person_47
    watchlist_movie_84.nationality = u'USA'
    watchlist_movie_84.comments = None
    watchlist_movie_84.tmdb_id = u'10637'
    watchlist_movie_84.save()

    watchlist_movie_85 = Movie()
    watchlist_movie_85.title = u'Sherlock Holmes'
    watchlist_movie_85.release_date = datetime.date(2009, 12, 25)
    watchlist_movie_85.runtime = 128
    watchlist_movie_85.director = watchlist_person_48
    watchlist_movie_85.nationality = u'USA'
    watchlist_movie_85.comments = None
    watchlist_movie_85.tmdb_id = u'10528'
    watchlist_movie_85.save()

    watchlist_movie_86 = Movie()
    watchlist_movie_86.title = u'Food, Inc.'
    watchlist_movie_86.release_date = datetime.date(2008, 9, 7)
    watchlist_movie_86.runtime = 94
    watchlist_movie_86.director = watchlist_person_49
    watchlist_movie_86.nationality = u'USA'
    watchlist_movie_86.comments = None
    watchlist_movie_86.tmdb_id = u'18570'
    watchlist_movie_86.save()

    watchlist_movie_87 = Movie()
    watchlist_movie_87.title = u'Ninja Assassin'
    watchlist_movie_87.release_date = datetime.date(2009, 9, 29)
    watchlist_movie_87.runtime = 99
    watchlist_movie_87.director = watchlist_person_50
    watchlist_movie_87.nationality = None
    watchlist_movie_87.comments = None
    watchlist_movie_87.tmdb_id = u'22832'
    watchlist_movie_87.save()

    watchlist_movie_88 = Movie()
    watchlist_movie_88.title = u'Cube'
    watchlist_movie_88.release_date = datetime.date(1997, 9, 11)
    watchlist_movie_88.runtime = 90
    watchlist_movie_88.director = watchlist_person_51
    watchlist_movie_88.nationality = None
    watchlist_movie_88.comments = None
    watchlist_movie_88.tmdb_id = u'431'
    watchlist_movie_88.save()

    watchlist_movie_89 = Movie()
    watchlist_movie_89.title = u'Green Zone'
    watchlist_movie_89.release_date = datetime.date(2010, 3, 12)
    watchlist_movie_89.runtime = 115
    watchlist_movie_89.director = watchlist_person_31
    watchlist_movie_89.nationality = None
    watchlist_movie_89.comments = None
    watchlist_movie_89.tmdb_id = u'22972'
    watchlist_movie_89.save()

    watchlist_movie_90 = Movie()
    watchlist_movie_90.title = u'Greenberg'
    watchlist_movie_90.release_date = datetime.date(2010, 4, 1)
    watchlist_movie_90.runtime = 107
    watchlist_movie_90.director = watchlist_person_24
    watchlist_movie_90.nationality = None
    watchlist_movie_90.comments = None
    watchlist_movie_90.tmdb_id = u'27583'
    watchlist_movie_90.save()

    watchlist_movie_91 = Movie()
    watchlist_movie_91.title = u'The Girl Next Door'
    watchlist_movie_91.release_date = datetime.date(2004, 3, 27)
    watchlist_movie_91.runtime = 109
    watchlist_movie_91.director = watchlist_person_52
    watchlist_movie_91.nationality = None
    watchlist_movie_91.comments = None
    watchlist_movie_91.tmdb_id = u'10591'
    watchlist_movie_91.save()

    watchlist_movie_92 = Movie()
    watchlist_movie_92.title = u'Choke'
    watchlist_movie_92.release_date = datetime.date(2008, 10, 30)
    watchlist_movie_92.runtime = 89
    watchlist_movie_92.director = watchlist_person_53
    watchlist_movie_92.nationality = u'USA'
    watchlist_movie_92.comments = None
    watchlist_movie_92.tmdb_id = u'13973'
    watchlist_movie_92.save()

    watchlist_movie_93 = Movie()
    watchlist_movie_93.title = u'Kick-Ass'
    watchlist_movie_93.release_date = datetime.date(2010, 4, 16)
    watchlist_movie_93.runtime = 117
    watchlist_movie_93.director = watchlist_person_54
    watchlist_movie_93.nationality = None
    watchlist_movie_93.comments = None
    watchlist_movie_93.tmdb_id = u'23483'
    watchlist_movie_93.save()

    watchlist_movie_94 = Movie()
    watchlist_movie_94.title = u'Clash of the Titans'
    watchlist_movie_94.release_date = datetime.date(2010, 4, 2)
    watchlist_movie_94.runtime = 118
    watchlist_movie_94.director = watchlist_person_55
    watchlist_movie_94.nationality = None
    watchlist_movie_94.comments = None
    watchlist_movie_94.tmdb_id = u'18823'
    watchlist_movie_94.save()

    watchlist_movie_95 = Movie()
    watchlist_movie_95.title = u"Jennifer's Body"
    watchlist_movie_95.release_date = datetime.date(2009, 9, 18)
    watchlist_movie_95.runtime = 100
    watchlist_movie_95.director = watchlist_person_56
    watchlist_movie_95.nationality = None
    watchlist_movie_95.comments = None
    watchlist_movie_95.tmdb_id = u'19994'
    watchlist_movie_95.save()

    watchlist_movie_96 = Movie()
    watchlist_movie_96.title = u'Obsessed'
    watchlist_movie_96.release_date = datetime.date(2009, 4, 24)
    watchlist_movie_96.runtime = 105
    watchlist_movie_96.director = watchlist_person_57
    watchlist_movie_96.nationality = None
    watchlist_movie_96.comments = None
    watchlist_movie_96.tmdb_id = u'17335'
    watchlist_movie_96.save()

    watchlist_movie_97 = Movie()
    watchlist_movie_97.title = u'The Ghost Writer'
    watchlist_movie_97.release_date = datetime.date(2010, 2, 12)
    watchlist_movie_97.runtime = 128
    watchlist_movie_97.director = watchlist_person_58
    watchlist_movie_97.nationality = None
    watchlist_movie_97.comments = None
    watchlist_movie_97.tmdb_id = u'11439'
    watchlist_movie_97.save()

    watchlist_movie_98 = Movie()
    watchlist_movie_98.title = u'Prince of Persia: The Sands of Time'
    watchlist_movie_98.release_date = datetime.date(2010, 5, 26)
    watchlist_movie_98.runtime = 116
    watchlist_movie_98.director = watchlist_person_34
    watchlist_movie_98.nationality = u'USA'
    watchlist_movie_98.comments = None
    watchlist_movie_98.tmdb_id = u'9543'
    watchlist_movie_98.save()

    watchlist_movie_99 = Movie()
    watchlist_movie_99.title = u'Robin Hood'
    watchlist_movie_99.release_date = datetime.date(2010, 5, 14)
    watchlist_movie_99.runtime = 148
    watchlist_movie_99.director = watchlist_person_59
    watchlist_movie_99.nationality = u'USA'
    watchlist_movie_99.comments = None
    watchlist_movie_99.tmdb_id = u'20662'
    watchlist_movie_99.save()

    watchlist_movie_100 = Movie()
    watchlist_movie_100.title = u'The Interpreter'
    watchlist_movie_100.release_date = datetime.date(2005, 3, 11)
    watchlist_movie_100.runtime = 128
    watchlist_movie_100.director = watchlist_person_60
    watchlist_movie_100.nationality = None
    watchlist_movie_100.comments = None
    watchlist_movie_100.tmdb_id = u'179'
    watchlist_movie_100.save()

    watchlist_movie_101 = Movie()
    watchlist_movie_101.title = u'16 Blocks'
    watchlist_movie_101.release_date = datetime.date(2006, 3, 1)
    watchlist_movie_101.runtime = 102
    watchlist_movie_101.director = watchlist_person_61
    watchlist_movie_101.nationality = None
    watchlist_movie_101.comments = None
    watchlist_movie_101.tmdb_id = u'2207'
    watchlist_movie_101.save()

    watchlist_movie_102 = Movie()
    watchlist_movie_102.title = u'How to Train Your Dragon'
    watchlist_movie_102.release_date = datetime.date(2010, 3, 26)
    watchlist_movie_102.runtime = 98
    watchlist_movie_102.director = watchlist_person_62
    watchlist_movie_102.nationality = u'USA'
    watchlist_movie_102.comments = None
    watchlist_movie_102.tmdb_id = u'10191'
    watchlist_movie_102.save()

    watchlist_movie_103 = Movie()
    watchlist_movie_103.title = u"Winter's Bone"
    watchlist_movie_103.release_date = datetime.date(2010, 3, 10)
    watchlist_movie_103.runtime = 100
    watchlist_movie_103.director = watchlist_person_63
    watchlist_movie_103.nationality = None
    watchlist_movie_103.comments = None
    watchlist_movie_103.tmdb_id = u'39013'
    watchlist_movie_103.save()

    watchlist_movie_104 = Movie()
    watchlist_movie_104.title = u'The Social Network'
    watchlist_movie_104.release_date = datetime.date(2010, 10, 1)
    watchlist_movie_104.runtime = 121
    watchlist_movie_104.director = watchlist_person_64
    watchlist_movie_104.nationality = None
    watchlist_movie_104.comments = None
    watchlist_movie_104.tmdb_id = u'37799'
    watchlist_movie_104.save()

    watchlist_movie_105 = Movie()
    watchlist_movie_105.title = u'Catfish'
    watchlist_movie_105.release_date = datetime.date(2010, 9, 17)
    watchlist_movie_105.runtime = 87
    watchlist_movie_105.director = watchlist_person_65
    watchlist_movie_105.nationality = u'USA'
    watchlist_movie_105.comments = None
    watchlist_movie_105.tmdb_id = u'42296'
    watchlist_movie_105.save()

    watchlist_movie_106 = Movie()
    watchlist_movie_106.title = u'Exit Through the Gift Shop'
    watchlist_movie_106.release_date = datetime.date(2010, 3, 22)
    watchlist_movie_106.runtime = 87
    watchlist_movie_106.director = watchlist_person_66
    watchlist_movie_106.nationality = None
    watchlist_movie_106.comments = None
    watchlist_movie_106.tmdb_id = u'39452'
    watchlist_movie_106.save()

    watchlist_movie_107 = Movie()
    watchlist_movie_107.title = u'Due Date'
    watchlist_movie_107.release_date = datetime.date(2010, 11, 5)
    watchlist_movie_107.runtime = 100
    watchlist_movie_107.director = watchlist_person_12
    watchlist_movie_107.nationality = u'USA'
    watchlist_movie_107.comments = None
    watchlist_movie_107.tmdb_id = u'41733'
    watchlist_movie_107.save()

    watchlist_movie_108 = Movie()
    watchlist_movie_108.title = u'Scott Pilgrim vs. the World'
    watchlist_movie_108.release_date = datetime.date(2010, 8, 13)
    watchlist_movie_108.runtime = 112
    watchlist_movie_108.director = watchlist_person_67
    watchlist_movie_108.nationality = u'USA'
    watchlist_movie_108.comments = None
    watchlist_movie_108.tmdb_id = u'22538'
    watchlist_movie_108.save()

    watchlist_movie_109 = Movie()
    watchlist_movie_109.title = u'Splice'
    watchlist_movie_109.release_date = datetime.date(2010, 6, 4)
    watchlist_movie_109.runtime = 104
    watchlist_movie_109.director = watchlist_person_51
    watchlist_movie_109.nationality = None
    watchlist_movie_109.comments = None
    watchlist_movie_109.tmdb_id = u'37707'
    watchlist_movie_109.save()

    watchlist_movie_110 = Movie()
    watchlist_movie_110.title = u'Beverly Hills Cop'
    watchlist_movie_110.release_date = datetime.date(1984, 12, 5)
    watchlist_movie_110.runtime = 105
    watchlist_movie_110.director = watchlist_person_68
    watchlist_movie_110.nationality = u'USA'
    watchlist_movie_110.comments = None
    watchlist_movie_110.tmdb_id = u'90'
    watchlist_movie_110.save()

    watchlist_movie_111 = Movie()
    watchlist_movie_111.title = u'Inception'
    watchlist_movie_111.release_date = datetime.date(2010, 7, 16)
    watchlist_movie_111.runtime = 148
    watchlist_movie_111.director = watchlist_person_69
    watchlist_movie_111.nationality = u'USA'
    watchlist_movie_111.comments = None
    watchlist_movie_111.tmdb_id = u'27205'
    watchlist_movie_111.save()

    from watchlist2.watchlist.models import Viewing

    watchlist_viewing_1 = Viewing()
    watchlist_viewing_1.movie = watchlist_movie_1
    watchlist_viewing_1.date = datetime.date(2009, 5, 29)
    watchlist_viewing_1.notes = None
    watchlist_viewing_1.save()

    watchlist_viewing_2 = Viewing()
    watchlist_viewing_2.movie = watchlist_movie_2
    watchlist_viewing_2.date = datetime.date(2009, 5, 30)
    watchlist_viewing_2.notes = None
    watchlist_viewing_2.save()

    watchlist_viewing_3 = Viewing()
    watchlist_viewing_3.movie = watchlist_movie_3
    watchlist_viewing_3.date = datetime.date(2009, 6, 1)
    watchlist_viewing_3.notes = None
    watchlist_viewing_3.save()

    watchlist_viewing_4 = Viewing()
    watchlist_viewing_4.movie = watchlist_movie_4
    watchlist_viewing_4.date = datetime.date(2009, 6, 1)
    watchlist_viewing_4.notes = None
    watchlist_viewing_4.save()

    watchlist_viewing_5 = Viewing()
    watchlist_viewing_5.movie = watchlist_movie_5
    watchlist_viewing_5.date = datetime.date(2009, 6, 2)
    watchlist_viewing_5.notes = None
    watchlist_viewing_5.save()

    watchlist_viewing_6 = Viewing()
    watchlist_viewing_6.movie = watchlist_movie_6
    watchlist_viewing_6.date = datetime.date(2009, 6, 3)
    watchlist_viewing_6.notes = None
    watchlist_viewing_6.save()

    watchlist_viewing_7 = Viewing()
    watchlist_viewing_7.movie = watchlist_movie_7
    watchlist_viewing_7.date = datetime.date(2009, 6, 10)
    watchlist_viewing_7.notes = None
    watchlist_viewing_7.save()

    watchlist_viewing_8 = Viewing()
    watchlist_viewing_8.movie = watchlist_movie_8
    watchlist_viewing_8.date = datetime.date(2009, 6, 15)
    watchlist_viewing_8.notes = None
    watchlist_viewing_8.save()

    watchlist_viewing_9 = Viewing()
    watchlist_viewing_9.movie = watchlist_movie_9
    watchlist_viewing_9.date = datetime.date(2009, 6, 18)
    watchlist_viewing_9.notes = None
    watchlist_viewing_9.save()

    watchlist_viewing_10 = Viewing()
    watchlist_viewing_10.movie = watchlist_movie_10
    watchlist_viewing_10.date = datetime.date(2009, 6, 19)
    watchlist_viewing_10.notes = None
    watchlist_viewing_10.save()

    watchlist_viewing_11 = Viewing()
    watchlist_viewing_11.movie = watchlist_movie_11
    watchlist_viewing_11.date = datetime.date(2009, 6, 20)
    watchlist_viewing_11.notes = None
    watchlist_viewing_11.save()

    watchlist_viewing_12 = Viewing()
    watchlist_viewing_12.movie = watchlist_movie_12
    watchlist_viewing_12.date = datetime.date(2009, 6, 20)
    watchlist_viewing_12.notes = None
    watchlist_viewing_12.save()

    watchlist_viewing_13 = Viewing()
    watchlist_viewing_13.movie = watchlist_movie_13
    watchlist_viewing_13.date = datetime.date(2009, 6, 21)
    watchlist_viewing_13.notes = None
    watchlist_viewing_13.save()

    watchlist_viewing_14 = Viewing()
    watchlist_viewing_14.movie = watchlist_movie_14
    watchlist_viewing_14.date = datetime.date(2009, 6, 30)
    watchlist_viewing_14.notes = None
    watchlist_viewing_14.save()

    watchlist_viewing_15 = Viewing()
    watchlist_viewing_15.movie = watchlist_movie_15
    watchlist_viewing_15.date = datetime.date(2009, 7, 1)
    watchlist_viewing_15.notes = None
    watchlist_viewing_15.save()

    watchlist_viewing_16 = Viewing()
    watchlist_viewing_16.movie = watchlist_movie_16
    watchlist_viewing_16.date = datetime.date(2009, 7, 5)
    watchlist_viewing_16.notes = None
    watchlist_viewing_16.save()

    watchlist_viewing_17 = Viewing()
    watchlist_viewing_17.movie = watchlist_movie_17
    watchlist_viewing_17.date = datetime.date(2009, 7, 10)
    watchlist_viewing_17.notes = None
    watchlist_viewing_17.save()

    watchlist_viewing_18 = Viewing()
    watchlist_viewing_18.movie = watchlist_movie_18
    watchlist_viewing_18.date = datetime.date(2009, 7, 11)
    watchlist_viewing_18.notes = None
    watchlist_viewing_18.save()

    watchlist_viewing_19 = Viewing()
    watchlist_viewing_19.movie = watchlist_movie_19
    watchlist_viewing_19.date = datetime.date(2009, 7, 11)
    watchlist_viewing_19.notes = None
    watchlist_viewing_19.save()

    watchlist_viewing_20 = Viewing()
    watchlist_viewing_20.movie = watchlist_movie_20
    watchlist_viewing_20.date = datetime.date(2009, 7, 11)
    watchlist_viewing_20.notes = None
    watchlist_viewing_20.save()

    watchlist_viewing_21 = Viewing()
    watchlist_viewing_21.movie = watchlist_movie_21
    watchlist_viewing_21.date = datetime.date(2009, 7, 15)
    watchlist_viewing_21.notes = None
    watchlist_viewing_21.save()

    watchlist_viewing_22 = Viewing()
    watchlist_viewing_22.movie = watchlist_movie_22
    watchlist_viewing_22.date = datetime.date(2009, 7, 15)
    watchlist_viewing_22.notes = None
    watchlist_viewing_22.save()

    watchlist_viewing_23 = Viewing()
    watchlist_viewing_23.movie = watchlist_movie_23
    watchlist_viewing_23.date = datetime.date(2009, 7, 18)
    watchlist_viewing_23.notes = None
    watchlist_viewing_23.save()

    watchlist_viewing_24 = Viewing()
    watchlist_viewing_24.movie = watchlist_movie_24
    watchlist_viewing_24.date = datetime.date(2009, 7, 18)
    watchlist_viewing_24.notes = None
    watchlist_viewing_24.save()

    watchlist_viewing_25 = Viewing()
    watchlist_viewing_25.movie = watchlist_movie_25
    watchlist_viewing_25.date = datetime.date(2009, 7, 20)
    watchlist_viewing_25.notes = None
    watchlist_viewing_25.save()

    watchlist_viewing_26 = Viewing()
    watchlist_viewing_26.movie = watchlist_movie_26
    watchlist_viewing_26.date = datetime.date(2009, 7, 20)
    watchlist_viewing_26.notes = None
    watchlist_viewing_26.save()

    watchlist_viewing_27 = Viewing()
    watchlist_viewing_27.movie = watchlist_movie_27
    watchlist_viewing_27.date = datetime.date(2009, 7, 21)
    watchlist_viewing_27.notes = None
    watchlist_viewing_27.save()

    watchlist_viewing_28 = Viewing()
    watchlist_viewing_28.movie = watchlist_movie_28
    watchlist_viewing_28.date = datetime.date(2009, 7, 22)
    watchlist_viewing_28.notes = None
    watchlist_viewing_28.save()

    watchlist_viewing_29 = Viewing()
    watchlist_viewing_29.movie = watchlist_movie_29
    watchlist_viewing_29.date = datetime.date(2009, 7, 23)
    watchlist_viewing_29.notes = None
    watchlist_viewing_29.save()

    watchlist_viewing_30 = Viewing()
    watchlist_viewing_30.movie = watchlist_movie_30
    watchlist_viewing_30.date = datetime.date(2009, 7, 24)
    watchlist_viewing_30.notes = None
    watchlist_viewing_30.save()

    watchlist_viewing_31 = Viewing()
    watchlist_viewing_31.movie = watchlist_movie_31
    watchlist_viewing_31.date = datetime.date(2009, 7, 26)
    watchlist_viewing_31.notes = None
    watchlist_viewing_31.save()

    watchlist_viewing_32 = Viewing()
    watchlist_viewing_32.movie = watchlist_movie_32
    watchlist_viewing_32.date = datetime.date(2009, 7, 28)
    watchlist_viewing_32.notes = None
    watchlist_viewing_32.save()

    watchlist_viewing_33 = Viewing()
    watchlist_viewing_33.movie = watchlist_movie_33
    watchlist_viewing_33.date = datetime.date(2009, 7, 31)
    watchlist_viewing_33.notes = None
    watchlist_viewing_33.save()

    watchlist_viewing_34 = Viewing()
    watchlist_viewing_34.movie = watchlist_movie_34
    watchlist_viewing_34.date = datetime.date(2009, 7, 31)
    watchlist_viewing_34.notes = None
    watchlist_viewing_34.save()

    watchlist_viewing_35 = Viewing()
    watchlist_viewing_35.movie = watchlist_movie_35
    watchlist_viewing_35.date = datetime.date(2009, 8, 1)
    watchlist_viewing_35.notes = None
    watchlist_viewing_35.save()

    watchlist_viewing_36 = Viewing()
    watchlist_viewing_36.movie = watchlist_movie_36
    watchlist_viewing_36.date = datetime.date(2009, 8, 2)
    watchlist_viewing_36.notes = None
    watchlist_viewing_36.save()

    watchlist_viewing_37 = Viewing()
    watchlist_viewing_37.movie = watchlist_movie_37
    watchlist_viewing_37.date = datetime.date(2009, 8, 3)
    watchlist_viewing_37.notes = None
    watchlist_viewing_37.save()

    watchlist_viewing_38 = Viewing()
    watchlist_viewing_38.movie = watchlist_movie_38
    watchlist_viewing_38.date = datetime.date(2009, 8, 3)
    watchlist_viewing_38.notes = None
    watchlist_viewing_38.save()

    watchlist_viewing_39 = Viewing()
    watchlist_viewing_39.movie = watchlist_movie_39
    watchlist_viewing_39.date = datetime.date(2009, 8, 5)
    watchlist_viewing_39.notes = None
    watchlist_viewing_39.save()

    watchlist_viewing_40 = Viewing()
    watchlist_viewing_40.movie = watchlist_movie_40
    watchlist_viewing_40.date = datetime.date(2009, 8, 8)
    watchlist_viewing_40.notes = None
    watchlist_viewing_40.save()

    watchlist_viewing_41 = Viewing()
    watchlist_viewing_41.movie = watchlist_movie_41
    watchlist_viewing_41.date = datetime.date(2009, 8, 9)
    watchlist_viewing_41.notes = None
    watchlist_viewing_41.save()

    watchlist_viewing_42 = Viewing()
    watchlist_viewing_42.movie = watchlist_movie_42
    watchlist_viewing_42.date = datetime.date(2009, 8, 10)
    watchlist_viewing_42.notes = None
    watchlist_viewing_42.save()

    watchlist_viewing_43 = Viewing()
    watchlist_viewing_43.movie = watchlist_movie_43
    watchlist_viewing_43.date = datetime.date(2009, 8, 12)
    watchlist_viewing_43.notes = None
    watchlist_viewing_43.save()

    watchlist_viewing_44 = Viewing()
    watchlist_viewing_44.movie = watchlist_movie_44
    watchlist_viewing_44.date = datetime.date(2009, 8, 15)
    watchlist_viewing_44.notes = None
    watchlist_viewing_44.save()

    watchlist_viewing_45 = Viewing()
    watchlist_viewing_45.movie = watchlist_movie_45
    watchlist_viewing_45.date = datetime.date(2009, 8, 15)
    watchlist_viewing_45.notes = None
    watchlist_viewing_45.save()

    watchlist_viewing_46 = Viewing()
    watchlist_viewing_46.movie = watchlist_movie_46
    watchlist_viewing_46.date = datetime.date(2009, 8, 16)
    watchlist_viewing_46.notes = None
    watchlist_viewing_46.save()

    watchlist_viewing_47 = Viewing()
    watchlist_viewing_47.movie = watchlist_movie_47
    watchlist_viewing_47.date = datetime.date(2009, 8, 18)
    watchlist_viewing_47.notes = None
    watchlist_viewing_47.save()

    watchlist_viewing_48 = Viewing()
    watchlist_viewing_48.movie = watchlist_movie_48
    watchlist_viewing_48.date = datetime.date(2009, 8, 18)
    watchlist_viewing_48.notes = None
    watchlist_viewing_48.save()

    watchlist_viewing_49 = Viewing()
    watchlist_viewing_49.movie = watchlist_movie_49
    watchlist_viewing_49.date = datetime.date(2009, 8, 19)
    watchlist_viewing_49.notes = None
    watchlist_viewing_49.save()

    watchlist_viewing_50 = Viewing()
    watchlist_viewing_50.movie = watchlist_movie_50
    watchlist_viewing_50.date = datetime.date(2009, 8, 22)
    watchlist_viewing_50.notes = None
    watchlist_viewing_50.save()

    watchlist_viewing_51 = Viewing()
    watchlist_viewing_51.movie = watchlist_movie_51
    watchlist_viewing_51.date = datetime.date(2009, 8, 24)
    watchlist_viewing_51.notes = None
    watchlist_viewing_51.save()

    watchlist_viewing_52 = Viewing()
    watchlist_viewing_52.movie = watchlist_movie_52
    watchlist_viewing_52.date = datetime.date(2009, 8, 29)
    watchlist_viewing_52.notes = None
    watchlist_viewing_52.save()

    watchlist_viewing_53 = Viewing()
    watchlist_viewing_53.movie = watchlist_movie_53
    watchlist_viewing_53.date = datetime.date(2009, 8, 30)
    watchlist_viewing_53.notes = None
    watchlist_viewing_53.save()

    watchlist_viewing_54 = Viewing()
    watchlist_viewing_54.movie = watchlist_movie_54
    watchlist_viewing_54.date = datetime.date(2009, 9, 4)
    watchlist_viewing_54.notes = None
    watchlist_viewing_54.save()

    watchlist_viewing_55 = Viewing()
    watchlist_viewing_55.movie = watchlist_movie_55
    watchlist_viewing_55.date = datetime.date(2009, 9, 5)
    watchlist_viewing_55.notes = None
    watchlist_viewing_55.save()

    watchlist_viewing_56 = Viewing()
    watchlist_viewing_56.movie = watchlist_movie_56
    watchlist_viewing_56.date = datetime.date(2009, 9, 7)
    watchlist_viewing_56.notes = None
    watchlist_viewing_56.save()

    watchlist_viewing_57 = Viewing()
    watchlist_viewing_57.movie = watchlist_movie_57
    watchlist_viewing_57.date = datetime.date(2009, 9, 8)
    watchlist_viewing_57.notes = None
    watchlist_viewing_57.save()

    watchlist_viewing_58 = Viewing()
    watchlist_viewing_58.movie = watchlist_movie_58
    watchlist_viewing_58.date = datetime.date(2009, 9, 9)
    watchlist_viewing_58.notes = None
    watchlist_viewing_58.save()

    watchlist_viewing_59 = Viewing()
    watchlist_viewing_59.movie = watchlist_movie_59
    watchlist_viewing_59.date = datetime.date(2009, 9, 13)
    watchlist_viewing_59.notes = None
    watchlist_viewing_59.save()

    watchlist_viewing_60 = Viewing()
    watchlist_viewing_60.movie = watchlist_movie_60
    watchlist_viewing_60.date = datetime.date(2009, 9, 13)
    watchlist_viewing_60.notes = None
    watchlist_viewing_60.save()

    watchlist_viewing_61 = Viewing()
    watchlist_viewing_61.movie = watchlist_movie_61
    watchlist_viewing_61.date = datetime.date(2009, 9, 17)
    watchlist_viewing_61.notes = None
    watchlist_viewing_61.save()

    watchlist_viewing_62 = Viewing()
    watchlist_viewing_62.movie = watchlist_movie_62
    watchlist_viewing_62.date = datetime.date(2009, 9, 19)
    watchlist_viewing_62.notes = None
    watchlist_viewing_62.save()

    watchlist_viewing_63 = Viewing()
    watchlist_viewing_63.movie = watchlist_movie_63
    watchlist_viewing_63.date = datetime.date(2009, 9, 19)
    watchlist_viewing_63.notes = None
    watchlist_viewing_63.save()

    watchlist_viewing_64 = Viewing()
    watchlist_viewing_64.movie = watchlist_movie_64
    watchlist_viewing_64.date = datetime.date(2009, 10, 14)
    watchlist_viewing_64.notes = None
    watchlist_viewing_64.save()

    watchlist_viewing_65 = Viewing()
    watchlist_viewing_65.movie = watchlist_movie_65
    watchlist_viewing_65.date = datetime.date(2009, 10, 14)
    watchlist_viewing_65.notes = None
    watchlist_viewing_65.save()

    watchlist_viewing_66 = Viewing()
    watchlist_viewing_66.movie = watchlist_movie_66
    watchlist_viewing_66.date = datetime.date(2009, 10, 23)
    watchlist_viewing_66.notes = None
    watchlist_viewing_66.save()

    watchlist_viewing_67 = Viewing()
    watchlist_viewing_67.movie = watchlist_movie_67
    watchlist_viewing_67.date = datetime.date(2009, 10, 24)
    watchlist_viewing_67.notes = None
    watchlist_viewing_67.save()

    watchlist_viewing_68 = Viewing()
    watchlist_viewing_68.movie = watchlist_movie_68
    watchlist_viewing_68.date = datetime.date(2009, 10, 25)
    watchlist_viewing_68.notes = None
    watchlist_viewing_68.save()

    watchlist_viewing_69 = Viewing()
    watchlist_viewing_69.movie = watchlist_movie_69
    watchlist_viewing_69.date = datetime.date(2009, 10, 26)
    watchlist_viewing_69.notes = None
    watchlist_viewing_69.save()

    watchlist_viewing_70 = Viewing()
    watchlist_viewing_70.movie = watchlist_movie_70
    watchlist_viewing_70.date = datetime.date(2009, 10, 27)
    watchlist_viewing_70.notes = None
    watchlist_viewing_70.save()

    watchlist_viewing_71 = Viewing()
    watchlist_viewing_71.movie = watchlist_movie_71
    watchlist_viewing_71.date = datetime.date(2009, 10, 28)
    watchlist_viewing_71.notes = None
    watchlist_viewing_71.save()

    watchlist_viewing_72 = Viewing()
    watchlist_viewing_72.movie = watchlist_movie_72
    watchlist_viewing_72.date = datetime.date(2009, 10, 30)
    watchlist_viewing_72.notes = None
    watchlist_viewing_72.save()

    watchlist_viewing_73 = Viewing()
    watchlist_viewing_73.movie = watchlist_movie_73
    watchlist_viewing_73.date = datetime.date(2009, 11, 16)
    watchlist_viewing_73.notes = None
    watchlist_viewing_73.save()

    watchlist_viewing_74 = Viewing()
    watchlist_viewing_74.movie = watchlist_movie_74
    watchlist_viewing_74.date = datetime.date(2009, 11, 25)
    watchlist_viewing_74.notes = None
    watchlist_viewing_74.save()

    watchlist_viewing_75 = Viewing()
    watchlist_viewing_75.movie = watchlist_movie_75
    watchlist_viewing_75.date = datetime.date(2009, 12, 5)
    watchlist_viewing_75.notes = None
    watchlist_viewing_75.save()

    watchlist_viewing_76 = Viewing()
    watchlist_viewing_76.movie = watchlist_movie_76
    watchlist_viewing_76.date = datetime.date(2009, 12, 5)
    watchlist_viewing_76.notes = None
    watchlist_viewing_76.save()

    watchlist_viewing_77 = Viewing()
    watchlist_viewing_77.movie = watchlist_movie_77
    watchlist_viewing_77.date = datetime.date(2009, 12, 10)
    watchlist_viewing_77.notes = None
    watchlist_viewing_77.save()

    watchlist_viewing_78 = Viewing()
    watchlist_viewing_78.movie = watchlist_movie_78
    watchlist_viewing_78.date = datetime.date(2009, 12, 19)
    watchlist_viewing_78.notes = None
    watchlist_viewing_78.save()

    watchlist_viewing_79 = Viewing()
    watchlist_viewing_79.movie = watchlist_movie_79
    watchlist_viewing_79.date = datetime.date(2010, 1, 4)
    watchlist_viewing_79.notes = None
    watchlist_viewing_79.save()

    watchlist_viewing_80 = Viewing()
    watchlist_viewing_80.movie = watchlist_movie_80
    watchlist_viewing_80.date = datetime.date(2010, 1, 7)
    watchlist_viewing_80.notes = None
    watchlist_viewing_80.save()

    watchlist_viewing_81 = Viewing()
    watchlist_viewing_81.movie = watchlist_movie_81
    watchlist_viewing_81.date = datetime.date(2010, 1, 24)
    watchlist_viewing_81.notes = None
    watchlist_viewing_81.save()

    watchlist_viewing_82 = Viewing()
    watchlist_viewing_82.movie = watchlist_movie_82
    watchlist_viewing_82.date = datetime.date(2010, 1, 30)
    watchlist_viewing_82.notes = None
    watchlist_viewing_82.save()

    watchlist_viewing_83 = Viewing()
    watchlist_viewing_83.movie = watchlist_movie_83
    watchlist_viewing_83.date = datetime.date(2010, 2, 6)
    watchlist_viewing_83.notes = None
    watchlist_viewing_83.save()

    watchlist_viewing_84 = Viewing()
    watchlist_viewing_84.movie = watchlist_movie_84
    watchlist_viewing_84.date = datetime.date(2010, 2, 8)
    watchlist_viewing_84.notes = None
    watchlist_viewing_84.save()

    watchlist_viewing_85 = Viewing()
    watchlist_viewing_85.movie = watchlist_movie_85
    watchlist_viewing_85.date = datetime.date(2010, 2, 13)
    watchlist_viewing_85.notes = None
    watchlist_viewing_85.save()

    watchlist_viewing_86 = Viewing()
    watchlist_viewing_86.movie = watchlist_movie_86
    watchlist_viewing_86.date = datetime.date(2010, 5, 15)
    watchlist_viewing_86.notes = None
    watchlist_viewing_86.save()

    watchlist_viewing_87 = Viewing()
    watchlist_viewing_87.movie = watchlist_movie_87
    watchlist_viewing_87.date = datetime.date(2010, 6, 3)
    watchlist_viewing_87.notes = None
    watchlist_viewing_87.save()

    watchlist_viewing_88 = Viewing()
    watchlist_viewing_88.movie = watchlist_movie_88
    watchlist_viewing_88.date = datetime.date(2010, 6, 13)
    watchlist_viewing_88.notes = None
    watchlist_viewing_88.save()

    watchlist_viewing_89 = Viewing()
    watchlist_viewing_89.movie = watchlist_movie_89
    watchlist_viewing_89.date = datetime.date(2010, 6, 14)
    watchlist_viewing_89.notes = None
    watchlist_viewing_89.save()

    watchlist_viewing_90 = Viewing()
    watchlist_viewing_90.movie = watchlist_movie_90
    watchlist_viewing_90.date = datetime.date(2010, 7, 8)
    watchlist_viewing_90.notes = None
    watchlist_viewing_90.save()

    watchlist_viewing_91 = Viewing()
    watchlist_viewing_91.movie = watchlist_movie_91
    watchlist_viewing_91.date = datetime.date(2010, 7, 10)
    watchlist_viewing_91.notes = None
    watchlist_viewing_91.save()

    watchlist_viewing_92 = Viewing()
    watchlist_viewing_92.movie = watchlist_movie_92
    watchlist_viewing_92.date = datetime.date(2010, 7, 26)
    watchlist_viewing_92.notes = None
    watchlist_viewing_92.save()

    watchlist_viewing_93 = Viewing()
    watchlist_viewing_93.movie = watchlist_movie_93
    watchlist_viewing_93.date = datetime.date(2010, 8, 2)
    watchlist_viewing_93.notes = None
    watchlist_viewing_93.save()

    watchlist_viewing_94 = Viewing()
    watchlist_viewing_94.movie = watchlist_movie_94
    watchlist_viewing_94.date = datetime.date(2010, 8, 2)
    watchlist_viewing_94.notes = None
    watchlist_viewing_94.save()

    watchlist_viewing_95 = Viewing()
    watchlist_viewing_95.movie = watchlist_movie_95
    watchlist_viewing_95.date = datetime.date(2010, 8, 3)
    watchlist_viewing_95.notes = None
    watchlist_viewing_95.save()

    watchlist_viewing_96 = Viewing()
    watchlist_viewing_96.movie = watchlist_movie_96
    watchlist_viewing_96.date = datetime.date(2010, 8, 8)
    watchlist_viewing_96.notes = None
    watchlist_viewing_96.save()

    watchlist_viewing_97 = Viewing()
    watchlist_viewing_97.movie = watchlist_movie_97
    watchlist_viewing_97.date = datetime.date(2010, 8, 9)
    watchlist_viewing_97.notes = None
    watchlist_viewing_97.save()

    watchlist_viewing_98 = Viewing()
    watchlist_viewing_98.movie = watchlist_movie_98
    watchlist_viewing_98.date = datetime.date(2010, 9, 1)
    watchlist_viewing_98.notes = None
    watchlist_viewing_98.save()

    watchlist_viewing_99 = Viewing()
    watchlist_viewing_99.movie = watchlist_movie_99
    watchlist_viewing_99.date = datetime.date(2010, 9, 11)
    watchlist_viewing_99.notes = None
    watchlist_viewing_99.save()

    watchlist_viewing_100 = Viewing()
    watchlist_viewing_100.movie = watchlist_movie_100
    watchlist_viewing_100.date = datetime.date(2010, 9, 26)
    watchlist_viewing_100.notes = None
    watchlist_viewing_100.save()

    watchlist_viewing_101 = Viewing()
    watchlist_viewing_101.movie = watchlist_movie_101
    watchlist_viewing_101.date = datetime.date(2010, 10, 1)
    watchlist_viewing_101.notes = None
    watchlist_viewing_101.save()

    watchlist_viewing_102 = Viewing()
    watchlist_viewing_102.movie = watchlist_movie_102
    watchlist_viewing_102.date = datetime.date(2010, 10, 9)
    watchlist_viewing_102.notes = None
    watchlist_viewing_102.save()

    watchlist_viewing_103 = Viewing()
    watchlist_viewing_103.movie = watchlist_movie_103
    watchlist_viewing_103.date = datetime.date(2010, 10, 19)
    watchlist_viewing_103.notes = None
    watchlist_viewing_103.save()

    watchlist_viewing_104 = Viewing()
    watchlist_viewing_104.movie = watchlist_movie_104
    watchlist_viewing_104.date = datetime.date(2010, 10, 3)
    watchlist_viewing_104.notes = None
    watchlist_viewing_104.save()

    watchlist_viewing_105 = Viewing()
    watchlist_viewing_105.movie = watchlist_movie_105
    watchlist_viewing_105.date = datetime.date(2010, 11, 18)
    watchlist_viewing_105.notes = None
    watchlist_viewing_105.save()

    watchlist_viewing_106 = Viewing()
    watchlist_viewing_106.movie = watchlist_movie_106
    watchlist_viewing_106.date = datetime.date(2010, 11, 20)
    watchlist_viewing_106.notes = None
    watchlist_viewing_106.save()

    watchlist_viewing_107 = Viewing()
    watchlist_viewing_107.movie = watchlist_movie_107
    watchlist_viewing_107.date = datetime.date(2010, 11, 27)
    watchlist_viewing_107.notes = None
    watchlist_viewing_107.save()

    watchlist_viewing_108 = Viewing()
    watchlist_viewing_108.movie = watchlist_movie_108
    watchlist_viewing_108.date = datetime.date(2010, 12, 4)
    watchlist_viewing_108.notes = None
    watchlist_viewing_108.save()

    watchlist_viewing_109 = Viewing()
    watchlist_viewing_109.movie = watchlist_movie_109
    watchlist_viewing_109.date = datetime.date(2010, 10, 5)
    watchlist_viewing_109.notes = None
    watchlist_viewing_109.save()

    watchlist_viewing_110 = Viewing()
    watchlist_viewing_110.movie = watchlist_movie_110
    watchlist_viewing_110.date = datetime.date(2010, 12, 5)
    watchlist_viewing_110.notes = None
    watchlist_viewing_110.save()

    watchlist_viewing_111 = Viewing()
    watchlist_viewing_111.movie = watchlist_movie_111
    watchlist_viewing_111.date = datetime.date(2010, 12, 10)
    watchlist_viewing_111.notes = None
    watchlist_viewing_111.save()

