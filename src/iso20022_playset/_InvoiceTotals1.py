# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Adjustment5
from . import ISODate

class InvoiceTotals1(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_PmtDueDt", "_TtlInvcAmt", "_TtlTaxAmt", "_TtlTaxblAmt"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment5, False)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment5, False)

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDueDt', ISODate, False)

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = base_types.UninitialisedField(self, 'PmtDueDt', ISODate, False)

	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlInvcAmt', ActiveCurrencyAndAmount, False)

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = base_types.UninitialisedField(self, 'TtlInvcAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxAmt', ActiveCurrencyAndAmount, False)

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = base_types.UninitialisedField(self, 'TtlTaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlTaxblAmt(self):
		return self._TtlTaxblAmt

	@TtlTaxblAmt.setter
	def TtlTaxblAmt(self, value):
		self._TtlTaxblAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxblAmt', ActiveCurrencyAndAmount, False)

	@TtlTaxblAmt.deleter
	def TtlTaxblAmt(self):
		del self._TtlTaxblAmt
		self._TtlTaxblAmt = base_types.UninitialisedField(self, 'TtlTaxblAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInvcAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))