# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import CashAccountIdentification5Choice
from . import DateAndDateTime2Choice
from . import DeliveryReceiptType2Code
from . import FailingStatus15Choice
from . import FinancialInstrumentQuantity1Choice
from . import ISODateTime
from . import PartyIdentification144
from . import PartyIdentification272
from . import ReceiveDelivery1Code
from . import SecuritiesAccount19
from . import SettlementDate17Choice
from . import SettlementOrCorporateActionEvent27Choice
from . import SystemEvent3

class PenaltyTransactionRecord2(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AckdStsTmStmp", "_BizDayEvt", "_CorpActnRltdDt", "_CshAcct", "_CshAcctOwnr", "_MtchdStsTmStmp", "_Pmt", "_PstngAmt", "_PstngQty", "_SctiesMvmntTp", "_SfkpgAcct", "_SttlmDt", "_SttlmStsFlng", "_SttlmTxOrCorpActnEvtTp"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if value is not None else base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@property
	def BizDayEvt(self):
		return self._BizDayEvt

	@BizDayEvt.setter
	def BizDayEvt(self, value):
		self._BizDayEvt = value if value is not None else base_types.UninitialisedField(self, 'BizDayEvt', SystemEvent3, False)

	@BizDayEvt.deleter
	def BizDayEvt(self):
		del self._BizDayEvt
		self._BizDayEvt = base_types.UninitialisedField(self, 'BizDayEvt', SystemEvent3, False)

	@property
	def CorpActnRltdDt(self):
		return self._CorpActnRltdDt

	@CorpActnRltdDt.setter
	def CorpActnRltdDt(self, value):
		self._CorpActnRltdDt = value if value is not None else base_types.UninitialisedField(self, 'CorpActnRltdDt', DateAndDateTime2Choice, False)

	@CorpActnRltdDt.deleter
	def CorpActnRltdDt(self):
		del self._CorpActnRltdDt
		self._CorpActnRltdDt = base_types.UninitialisedField(self, 'CorpActnRltdDt', DateAndDateTime2Choice, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification5Choice, False)

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CshAcctOwnr', PartyIdentification272, False)

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = base_types.UninitialisedField(self, 'CshAcctOwnr', PartyIdentification272, False)

	@property
	def MtchdStsTmStmp(self):
		return self._MtchdStsTmStmp

	@MtchdStsTmStmp.setter
	def MtchdStsTmStmp(self, value):
		self._MtchdStsTmStmp = value if value is not None else base_types.UninitialisedField(self, 'MtchdStsTmStmp', ISODateTime, False)

	@MtchdStsTmStmp.deleter
	def MtchdStsTmStmp(self):
		del self._MtchdStsTmStmp
		self._MtchdStsTmStmp = base_types.UninitialisedField(self, 'MtchdStsTmStmp', ISODateTime, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if value is not None else base_types.UninitialisedField(self, 'PstngAmt', AmountAndDirection5, False)

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = base_types.UninitialisedField(self, 'PstngAmt', AmountAndDirection5, False)

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if value is not None else base_types.UninitialisedField(self, 'PstngQty', FinancialInstrumentQuantity1Choice, False)

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = base_types.UninitialisedField(self, 'PstngQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@property
	def SttlmStsFlng(self):
		return self._SttlmStsFlng

	@SttlmStsFlng.setter
	def SttlmStsFlng(self, value):
		self._SttlmStsFlng = value if value is not None else base_types.UninitialisedField(self, 'SttlmStsFlng', FailingStatus15Choice, False)

	@SttlmStsFlng.deleter
	def SttlmStsFlng(self):
		del self._SttlmStsFlng
		self._SttlmStsFlng = base_types.UninitialisedField(self, 'SttlmStsFlng', FailingStatus15Choice, False)

	@property
	def SttlmTxOrCorpActnEvtTp(self):
		return self._SttlmTxOrCorpActnEvtTp

	@SttlmTxOrCorpActnEvtTp.setter
	def SttlmTxOrCorpActnEvtTp(self, value):
		self._SttlmTxOrCorpActnEvtTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmTxOrCorpActnEvtTp', SettlementOrCorporateActionEvent27Choice, False)

	@SttlmTxOrCorpActnEvtTp.deleter
	def SttlmTxOrCorpActnEvtTp(self):
		del self._SttlmTxOrCorpActnEvtTp
		self._SttlmTxOrCorpActnEvtTp = base_types.UninitialisedField(self, 'SttlmTxOrCorpActnEvtTp', SettlementOrCorporateActionEvent27Choice, False)

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