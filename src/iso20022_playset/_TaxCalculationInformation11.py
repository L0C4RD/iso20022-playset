# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import TaxBasis1Choice

class TaxCalculationInformation11(base_types._BaseFieldType):

	__slots__ = ["_Bsis", "_TaxblAmt"]
	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if value is not None else base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	@property
	def TaxblAmt(self):
		return self._TaxblAmt

	@TaxblAmt.setter
	def TaxblAmt(self, value):
		self._TaxblAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxblAmt', ActiveCurrencyAndAmount, False)

	@TaxblAmt.deleter
	def TaxblAmt(self):
		del self._TaxblAmt
		self._TaxblAmt = base_types.UninitialisedField(self, 'TaxblAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))