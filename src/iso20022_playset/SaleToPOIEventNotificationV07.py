from . import base_types
from .SystemEventNotification8 import SystemEventNotification8
from .ContentInformationType38 import ContentInformationType38
from .Header41 import Header41

class SaleToPOIEventNotificationV07(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_EvtNtfctn", "_Hdr"]
	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def EvtNtfctn(self):
		return self._EvtNtfctn

	@EvtNtfctn.setter
	def EvtNtfctn(self, value):
		self._EvtNtfctn = value if type(value) != base_types.auto else self.make_default("EvtNtfctn")

	@EvtNtfctn.deleter
	def EvtNtfctn(self):
		del self._EvtNtfctn
		self._EvtNtfctn = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtNtfctn', type=SystemEventNotification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
	))

