# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._InterestRecord2 import InterestRecord2

class TransactionInterest4(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_TtlIntrstAndTaxAmt"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != base_types.auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def TtlIntrstAndTaxAmt(self):
		return self._TtlIntrstAndTaxAmt

	@TtlIntrstAndTaxAmt.setter
	def TtlIntrstAndTaxAmt(self, value):
		self._TtlIntrstAndTaxAmt = value if type(value) != base_types.auto else self.make_default("TtlIntrstAndTaxAmt")

	@TtlIntrstAndTaxAmt.deleter
	def TtlIntrstAndTaxAmt(self):
		del self._TtlIntrstAndTaxAmt
		self._TtlIntrstAndTaxAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=InterestRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlIntrstAndTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))