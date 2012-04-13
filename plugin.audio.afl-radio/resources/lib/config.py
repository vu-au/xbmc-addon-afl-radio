#
#    AFL Radio XBMC Plugin
#    Copyright (C) 2012 Andy Botting
#
#    AFL Radio is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AFL Radio is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AFL Radio.  If not, see <http://www.gnu.org/licenses/>.
#

import os

NAME = 'AFL Radio'
VERSION = '0.2'

HOST = "lon-cdn220-is-1.se.bptvlive.ngcdn.telstra.com"
URL = "http://" + HOST + "/online-radio-afl_%s"
THUMB_PATH = os.path.join(os.getcwd(), "resources", "img", "radio_%s.jpg")

# Stations list
STATIONS = [
	{ 'name':'SEN Melbourne',                     'id':'1' },
	{ 'name':'ABC774',                            'id':'2' },
	{ 'name':'5AA Adelaide',                      'id':'3' },
	{ 'name':'6PR Perth',                         'id':'4' },
	{ 'name':'3AW Melbourne',                     'id':'5' },
#	{ 'name':'National Indigenous Radio Service', 'id':'6' },
	{ 'name':'Gold FM Gold Coast',                'id':'7' },
	{ 'name':'Triple M Sydney',                   'id':'11' },
	{ 'name':'Triple M Melbourne',                'id':'12' },
	{ 'name':'Triple M Brisbane',                 'id':'13' },
	{ 'name':'Triple M Adelaide',                 'id':'14' },
	{ 'name':'K-Rock Geelong',                    'id':'15' },
]
