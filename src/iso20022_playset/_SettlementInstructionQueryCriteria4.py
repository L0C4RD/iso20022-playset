from . import base_types
from ._AccountIdentificationSearchCriteria2Choice import AccountIdentificationSearchCriteria2Choice
from ._ActiveCurrencyAndAmountRange3 import ActiveCurrencyAndAmountRange3
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CountryCode import CountryCode
from ._DateAndDateTimeSearch5Choice import DateAndDateTimeSearch5Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._PartyIdentification136 import PartyIdentification136
from ._PartyIdentification148 import PartyIdentification148
from ._PriorityNumeric4Choice import PriorityNumeric4Choice
from ._QuantitySearch2Choice import QuantitySearch2Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._References83Choice import References83Choice
from ._Registration10Choice import Registration10Choice
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecuritiesTransactionType48Choice import SecuritiesTransactionType48Choice
from ._SecurityIdentification19 import SecurityIdentification19
from ._SettlementInstructionQueryStatus3 import SettlementInstructionQueryStatus3
from ._SettlementParties78 import SettlementParties78
from ._SettlementTransactionCondition34Choice import SettlementTransactionCondition34Choice
from ._SettlementTransactionCondition5Code import SettlementTransactionCondition5Code
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._TradeTransactionCondition1Code import TradeTransactionCondition1Code
from ._YesNoIndicator import YesNoIndicator

class SettlementInstructionQueryCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CntrptSttlmPties", "_CondlSctiesDlvry", "_CshAcct", "_CtryOfIsse", "_DlvrgSttlmPties", "_FctvSttlmDt", "_FinInstrmId", "_HldInd", "_IntnddSttlmDt", "_IssrCSD", "_MsgOrgtr", "_Pmt", "_PrtlSttlmInd", "_Prty", "_RcvgSttlmPties", "_Refs", "_SctiesMvmntTp", "_SctiesTxCond", "_SctiesTxTp", "_SfkpgAcct", "_SfkpgAcctOwnr", "_Sts", "_SttldAmt", "_SttldQty", "_SttlmAmt", "_SttlmCcy", "_SttlmQty", "_TradDt", "_TradTxCond"]
	@property
	def CntrptSttlmPties(self):
		return self._CntrptSttlmPties

	@CntrptSttlmPties.setter
	def CntrptSttlmPties(self, value):
		self._CntrptSttlmPties = value if type(value) != base_types.auto else self.make_default("CntrptSttlmPties")

	@CntrptSttlmPties.deleter
	def CntrptSttlmPties(self):
		del self._CntrptSttlmPties
		self._CntrptSttlmPties = None

	@property
	def CondlSctiesDlvry(self):
		return self._CondlSctiesDlvry

	@CondlSctiesDlvry.setter
	def CondlSctiesDlvry(self, value):
		self._CondlSctiesDlvry = value if type(value) != base_types.auto else self.make_default("CondlSctiesDlvry")

	@CondlSctiesDlvry.deleter
	def CondlSctiesDlvry(self):
		del self._CondlSctiesDlvry
		self._CondlSctiesDlvry = None

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
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if type(value) != base_types.auto else self.make_default("CtryOfIsse")

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != base_types.auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if type(value) != base_types.auto else self.make_default("HldInd")

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = None

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if type(value) != base_types.auto else self.make_default("IntnddSttlmDt")

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = None

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != base_types.auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if type(value) != base_types.auto else self.make_default("MsgOrgtr")

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = None

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
	def PrtlSttlmInd(self):
		return self._PrtlSttlmInd

	@PrtlSttlmInd.setter
	def PrtlSttlmInd(self, value):
		self._PrtlSttlmInd = value if type(value) != base_types.auto else self.make_default("PrtlSttlmInd")

	@PrtlSttlmInd.deleter
	def PrtlSttlmInd(self):
		del self._PrtlSttlmInd
		self._PrtlSttlmInd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

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
	def SctiesTxCond(self):
		return self._SctiesTxCond

	@SctiesTxCond.setter
	def SctiesTxCond(self, value):
		self._SctiesTxCond = value if type(value) != base_types.auto else self.make_default("SctiesTxCond")

	@SctiesTxCond.deleter
	def SctiesTxCond(self):
		del self._SctiesTxCond
		self._SctiesTxCond = None

	@property
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if type(value) != base_types.auto else self.make_default("SctiesTxTp")

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = None

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
	def SfkpgAcctOwnr(self):
		return self._SfkpgAcctOwnr

	@SfkpgAcctOwnr.setter
	def SfkpgAcctOwnr(self, value):
		self._SfkpgAcctOwnr = value if type(value) != base_types.auto else self.make_default("SfkpgAcctOwnr")

	@SfkpgAcctOwnr.deleter
	def SfkpgAcctOwnr(self):
		del self._SfkpgAcctOwnr
		self._SfkpgAcctOwnr = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if type(value) != base_types.auto else self.make_default("SttldAmt")

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = None

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if type(value) != base_types.auto else self.make_default("SttldQty")

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != base_types.auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrptSttlmPties', type=SettlementParties78, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CondlSctiesDlvry', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties78, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HldInd', type=Registration10Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=PartyIdentification136, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlSttlmInd', type=SettlementTransactionCondition5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties78, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Refs', type=References83Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesTxCond', type=SettlementTransactionCondition34Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType48Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcctOwnr', type=PartyIdentification148, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=SettlementInstructionQueryStatus3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttldAmt', type=ActiveCurrencyAndAmountRange3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=QuantitySearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmountRange3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmQty', type=QuantitySearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition1Code, min=0, max=None, mutex_group=None, array=True),
	))

