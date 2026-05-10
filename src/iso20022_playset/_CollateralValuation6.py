from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISINOct2015Identifier import ISINOct2015Identifier

class CollateralValuation6(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_NmnlAmt"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def NmnlAmt(self):
		return self._NmnlAmt

	@NmnlAmt.setter
	def NmnlAmt(self, value):
		self._NmnlAmt = value if type(value) != base_types.auto else self.make_default("NmnlAmt")

	@NmnlAmt.deleter
	def NmnlAmt(self):
		del self._NmnlAmt
		self._NmnlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

