from . import base_types
from ._Adjustment5 import Adjustment5
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISODate import ISODate

class InvoiceTotals1(base_types._BaseFieldType):

	__slots__ = ["_TtlInvcAmt", "_TtlTaxAmt", "_Adjstmnt", "_TtlTaxblAmt", "_PmtDueDt"]
	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if type(value) != base_types.auto else self.make_default("TtlInvcAmt")

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = None

	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if type(value) != base_types.auto else self.make_default("TtlTaxAmt")

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = None

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != base_types.auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

	@property
	def TtlTaxblAmt(self):
		return self._TtlTaxblAmt

	@TtlTaxblAmt.setter
	def TtlTaxblAmt(self, value):
		self._TtlTaxblAmt = value if type(value) != base_types.auto else self.make_default("TtlTaxblAmt")

	@TtlTaxblAmt.deleter
	def TtlTaxblAmt(self):
		del self._TtlTaxblAmt
		self._TtlTaxblAmt = None

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if type(value) != base_types.auto else self.make_default("PmtDueDt")

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlInvcAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

