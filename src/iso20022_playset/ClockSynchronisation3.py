from . import base_types
from .NetworkParameters7 import NetworkParameters7
from .ISOTime import ISOTime
from .Max70Text import Max70Text

class ClockSynchronisation3(base_types._BaseFieldType):

	__slots__ = ["_Dely", "_POITmZone", "_SynctnSvr"]
	@property
	def Dely(self):
		return self._Dely

	@Dely.setter
	def Dely(self, value):
		self._Dely = value if type(value) != base_types.auto else self.make_default("Dely")

	@Dely.deleter
	def Dely(self):
		del self._Dely
		self._Dely = None

	@property
	def POITmZone(self):
		return self._POITmZone

	@POITmZone.setter
	def POITmZone(self, value):
		self._POITmZone = value if type(value) != base_types.auto else self.make_default("POITmZone")

	@POITmZone.deleter
	def POITmZone(self):
		del self._POITmZone
		self._POITmZone = None

	@property
	def SynctnSvr(self):
		return self._SynctnSvr

	@SynctnSvr.setter
	def SynctnSvr(self, value):
		self._SynctnSvr = value if type(value) != base_types.auto else self.make_default("SynctnSvr")

	@SynctnSvr.deleter
	def SynctnSvr(self):
		del self._SynctnSvr
		self._SynctnSvr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dely', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITmZone', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SynctnSvr', type=NetworkParameters7, min=0, max=None, mutex_group=None, array=True),
	))

