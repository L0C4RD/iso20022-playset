from . import base_types
from ._CreditTransfer10 import CreditTransfer10
from ._InvestmentAccount60 import InvestmentAccount60
from ._DirectDebitMandate8 import DirectDebitMandate8
from ._Cheque21 import Cheque21
from ._PaymentCard34 import PaymentCard34

class PaymentInstrument27Choice(base_types._BaseFieldType):

	__slots__ = ["_PmtCardDtls", "_CshAcctDtls", "_ChqDtls", "_DrctDbtDtls", "_BkrsDrftDtls", "_CdtTrfDtls"]
	@property
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if type(value) != base_types.auto else self.make_default("PmtCardDtls")

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = None

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != base_types.auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if type(value) != base_types.auto else self.make_default("ChqDtls")

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = None

	@property
	def DrctDbtDtls(self):
		return self._DrctDbtDtls

	@DrctDbtDtls.setter
	def DrctDbtDtls(self, value):
		self._DrctDbtDtls = value if type(value) != base_types.auto else self.make_default("DrctDbtDtls")

	@DrctDbtDtls.deleter
	def DrctDbtDtls(self):
		del self._DrctDbtDtls
		self._DrctDbtDtls = None

	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if type(value) != base_types.auto else self.make_default("BkrsDrftDtls")

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = None

	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if type(value) != base_types.auto else self.make_default("CdtTrfDtls")

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard34, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer10, min=0, max=1, mutex_group=1, array=False),
	))

