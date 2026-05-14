from . import base_types
from ._CurrencyConversion34 import CurrencyConversion34
from ._CurrencyConversionResponse3Code import CurrencyConversionResponse3Code
from ._Max35Text import Max35Text

class CurrencyConversion36(base_types._BaseFieldType):

	__slots__ = ["_ConvsDtls", "_Rslt", "_RsltRsn"]
	@property
	def ConvsDtls(self):
		return self._ConvsDtls

	@ConvsDtls.setter
	def ConvsDtls(self, value):
		self._ConvsDtls = value if type(value) != base_types.auto else self.make_default("ConvsDtls")

	@ConvsDtls.deleter
	def ConvsDtls(self):
		del self._ConvsDtls
		self._ConvsDtls = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def RsltRsn(self):
		return self._RsltRsn

	@RsltRsn.setter
	def RsltRsn(self, value):
		self._RsltRsn = value if type(value) != base_types.auto else self.make_default("RsltRsn")

	@RsltRsn.deleter
	def RsltRsn(self):
		del self._RsltRsn
		self._RsltRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConvsDtls', type=CurrencyConversion34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rslt', type=CurrencyConversionResponse3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

