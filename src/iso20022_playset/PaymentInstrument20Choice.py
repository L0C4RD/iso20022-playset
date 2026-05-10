import base_types
import PaymentCard25
import Cheque9
import CreditTransfer8
import InvestmentAccount60
import DirectDebitMandate6

class PaymentInstrument20Choice(base_types._BaseFieldType):

	__slots__ = ["_PmtCardDtls", "_CshAcctDtls", "_BkrsDrftDtls", "_CdtTrfDtls", "_ChqDtls", "_DrctDbtDtls"]
	@property
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if type(value) != auto else self.make_default("PmtCardDtls")

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = None

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if type(value) != auto else self.make_default("BkrsDrftDtls")

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = None

	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if type(value) != auto else self.make_default("CdtTrfDtls")

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = None

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if type(value) != auto else self.make_default("ChqDtls")

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = None

	@property
	def DrctDbtDtls(self):
		return self._DrctDbtDtls

	@DrctDbtDtls.setter
	def DrctDbtDtls(self, value):
		self._DrctDbtDtls = value if type(value) != auto else self.make_default("DrctDbtDtls")

	@DrctDbtDtls.deleter
	def DrctDbtDtls(self):
		del self._DrctDbtDtls
		self._DrctDbtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard25, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate6, min=0, max=1, mutex_group=1, array=False),
	))

