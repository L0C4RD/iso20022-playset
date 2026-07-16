# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet14
from . import Cheque10
from . import CreditTransfer12
from . import DirectDebitMandate9
from . import InvestmentAccount60
from . import PaymentCard34

class PaymentInstrument29Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_BlckChainCshWllt", "_CdtTrfDtls", "_ChqDtls", "_CshAcctDtls", "_DrctDbtDtls", "_PmtCardDtls"]
	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if value is not None else base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque10, False)

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque10, False)

	@property
	def BlckChainCshWllt(self):
		return self._BlckChainCshWllt

	@BlckChainCshWllt.setter
	def BlckChainCshWllt(self, value):
		self._BlckChainCshWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainCshWllt', BlockChainAddressWallet14, False)

	@BlckChainCshWllt.deleter
	def BlckChainCshWllt(self):
		del self._BlckChainCshWllt
		self._BlckChainCshWllt = base_types.UninitialisedField(self, 'BlckChainCshWllt', BlockChainAddressWallet14, False)

	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer12, False)

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer12, False)

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if value is not None else base_types.UninitialisedField(self, 'ChqDtls', Cheque10, False)

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = base_types.UninitialisedField(self, 'ChqDtls', Cheque10, False)

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
		self._DrctDbtDtls = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate9, False)

	@DrctDbtDtls.deleter
	def DrctDbtDtls(self):
		del self._DrctDbtDtls
		self._DrctDbtDtls = base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate9, False)

	@property
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard34, False)

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BlckChainCshWllt', type=BlockChainAddressWallet14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard34, min=0, max=1, mutex_group=1, array=False),
	))