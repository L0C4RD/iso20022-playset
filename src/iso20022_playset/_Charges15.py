# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ChargesRecord8

class Charges15(base_types._BaseFieldType):

	__slots__ = ["_Rcrd", "_TtlChrgsAndTaxAmt"]
	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', ChargesRecord8, True)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', ChargesRecord8, True)

	@property
	def TtlChrgsAndTaxAmt(self):
		return self._TtlChrgsAndTaxAmt

	@TtlChrgsAndTaxAmt.setter
	def TtlChrgsAndTaxAmt(self, value):
		self._TtlChrgsAndTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlChrgsAndTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlChrgsAndTaxAmt.deleter
	def TtlChrgsAndTaxAmt(self):
		del self._TtlChrgsAndTaxAmt
		self._TtlChrgsAndTaxAmt = base_types.UninitialisedField(self, 'TtlChrgsAndTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rcrd', type=ChargesRecord8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlChrgsAndTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))