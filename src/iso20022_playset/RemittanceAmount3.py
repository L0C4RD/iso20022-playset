from . import base_types
from .DiscountAmountAndType1 import DiscountAmountAndType1
from .DocumentAdjustment1 import DocumentAdjustment1
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .TaxAmountAndType1 import TaxAmountAndType1

class RemittanceAmount3(base_types._BaseFieldType):

	__slots__ = ["_CdtNoteAmt", "_TaxAmt", "_DuePyblAmt", "_RmtdAmt", "_DscntApldAmt", "_AdjstmntAmtAndRsn"]
	@property
	def CdtNoteAmt(self):
		return self._CdtNoteAmt

	@CdtNoteAmt.setter
	def CdtNoteAmt(self, value):
		self._CdtNoteAmt = value if type(value) != auto else self.make_default("CdtNoteAmt")

	@CdtNoteAmt.deleter
	def CdtNoteAmt(self):
		del self._CdtNoteAmt
		self._CdtNoteAmt = None

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if type(value) != auto else self.make_default("TaxAmt")

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = None

	@property
	def DuePyblAmt(self):
		return self._DuePyblAmt

	@DuePyblAmt.setter
	def DuePyblAmt(self, value):
		self._DuePyblAmt = value if type(value) != auto else self.make_default("DuePyblAmt")

	@DuePyblAmt.deleter
	def DuePyblAmt(self):
		del self._DuePyblAmt
		self._DuePyblAmt = None

	@property
	def RmtdAmt(self):
		return self._RmtdAmt

	@RmtdAmt.setter
	def RmtdAmt(self, value):
		self._RmtdAmt = value if type(value) != auto else self.make_default("RmtdAmt")

	@RmtdAmt.deleter
	def RmtdAmt(self):
		del self._RmtdAmt
		self._RmtdAmt = None

	@property
	def DscntApldAmt(self):
		return self._DscntApldAmt

	@DscntApldAmt.setter
	def DscntApldAmt(self, value):
		self._DscntApldAmt = value if type(value) != auto else self.make_default("DscntApldAmt")

	@DscntApldAmt.deleter
	def DscntApldAmt(self):
		del self._DscntApldAmt
		self._DscntApldAmt = None

	@property
	def AdjstmntAmtAndRsn(self):
		return self._AdjstmntAmtAndRsn

	@AdjstmntAmtAndRsn.setter
	def AdjstmntAmtAndRsn(self, value):
		self._AdjstmntAmtAndRsn = value if type(value) != auto else self.make_default("AdjstmntAmtAndRsn")

	@AdjstmntAmtAndRsn.deleter
	def AdjstmntAmtAndRsn(self):
		del self._AdjstmntAmtAndRsn
		self._AdjstmntAmtAndRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtNoteAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=TaxAmountAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DuePyblAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntApldAmt', type=DiscountAmountAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdjstmntAmtAndRsn', type=DocumentAdjustment1, min=0, max=None, mutex_group=None, array=True),
	))

