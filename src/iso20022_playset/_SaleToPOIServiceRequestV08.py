from . import base_types
from ._ContentInformationType38 import ContentInformationType38
from ._Header41 import Header41
from ._ServiceRequest9 import ServiceRequest9

class SaleToPOIServiceRequestV08(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_SvcReq"]
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
	def SvcReq(self):
		return self._SvcReq

	@SvcReq.setter
	def SvcReq(self, value):
		self._SvcReq = value if type(value) != base_types.auto else self.make_default("SvcReq")

	@SvcReq.deleter
	def SvcReq(self):
		del self._SvcReq
		self._SvcReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcReq', type=ServiceRequest9, min=1, max=1, mutex_group=None, array=False),
	))

