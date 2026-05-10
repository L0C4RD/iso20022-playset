from . import base_types
from .HostToATMAcknowledgement1 import HostToATMAcknowledgement1
from .ContentInformationType10 import ContentInformationType10
from .ContentInformationType15 import ContentInformationType15
from .Header20 import Header20

class HostToATMAcknowledgementV01(base_types._BaseFieldType):

	__slots__ = ["_PrtctdHstToATMAck", "_Hdr", "_SctyTrlr", "_HstToATMAck"]
	@property
	def PrtctdHstToATMAck(self):
		return self._PrtctdHstToATMAck

	@PrtctdHstToATMAck.setter
	def PrtctdHstToATMAck(self, value):
		self._PrtctdHstToATMAck = value if type(value) != base_types.auto else self.make_default("PrtctdHstToATMAck")

	@PrtctdHstToATMAck.deleter
	def PrtctdHstToATMAck(self):
		del self._PrtctdHstToATMAck
		self._PrtctdHstToATMAck = None

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
	def HstToATMAck(self):
		return self._HstToATMAck

	@HstToATMAck.setter
	def HstToATMAck(self, value):
		self._HstToATMAck = value if type(value) != base_types.auto else self.make_default("HstToATMAck")

	@HstToATMAck.deleter
	def HstToATMAck(self):
		del self._HstToATMAck
		self._HstToATMAck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctdHstToATMAck', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstToATMAck', type=HostToATMAcknowledgement1, min=0, max=1, mutex_group=None, array=False),
	))

