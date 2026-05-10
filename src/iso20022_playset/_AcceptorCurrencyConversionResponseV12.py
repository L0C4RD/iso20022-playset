from . import base_types
from .ContentInformationType37 import ContentInformationType37
from .AcceptorCurrencyConversionResponse12 import AcceptorCurrencyConversionResponse12
from .Header70 import Header70

class AcceptorCurrencyConversionResponseV12(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_CcyConvsRspn", "_Hdr"]
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
	def CcyConvsRspn(self):
		return self._CcyConvsRspn

	@CcyConvsRspn.setter
	def CcyConvsRspn(self, value):
		self._CcyConvsRspn = value if type(value) != base_types.auto else self.make_default("CcyConvsRspn")

	@CcyConvsRspn.deleter
	def CcyConvsRspn(self):
		del self._CcyConvsRspn
		self._CcyConvsRspn = None

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
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsRspn', type=AcceptorCurrencyConversionResponse12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
	))

