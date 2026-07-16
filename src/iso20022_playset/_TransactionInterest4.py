# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import InterestRecord2

class TransactionInterest4(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_TtlIntrstAndTaxAmt"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', InterestRecord2, True)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', InterestRecord2, True)

	@property
	def TtlIntrstAndTaxAmt(self):
		return self._TtlIntrstAndTaxAmt

	@TtlIntrstAndTaxAmt.setter
	def TtlIntrstAndTaxAmt(self, value):
		self._TtlIntrstAndTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlIntrstAndTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlIntrstAndTaxAmt.deleter
	def TtlIntrstAndTaxAmt(self):
		del self._TtlIntrstAndTaxAmt
		self._TtlIntrstAndTaxAmt = base_types.UninitialisedField(self, 'TtlIntrstAndTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=InterestRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlIntrstAndTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))