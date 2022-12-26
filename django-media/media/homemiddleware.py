# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.contrib.sessions.models import Session
from django.template import RequestContext, Context, Template
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch

#import feedparser
import string
import random



from django.shortcuts import render

from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

from django.utils.deprecation import MiddlewareMixin

import re

from django.db.models import Q

import requests

from itertools import chain
from operator import attrgetter

from django.utils.crypto import get_random_string


from . models import *

#from . tasks import save_session_urls





DELAYED_SYSTEM = False



