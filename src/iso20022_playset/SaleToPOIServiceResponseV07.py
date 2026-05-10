from . import base_types
from .ContentInformationType38 import ContentInformationType38
from .ServiceResponse9 import ServiceResponse9
from .Header41 import Header41

class SaleToPOIServiceResponseV07(base_types._BaseFieldType):

	__slots__ = ["_SvcRspn", "_Hdr", "_SctyTrlr"]
	@property
	def SvcRspn(self):
		return self._SvcRspn

	@SvcRspn.setter
	def SvcRspn(self, value):
		self._SvcRspn = value if type(value) != base_types.auto else self.make_default("SvcRspn")

	@SvcRspn.deleter
	def SvcRspn(self):
		del self._SvcRspn
		self._SvcRspn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcRspn', type=ServiceResponse9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
	))

