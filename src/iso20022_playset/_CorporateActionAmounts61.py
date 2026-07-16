# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINActiveCurrencyAndAmount

class CorporateActionAmounts61(base_types._BaseFieldType):

	__slots__ = ["_ScndLvlTaxAmt", "_WhldgTaxAmt"]
	@property
	def ScndLvlTaxAmt(self):
		return self._ScndLvlTaxAmt

	@ScndLvlTaxAmt.setter
	def ScndLvlTaxAmt(self, value):
		self._ScndLvlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@ScndLvlTaxAmt.deleter
	def ScndLvlTaxAmt(self):
		del self._ScndLvlTaxAmt
		self._ScndLvlTaxAmt = base_types.UninitialisedField(self, 'ScndLvlTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@property
	def WhldgTaxAmt(self):
		return self._WhldgTaxAmt

	@WhldgTaxAmt.setter
	def WhldgTaxAmt(self, value):
		self._WhldgTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	@WhldgTaxAmt.deleter
	def WhldgTaxAmt(self):
		del self._WhldgTaxAmt
		self._WhldgTaxAmt = base_types.UninitialisedField(self, 'WhldgTaxAmt', RestrictedFINActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ScndLvlTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxAmt', type=RestrictedFINActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))