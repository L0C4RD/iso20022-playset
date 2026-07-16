# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Cheque9
from . import CreditTransfer8
from . import DirectDebitMandate6
from . import InvestmentAccount60
from . import PaymentCard25

class PaymentInstrument20Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_CdtTrfDtls", "_ChqDtls", "_CshAcctDtls", "_DrctDbtDtls", "_PmtCardDtls"]
	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if value is not None else base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque9, False)

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque9, False)

	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer8, False)

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer8, False)

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if value is not None else base_types.UninitialisedField(self, 'ChqDtls', Cheque9, False)

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = base_types.UninitialisedField(self, 'ChqDtls', Cheque9, False)

	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'CshAcctDtls', InvestmentAccount60, False)

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = base_types.UninitialisedField(self, 'CshAcctDtls', InvestmentAccount60, False)

	@property
	def DrctDbtDtls(self):
		return self._DrctDbtDtls

	@DrctDbtDtls.setter
	def DrctDbtDtls(self, value):
		self._DrctDbtDtls = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate6, False)

	@DrctDbtDtls.deleter
	def DrctDbtDtls(self):
		del self._DrctDbtDtls
		self._DrctDbtDtls = base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate6, False)

	@property
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard25, False)

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard25, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard25, min=0, max=1, mutex_group=1, array=False),
	))