from . import base_types
from ._BlockChainAddressWallet14 import BlockChainAddressWallet14
from ._Cheque10 import Cheque10
from ._CreditTransfer12 import CreditTransfer12
from ._DirectDebitMandate9 import DirectDebitMandate9
from ._InvestmentAccount60 import InvestmentAccount60
from ._PaymentCard34 import PaymentCard34

class PaymentInstrument29Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_BlckChainCshWllt", "_CdtTrfDtls", "_ChqDtls", "_CshAcctDtls", "_DrctDbtDtls", "_PmtCardDtls"]
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
	def BlckChainCshWllt(self):
		return self._BlckChainCshWllt

	@BlckChainCshWllt.setter
	def BlckChainCshWllt(self, value):
		self._BlckChainCshWllt = value if type(value) != base_types.auto else self.make_default("BlckChainCshWllt")

	@BlckChainCshWllt.deleter
	def BlckChainCshWllt(self):
		del self._BlckChainCshWllt
		self._BlckChainCshWllt = None

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
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if type(value) != base_types.auto else self.make_default("PmtCardDtls")

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BlckChainCshWllt', type=BlockChainAddressWallet14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcctDtls', type=InvestmentAccount60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard34, min=0, max=1, mutex_group=1, array=False),
	))

