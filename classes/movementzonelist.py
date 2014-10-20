#!/usr/bin/env python2
#
# Copyright 2014 Joel Cool-Panama <mr.jkuhl@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import ctypes
from sdl2 import *

from __init__ import *

class MovementZoneList():

	def __init__(self, stage):

		self.zoneList = [];

		counter = 1;

		while True:

			try:

				zone = stage.get('stage', "movementZone" + str(counter));
				zone = zone.split(',');
				zone = [int(num) for num in zone];

				self.zoneList.append(zone);
				counter += 1;

			except:

				break;
