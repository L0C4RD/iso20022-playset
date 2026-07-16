# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOTime
from . import Max70Text
from . import NetworkParameters7

class ClockSynchronisation3(base_types._BaseFieldType):

	__slots__ = ["_Dely", "_POITmZone", "_SynctnSvr"]
	@property
	def Dely(self):
		return self._Dely

	@Dely.setter
	def Dely(self, value):
		self._Dely = value if value is not None else base_types.UninitialisedField(self, 'Dely', ISOTime, False)

	@Dely.deleter
	def Dely(self):
		del self._Dely
		self._Dely = base_types.UninitialisedField(self, 'Dely', ISOTime, False)

	@property
	def POITmZone(self):
		return self._POITmZone

	@POITmZone.setter
	def POITmZone(self, value):
		self._POITmZone = value if value is not None else base_types.UninitialisedField(self, 'POITmZone', Max70Text, False)

	@POITmZone.deleter
	def POITmZone(self):
		del self._POITmZone
		self._POITmZone = base_types.UninitialisedField(self, 'POITmZone', Max70Text, False)

	@property
	def SynctnSvr(self):
		return self._SynctnSvr

	@SynctnSvr.setter
	def SynctnSvr(self, value):
		self._SynctnSvr = value if value is not None else base_types.UninitialisedField(self, 'SynctnSvr', NetworkParameters7, True)

	@SynctnSvr.deleter
	def SynctnSvr(self):
		del self._SynctnSvr
		self._SynctnSvr = base_types.UninitialisedField(self, 'SynctnSvr', NetworkParameters7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dely', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITmZone', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SynctnSvr', type=NetworkParameters7, min=0, max=None, mutex_group=None, array=True),
	))