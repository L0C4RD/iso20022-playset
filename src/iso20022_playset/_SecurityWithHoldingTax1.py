from . import base_types
from ._RateAndAmountFormat1Choice import RateAndAmountFormat1Choice
from ._CountryCode import CountryCode

class SecurityWithHoldingTax1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_WhldgTaxVal"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def WhldgTaxVal(self):
		return self._WhldgTaxVal

	@WhldgTaxVal.setter
	def WhldgTaxVal(self, value):
		self._WhldgTaxVal = value if type(value) != base_types.auto else self.make_default("WhldgTaxVal")

	@WhldgTaxVal.deleter
	def WhldgTaxVal(self):
		del self._WhldgTaxVal
		self._WhldgTaxVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxVal', type=RateAndAmountFormat1Choice, min=1, max=1, mutex_group=None, array=False),
	))

