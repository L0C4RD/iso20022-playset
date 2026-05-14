from . import base_types
from ._AmountAndDirection5 import AmountAndDirection5
from ._CashAccountIdentification5Choice import CashAccountIdentification5Choice
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._FailingStatus15Choice import FailingStatus15Choice
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._ISODateTime import ISODateTime
from ._PartyIdentification144 import PartyIdentification144
from ._PartyIdentification272 import PartyIdentification272
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SettlementDate17Choice import SettlementDate17Choice
from ._SettlementOrCorporateActionEvent27Choice import SettlementOrCorporateActionEvent27Choice
from ._SystemEvent3 import SystemEvent3

class PenaltyTransactionRecord2(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AckdStsTmStmp", "_BizDayEvt", "_CorpActnRltdDt", "_CshAcct", "_CshAcctOwnr", "_MtchdStsTmStmp", "_Pmt", "_PstngAmt", "_PstngQty", "_SctiesMvmntTp", "_SfkpgAcct", "_SttlmDt", "_SttlmStsFlng", "_SttlmTxOrCorpActnEvtTp"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if type(value) != base_types.auto else self.make_default("AckdStsTmStmp")

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = None

	@property
	def BizDayEvt(self):
		return self._BizDayEvt

	@BizDayEvt.setter
	def BizDayEvt(self, value):
		self._BizDayEvt = value if type(value) != base_types.auto else self.make_default("BizDayEvt")

	@BizDayEvt.deleter
	def BizDayEvt(self):
		del self._BizDayEvt
		self._BizDayEvt = None

	@property
	def CorpActnRltdDt(self):
		return self._CorpActnRltdDt

	@CorpActnRltdDt.setter
	def CorpActnRltdDt(self, value):
		self._CorpActnRltdDt = value if type(value) != base_types.auto else self.make_default("CorpActnRltdDt")

	@CorpActnRltdDt.deleter
	def CorpActnRltdDt(self):
		del self._CorpActnRltdDt
		self._CorpActnRltdDt = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def MtchdStsTmStmp(self):
		return self._MtchdStsTmStmp

	@MtchdStsTmStmp.setter
	def MtchdStsTmStmp(self, value):
		self._MtchdStsTmStmp = value if type(value) != base_types.auto else self.make_default("MtchdStsTmStmp")

	@MtchdStsTmStmp.deleter
	def MtchdStsTmStmp(self):
		del self._MtchdStsTmStmp
		self._MtchdStsTmStmp = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if type(value) != base_types.auto else self.make_default("PstngAmt")

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = None

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if type(value) != base_types.auto else self.make_default("PstngQty")

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != base_types.auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def SttlmStsFlng(self):
		return self._SttlmStsFlng

	@SttlmStsFlng.setter
	def SttlmStsFlng(self, value):
		self._SttlmStsFlng = value if type(value) != base_types.auto else self.make_default("SttlmStsFlng")

	@SttlmStsFlng.deleter
	def SttlmStsFlng(self):
		del self._SttlmStsFlng
		self._SttlmStsFlng = None

	@property
	def SttlmTxOrCorpActnEvtTp(self):
		return self._SttlmTxOrCorpActnEvtTp

	@SttlmTxOrCorpActnEvtTp.setter
	def SttlmTxOrCorpActnEvtTp(self, value):
		self._SttlmTxOrCorpActnEvtTp = value if type(value) != base_types.auto else self.make_default("SttlmTxOrCorpActnEvtTp")

	@SttlmTxOrCorpActnEvtTp.deleter
	def SttlmTxOrCorpActnEvtTp(self):
		del self._SttlmTxOrCorpActnEvtTp
		self._SttlmTxOrCorpActnEvtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizDayEvt', type=SystemEvent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnRltdDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStsFlng', type=FailingStatus15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxOrCorpActnEvtTp', type=SettlementOrCorporateActionEvent27Choice, min=1, max=1, mutex_group=None, array=False),
	))

