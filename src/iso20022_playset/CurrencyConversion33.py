import base_types
import CurrencyConversion32
import CurrencyConversionResponse2Code
import Max35Text

class CurrencyConversion33(base_types._BaseFieldType):

	__slots__ = ["_Rslt", "_RsltRsn", "_Convs"]
	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def RsltRsn(self):
		return self._RsltRsn

	@RsltRsn.setter
	def RsltRsn(self, value):
		self._RsltRsn = value if type(value) != auto else self.make_default("RsltRsn")

	@RsltRsn.deleter
	def RsltRsn(self):
		del self._RsltRsn
		self._RsltRsn = None

	@property
	def Convs(self):
		return self._Convs

	@Convs.setter
	def Convs(self, value):
		self._Convs = value if type(value) != auto else self.make_default("Convs")

	@Convs.deleter
	def Convs(self):
		del self._Convs
		self._Convs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rslt', type=CurrencyConversionResponse2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Convs', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
	))

