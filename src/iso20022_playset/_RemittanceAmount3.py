# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DiscountAmountAndType1
from . import DocumentAdjustment1
from . import TaxAmountAndType1

class RemittanceAmount3(base_types._BaseFieldType):

	__slots__ = ["_AdjstmntAmtAndRsn", "_CdtNoteAmt", "_DscntApldAmt", "_DuePyblAmt", "_RmtdAmt", "_TaxAmt"]
	@property
	def AdjstmntAmtAndRsn(self):
		return self._AdjstmntAmtAndRsn

	@AdjstmntAmtAndRsn.setter
	def AdjstmntAmtAndRsn(self, value):
		self._AdjstmntAmtAndRsn = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntAmtAndRsn', DocumentAdjustment1, True)

	@AdjstmntAmtAndRsn.deleter
	def AdjstmntAmtAndRsn(self):
		del self._AdjstmntAmtAndRsn
		self._AdjstmntAmtAndRsn = base_types.UninitialisedField(self, 'AdjstmntAmtAndRsn', DocumentAdjustment1, True)

	@property
	def CdtNoteAmt(self):
		return self._CdtNoteAmt

	@CdtNoteAmt.setter
	def CdtNoteAmt(self, value):
		self._CdtNoteAmt = value if value is not None else base_types.UninitialisedField(self, 'CdtNoteAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@CdtNoteAmt.deleter
	def CdtNoteAmt(self):
		del self._CdtNoteAmt
		self._CdtNoteAmt = base_types.UninitialisedField(self, 'CdtNoteAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def DscntApldAmt(self):
		return self._DscntApldAmt

	@DscntApldAmt.setter
	def DscntApldAmt(self, value):
		self._DscntApldAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntApldAmt', DiscountAmountAndType1, True)

	@DscntApldAmt.deleter
	def DscntApldAmt(self):
		del self._DscntApldAmt
		self._DscntApldAmt = base_types.UninitialisedField(self, 'DscntApldAmt', DiscountAmountAndType1, True)

	@property
	def DuePyblAmt(self):
		return self._DuePyblAmt

	@DuePyblAmt.setter
	def DuePyblAmt(self, value):
		self._DuePyblAmt = value if value is not None else base_types.UninitialisedField(self, 'DuePyblAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@DuePyblAmt.deleter
	def DuePyblAmt(self):
		del self._DuePyblAmt
		self._DuePyblAmt = base_types.UninitialisedField(self, 'DuePyblAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def RmtdAmt(self):
		return self._RmtdAmt

	@RmtdAmt.setter
	def RmtdAmt(self, value):
		self._RmtdAmt = value if value is not None else base_types.UninitialisedField(self, 'RmtdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@RmtdAmt.deleter
	def RmtdAmt(self):
		del self._RmtdAmt
		self._RmtdAmt = base_types.UninitialisedField(self, 'RmtdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxAmt', TaxAmountAndType1, True)

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = base_types.UninitialisedField(self, 'TaxAmt', TaxAmountAndType1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntAmtAndRsn', type=DocumentAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtNoteAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntApldAmt', type=DiscountAmountAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DuePyblAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=TaxAmountAndType1, min=0, max=None, mutex_group=None, array=True),
	))