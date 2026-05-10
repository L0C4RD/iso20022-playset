from . import base_types
from ._Header70 import Header70
from ._AcceptorCurrencyConversionRequest12 import AcceptorCurrencyConversionRequest12
from ._ContentInformationType37 import ContentInformationType37

class AcceptorCurrencyConversionRequestV12(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_Hdr", "_CcyConvsReq"]
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
	def CcyConvsReq(self):
		return self._CcyConvsReq

	@CcyConvsReq.setter
	def CcyConvsReq(self, value):
		self._CcyConvsReq = value if type(value) != base_types.auto else self.make_default("CcyConvsReq")

	@CcyConvsReq.deleter
	def CcyConvsReq(self):
		del self._CcyConvsReq
		self._CcyConvsReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsReq', type=AcceptorCurrencyConversionRequest12, min=1, max=1, mutex_group=None, array=False),
	))

