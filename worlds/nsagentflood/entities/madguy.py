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
# GNU General Public License for more details.  #
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import ctypes
from sdl2 import *
import time

sys.path.append("../../../");

from __init__ import *
import classes.entity

class MadGuy(classes.entity.Entity):

	def __init__(self, entityValues, spriteResource):

		classes.entity.Entity.__init__(self, entityValues, world, spriteResource);

	def entityAI(self, player, movementZoneList):

		if time.time() > self.atttimer + self.attinterval and (self.x == player.x + spriteSize or self.x == player.x - spriteSize) and self.y == player.y:

			print self.name + " hit you!";

			if player.health == 1:

				print "You died."
				return;

			self.atttimer = time.time();
			player.health -= 1;

		elif time.time() > self.mvttimer + self.mvtinterval:

			self.mvttimer = time.time();

			if self.x > player.x + spriteSize and self.x != player.x - spriteSize:

				self.setOrientation(DirectionsResource.left);
				self.setXCoord(self.x - stepSize, movementZoneList);

			elif self.x < player.x + spriteSize and self.x != player.x - spriteSize:

				self.setOrientation(DirectionsResource.right);
				self.setXCoord(self.x + stepSize, movementZoneList);

			elif self.y > player.y:

				self.setYCoord(self.y - stepSize, movementZoneList);

			elif self.y < player.y:

				self.setYCoord(self.y + stepSize, movementZoneList);
