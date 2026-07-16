# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import RateAndAmountFormat1Choice

class SecurityWithHoldingTax1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_WhldgTaxVal"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def WhldgTaxVal(self):
		return self._WhldgTaxVal

	@WhldgTaxVal.setter
	def WhldgTaxVal(self, value):
		self._WhldgTaxVal = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxVal', RateAndAmountFormat1Choice, False)

	@WhldgTaxVal.deleter
	def WhldgTaxVal(self):
		del self._WhldgTaxVal
		self._WhldgTaxVal = base_types.UninitialisedField(self, 'WhldgTaxVal', RateAndAmountFormat1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxVal', type=RateAndAmountFormat1Choice, min=1, max=1, mutex_group=None, array=False),
	))