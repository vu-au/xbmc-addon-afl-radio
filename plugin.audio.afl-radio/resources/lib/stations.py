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

import sys
import config, utils
import xbmc, xbmcgui, xbmcplugin

__handle__ = int(sys.argv[1])

def list_stations():
	for station in config.STATIONS:

		thumb = config.THUMB_PATH % station['id']
		listitem = xbmcgui.ListItem(station['name'])
		labels = {
			"title": station['name'],
			"genre": "Sport"
		}
		listitem.setInfo(type='music', infoLabels=labels)
		listitem.setThumbnailImage(thumb)

		params = utils.make_url({
			"id": station['id'], 
			"name": station['name']
		})
		url = "%s?%s" % (sys.argv[0], params)
		xbmcplugin.addDirectoryItem(handle=__handle__, url=url, listitem=listitem)

	xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)
