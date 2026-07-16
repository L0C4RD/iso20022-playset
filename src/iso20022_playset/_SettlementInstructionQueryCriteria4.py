# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationSearchCriteria2Choice
from . import ActiveCurrencyAndAmountRange3
from . import ActiveOrHistoricCurrencyCode
from . import CountryCode
from . import DateAndDateTimeSearch5Choice
from . import DeliveryReceiptType2Code
from . import PartyIdentification136
from . import PartyIdentification148
from . import PriorityNumeric4Choice
from . import QuantitySearch2Choice
from . import ReceiveDelivery1Code
from . import References83Choice
from . import Registration10Choice
from . import SecuritiesAccount19
from . import SecuritiesTransactionType48Choice
from . import SecurityIdentification19
from . import SettlementInstructionQueryStatus3
from . import SettlementParties78
from . import SettlementTransactionCondition34Choice
from . import SettlementTransactionCondition5Code
from . import SystemPartyIdentification8
from . import TradeTransactionCondition1Code
from . import YesNoIndicator

class SettlementInstructionQueryCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CntrptSttlmPties", "_CondlSctiesDlvry", "_CshAcct", "_CtryOfIsse", "_DlvrgSttlmPties", "_FctvSttlmDt", "_FinInstrmId", "_HldInd", "_IntnddSttlmDt", "_IssrCSD", "_MsgOrgtr", "_Pmt", "_PrtlSttlmInd", "_Prty", "_RcvgSttlmPties", "_Refs", "_SctiesMvmntTp", "_SctiesTxCond", "_SctiesTxTp", "_SfkpgAcct", "_SfkpgAcctOwnr", "_Sts", "_SttldAmt", "_SttldQty", "_SttlmAmt", "_SttlmCcy", "_SttlmQty", "_TradDt", "_TradTxCond"]
	@property
	def CntrptSttlmPties(self):
		return self._CntrptSttlmPties

	@CntrptSttlmPties.setter
	def CntrptSttlmPties(self, value):
		self._CntrptSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'CntrptSttlmPties', SettlementParties78, True)

	@CntrptSttlmPties.deleter
	def CntrptSttlmPties(self):
		del self._CntrptSttlmPties
		self._CntrptSttlmPties = base_types.UninitialisedField(self, 'CntrptSttlmPties', SettlementParties78, True)

	@property
	def CondlSctiesDlvry(self):
		return self._CondlSctiesDlvry

	@CondlSctiesDlvry.setter
	def CondlSctiesDlvry(self, value):
		self._CondlSctiesDlvry = value if value is not None else base_types.UninitialisedField(self, 'CondlSctiesDlvry', YesNoIndicator, False)

	@CondlSctiesDlvry.deleter
	def CondlSctiesDlvry(self):
		del self._CondlSctiesDlvry
		self._CondlSctiesDlvry = base_types.UninitialisedField(self, 'CondlSctiesDlvry', YesNoIndicator, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', AccountIdentificationSearchCriteria2Choice, True)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', AccountIdentificationSearchCriteria2Choice, True)

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, True)

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, True)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties78, True)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties78, True)

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTimeSearch5Choice, False)

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTimeSearch5Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, True)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, True)

	@property
	def HldInd(self):
		return self._HldInd

	@HldInd.setter
	def HldInd(self, value):
		self._HldInd = value if value is not None else base_types.UninitialisedField(self, 'HldInd', Registration10Choice, True)

	@HldInd.deleter
	def HldInd(self):
		del self._HldInd
		self._HldInd = base_types.UninitialisedField(self, 'HldInd', Registration10Choice, True)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTimeSearch5Choice, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTimeSearch5Choice, False)

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrCSD', PartyIdentification136, True)

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = base_types.UninitialisedField(self, 'IssrCSD', PartyIdentification136, True)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, True)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, True)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, True)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, True)

	@property
	def PrtlSttlmInd(self):
		return self._PrtlSttlmInd

	@PrtlSttlmInd.setter
	def PrtlSttlmInd(self, value):
		self._PrtlSttlmInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlmInd', SettlementTransactionCondition5Code, False)

	@PrtlSttlmInd.deleter
	def PrtlSttlmInd(self):
		del self._PrtlSttlmInd
		self._PrtlSttlmInd = base_types.UninitialisedField(self, 'PrtlSttlmInd', SettlementTransactionCondition5Code, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, True)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, True)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties78, True)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties78, True)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', References83Choice, True)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', References83Choice, True)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, True)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, True)

	@property
	def SctiesTxCond(self):
		return self._SctiesTxCond

	@SctiesTxCond.setter
	def SctiesTxCond(self, value):
		self._SctiesTxCond = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxCond', SettlementTransactionCondition34Choice, True)

	@SctiesTxCond.deleter
	def SctiesTxCond(self):
		del self._SctiesTxCond
		self._SctiesTxCond = base_types.UninitialisedField(self, 'SctiesTxCond', SettlementTransactionCondition34Choice, True)

	@property
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType48Choice, True)

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType48Choice, True)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, True)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, True)

	@property
	def SfkpgAcctOwnr(self):
		return self._SfkpgAcctOwnr

	@SfkpgAcctOwnr.setter
	def SfkpgAcctOwnr(self, value):
		self._SfkpgAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcctOwnr', PartyIdentification148, True)

	@SfkpgAcctOwnr.deleter
	def SfkpgAcctOwnr(self):
		del self._SfkpgAcctOwnr
		self._SfkpgAcctOwnr = base_types.UninitialisedField(self, 'SfkpgAcctOwnr', PartyIdentification148, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', SettlementInstructionQueryStatus3, True)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', SettlementInstructionQueryStatus3, True)

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if value is not None else base_types.UninitialisedField(self, 'SttldAmt', ActiveCurrencyAndAmountRange3, False)

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = base_types.UninitialisedField(self, 'SttldAmt', ActiveCurrencyAndAmountRange3, False)

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if value is not None else base_types.UninitialisedField(self, 'SttldQty', QuantitySearch2Choice, False)

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = base_types.UninitialisedField(self, 'SttldQty', QuantitySearch2Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmountRange3, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmountRange3, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveOrHistoricCurrencyCode, True)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveOrHistoricCurrencyCode, True)

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if value is not None else base_types.UninitialisedField(self, 'SttlmQty', QuantitySearch2Choice, False)

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = base_types.UninitialisedField(self, 'SttlmQty', QuantitySearch2Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', DateAndDateTimeSearch5Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', DateAndDateTimeSearch5Choice, False)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition1Code, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition1Code, True)

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