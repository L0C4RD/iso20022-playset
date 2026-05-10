from . import base_types
from .ContentInformationType38 import ContentInformationType38
from .Header41 import Header41
from .SystemAbort8 import SystemAbort8

class SaleToPOIAbortV07(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_Abrt"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def Abrt(self):
		return self._Abrt

	@Abrt.setter
	def Abrt(self, value):
		self._Abrt = value if type(value) != auto else self.make_default("Abrt")

	@Abrt.deleter
	def Abrt(self):
		del self._Abrt
		self._Abrt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Abrt', type=SystemAbort8, min=1, max=1, mutex_group=None, array=False),
	))

