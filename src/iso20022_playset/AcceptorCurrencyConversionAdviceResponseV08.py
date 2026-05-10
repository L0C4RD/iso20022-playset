from . import base_types
import ContentInformationType37
import AcceptorCancellationAdviceResponse13
import Header70

class AcceptorCurrencyConversionAdviceResponseV08(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_Hdr", "_CcyConvsAdvcRspn"]
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
	def CcyConvsAdvcRspn(self):
		return self._CcyConvsAdvcRspn

	@CcyConvsAdvcRspn.setter
	def CcyConvsAdvcRspn(self, value):
		self._CcyConvsAdvcRspn = value if type(value) != auto else self.make_default("CcyConvsAdvcRspn")

	@CcyConvsAdvcRspn.deleter
	def CcyConvsAdvcRspn(self):
		del self._CcyConvsAdvcRspn
		self._CcyConvsAdvcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsAdvcRspn', type=AcceptorCancellationAdviceResponse13, min=1, max=1, mutex_group=None, array=False),
	))

