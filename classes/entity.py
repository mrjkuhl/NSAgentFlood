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

class Entity():

	sprite = "";

	def __init__(self, entityValues, world, spriteResource):

		self.x = int(entityValues[0]);
		self.y = int(entityValues[1]);
		self.health = int(entityValues[2]);
		self.orientation = entityValues[3];
		self.attinterval = float(entityValues[4]);
		self.mvtinterval = float(entityValues[5]);
		self.atttimer = int(entityValues[6]);
		self.mvttimer = int(entityValues[7]);
		self.name = entityValues[8];
		self.destination = SDL_Rect(self.x, self.y, spriteSize, spriteSize);

		self.spriteResource = spriteResource;

		self.updateSprite();

	def setOrientation(self, newOrientation):

		self.orientation = newOrientation;

		self.updateSprite();

	def setXCoord(self, newXCoord, movementZoneList):

		if self.testZone(movementZoneList, newXCoord, self.y):

			self.x = newXCoord;

			self.updateDestination();

	def setYCoord(self, newYCoord, movementZoneList):

		if self.testZone(movementZoneList, self.x, newYCoord):

			self.y = newYCoord

			self.updateDestination();

	def updateDestination(self):

		self.destination = SDL_Rect(self.x, self.y, spriteSize, spriteSize);
	def updateSprite(self):

		if self.orientation == DirectionsResource.left:

			self.sprite = self.spriteResource.spriteLeft;

		else:

			self.sprite = self.spriteResource.spriteRight;

	def testZone(self, movementZoneList, newXCoord, newYCoord):

		finalx = newXCoord + spriteSize;
		finaly = newYCoord + spriteSize;

		for movementZone in movementZoneList:

			movementZone = movementZone.split(',');
			movementZone = [int(num) for num in movementZone];

			if newXCoord >= movementZone[0] and newYCoord >= movementZone[1] and finalx <= movementZone[2] and newYCoord >= movementZone[3] and finalx <= movementZone[4] and finaly <= movementZone[5] and newXCoord >= movementZone[6] and finaly <= movementZone[7]:

				return True;

		return False;

	def entityAI(self, player, movementZoneList):

		return;
