from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CurrencyFactors1 import CurrencyFactors1

class PayInFactors1(base_types._BaseFieldType):

	__slots__ = ["_CcyFctrs", "_AggtShrtPosLmt"]
	@property
	def AggtShrtPosLmt(self):
		return self._AggtShrtPosLmt

	@AggtShrtPosLmt.setter
	def AggtShrtPosLmt(self, value):
		self._AggtShrtPosLmt = value if type(value) != base_types.auto else self.make_default("AggtShrtPosLmt")

	@AggtShrtPosLmt.deleter
	def AggtShrtPosLmt(self):
		del self._AggtShrtPosLmt
		self._AggtShrtPosLmt = None

	@property
	def CcyFctrs(self):
		return self._CcyFctrs

	@CcyFctrs.setter
	def CcyFctrs(self, value):
		self._CcyFctrs = value if type(value) != base_types.auto else self.make_default("CcyFctrs")

	@CcyFctrs.deleter
	def CcyFctrs(self):
		del self._CcyFctrs
		self._CcyFctrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtShrtPosLmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyFctrs', type=CurrencyFactors1, min=1, max=None, mutex_group=None, array=True),
	))

