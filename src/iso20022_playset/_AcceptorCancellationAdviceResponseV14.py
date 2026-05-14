from . import base_types
from ._AcceptorCancellationAdviceResponse14 import AcceptorCancellationAdviceResponse14
from ._ContentInformationType37 import ContentInformationType37
from ._Header70 import Header70

class AcceptorCancellationAdviceResponseV14(base_types._BaseFieldType):

	__slots__ = ["_CxlAdvcRspn", "_Hdr", "_SctyTrlr"]
	@property
	def CxlAdvcRspn(self):
		return self._CxlAdvcRspn

	@CxlAdvcRspn.setter
	def CxlAdvcRspn(self, value):
		self._CxlAdvcRspn = value if type(value) != base_types.auto else self.make_default("CxlAdvcRspn")

	@CxlAdvcRspn.deleter
	def CxlAdvcRspn(self):
		del self._CxlAdvcRspn
		self._CxlAdvcRspn = None

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
		base_types.FieldEntry(name='CxlAdvcRspn', type=AcceptorCancellationAdviceResponse14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))

