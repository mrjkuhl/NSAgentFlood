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
import sys
import importlib

from __init__ import *
import spriteresources

class EntityList():


	def __init__(self, stage, world):

		self.entityList = [];
		mobTypes = {};
		counter = 1;

		sys.path.append(world);

		while True:

			try:

				entityValues = stage.get('stage', "entity" + str(counter));
				entityValues = entityValues.split(',');

				entityClass = entityValues[9];
				entityValues.remove(entityClass);

				classObject = importlib.import_module(b"entities." + entityValues[8]);
				entityClass = getattr(classObject, entityClass);

				if entityValues[8] not in mobTypes:

					mobTypes[entityValues[8]] = spriteresources.SpriteResources(world, entityValues[8]);

				spriteResource = mobTypes[entityValues[8]];

				self.addEntity(entityClass, entityValues, spriteResource);

				counter += 1;

			except:

				break;

	def addEntity(self, entityClass, entityValues, spriteResource):

		self.entityList.append(entityClass(entityValues, spriteResource));

	def removeEntity(self, entity):

		self.entityList.remove(entity);
