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

import config, utils
import xbmc, xbmcgui, xbmcplugin

def play(params):
	p = utils.get_url(params)

	# Show a dialog
	d = xbmcgui.DialogProgress()
	d.create(config.NAME, "Starting %s..." % p['name'])

	try:
		thumb = config.THUMB_PATH % p['id']
		labels = {
			"label": p['name'],
			"title": p['name'],
			"artist": config.NAME,
			"genre": "Sport"
		}
		listitem = xbmcgui.ListItem(p['name'])
		listitem.setInfo(type='music', infoLabels=labels)
		listitem.setThumbnailImage(thumb)
		url = "http://%s/online-radio-afl_%s" % (config.HOST, p['id'])
		xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, listitem)
	except:
		# user cancelled dialog or an error occurred
		d = xbmcgui.Dialog()
		message = utils.dialog_error("Unable to play %s" % p['name'])
		d.ok(*message)
		utils.log_error();
