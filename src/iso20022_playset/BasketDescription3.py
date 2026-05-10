from . import base_types
from .ISINOct2015Identifier import ISINOct2015Identifier
from .FinancialInstrument58 import FinancialInstrument58

class BasketDescription3(base_types._BaseFieldType):

	__slots__ = ["_Indx", "_ISIN"]
	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indx', type=FinancialInstrument58, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
	))

