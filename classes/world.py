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
import ConfigParser

from __init__ import *
from entitylist import EntityList
from movementzonelist import MovementZoneList

class World():

	def __init__(self, worldPath, renderer):

		self.worldPath = worldPath;
		self.renderer = renderer;

		self.changeLevel("level1");

		self.loadStageConf("stage1");
		self.changeStage();

	def changeLevel(self, level):

		self.level = level;

	def changeStage(self):

		self.movementZoneList = MovementZoneList(self.stage);
		self.entityList = EntityList(self.stage, self.worldPath);

		image = SDL_LoadBMP(self.worldPath + "resources/" + self.stage.get('stage', 'background'));
		self.background = SDL_CreateTextureFromSurface(self.renderer, image);
		SDL_FreeSurface(image);

	def loadStageConf(self, stage):

		confFile = self.worldPath + "/" + self.level + "/stages/" + stage + ".conf";

		filePointer = ConfigParser.RawConfigParser();
		filePointer.read(confFile);

		self.stage = filePointer;

	def gotoNextStage(self, direction):

		nextStage = self.getNextStage(direction);

		self.loadStageConf(nextStage);
		self.changeStage();

	def getNextStage(self, direction):

		nextStage = "stage" + direction.capitalize();
		nextStage = self.stage.get('stage', nextStage);

		return nextStage;
