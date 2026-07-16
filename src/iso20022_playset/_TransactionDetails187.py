# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection20
from . import CountryCode
from . import DateAndDateTime2Choice
from . import DeliveryReceiptType2Code
from . import FinancialInstrumentQuantity1Choice
from . import ISODateTime
from . import Linkages57
from . import Max350Text
from . import Max3Number
from . import PlaceOfClearingIdentification2
from . import PlaceOfTradeIdentification1
from . import PriorityNumeric4Choice
from . import ReceiveDelivery1Code
from . import SafeKeepingPlace3
from . import SecurityIdentification19
from . import SettlementDate19Choice
from . import SettlementDetails235
from . import SettlementOrCorporateActionEvent26Choice
from . import SettlementParties78
from . import SupplementaryData1
from . import SystemPartyIdentification8
from . import TradeDate8Choice
from . import TransactionActivity3Choice
from . import YesNoIndicator

class TransactionDetails187(base_types._BaseFieldType):

	__slots__ = ["_AckdStsTmStmp", "_AcrdIntrstAmt", "_CondlSctiesDlvry", "_CreDtTm", "_CtryOfIsse", "_DlvrgSttlmPties", "_FctvSttlmDt", "_FinInstrmId", "_IntnddSttlmDt", "_Lnkgs", "_MsgOrgtr", "_MtchdStsTmStmp", "_NbOfDaysAcrd", "_PlcOfClr", "_PlcOfTrad", "_Pmt", "_PrevslySttldAmt", "_PrevslySttldQty", "_Prty", "_RcvgSttlmPties", "_RmngSttlmAmt", "_RmngToBeSttldQty", "_RvslInd", "_SctiesMvmntTp", "_SfkpgPlc", "_SplmtryData", "_StsDt", "_SttldAmt", "_SttldQty", "_SttlmAmt", "_SttlmParams", "_SttlmQty", "_SttlmTxOrCorpActnEvtTp", "_TradDt", "_TxActvty", "_TxAddtlDtls", "_ValDt"]
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
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection20, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection20, False)

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
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties78, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties78, False)

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', SettlementDate19Choice, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', SettlementDate19Choice, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

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
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if value is not None else base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

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
	def PrevslySttldAmt(self):
		return self._PrevslySttldAmt

	@PrevslySttldAmt.setter
	def PrevslySttldAmt(self, value):
		self._PrevslySttldAmt = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldAmt', AmountAndDirection20, False)

	@PrevslySttldAmt.deleter
	def PrevslySttldAmt(self):
		del self._PrevslySttldAmt
		self._PrevslySttldAmt = base_types.UninitialisedField(self, 'PrevslySttldAmt', AmountAndDirection20, False)

	@property
	def PrevslySttldQty(self):
		return self._PrevslySttldQty

	@PrevslySttldQty.setter
	def PrevslySttldQty(self, value):
		self._PrevslySttldQty = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity1Choice, False)

	@PrevslySttldQty.deleter
	def PrevslySttldQty(self):
		del self._PrevslySttldQty
		self._PrevslySttldQty = base_types.UninitialisedField(self, 'PrevslySttldQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties78, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties78, False)

	@property
	def RmngSttlmAmt(self):
		return self._RmngSttlmAmt

	@RmngSttlmAmt.setter
	def RmngSttlmAmt(self, value):
		self._RmngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngSttlmAmt', AmountAndDirection20, False)

	@RmngSttlmAmt.deleter
	def RmngSttlmAmt(self):
		del self._RmngSttlmAmt
		self._RmngSttlmAmt = base_types.UninitialisedField(self, 'RmngSttlmAmt', AmountAndDirection20, False)

	@property
	def RmngToBeSttldQty(self):
		return self._RmngToBeSttldQty

	@RmngToBeSttldQty.setter
	def RmngToBeSttldQty(self, value):
		self._RmngToBeSttldQty = value if value is not None else base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity1Choice, False)

	@RmngToBeSttldQty.deleter
	def RmngToBeSttldQty(self):
		del self._RmngToBeSttldQty
		self._RmngToBeSttldQty = base_types.UninitialisedField(self, 'RmngToBeSttldQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def RvslInd(self):
		return self._RvslInd

	@RvslInd.setter
	def RvslInd(self, value):
		self._RvslInd = value if value is not None else base_types.UninitialisedField(self, 'RvslInd', YesNoIndicator, False)

	@RvslInd.deleter
	def RvslInd(self):
		del self._RvslInd
		self._RvslInd = base_types.UninitialisedField(self, 'RvslInd', YesNoIndicator, False)

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
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace3, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace3, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if value is not None else base_types.UninitialisedField(self, 'SttldAmt', AmountAndDirection20, False)

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = base_types.UninitialisedField(self, 'SttldAmt', AmountAndDirection20, False)

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if value is not None else base_types.UninitialisedField(self, 'SttldQty', FinancialInstrumentQuantity1Choice, False)

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = base_types.UninitialisedField(self, 'SttldQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection20, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection20, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails235, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails235, False)

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if value is not None else base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def SttlmTxOrCorpActnEvtTp(self):
		return self._SttlmTxOrCorpActnEvtTp

	@SttlmTxOrCorpActnEvtTp.setter
	def SttlmTxOrCorpActnEvtTp(self, value):
		self._SttlmTxOrCorpActnEvtTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmTxOrCorpActnEvtTp', SettlementOrCorporateActionEvent26Choice, False)

	@SttlmTxOrCorpActnEvtTp.deleter
	def SttlmTxOrCorpActnEvtTp(self):
		del self._SttlmTxOrCorpActnEvtTp
		self._SttlmTxOrCorpActnEvtTp = base_types.UninitialisedField(self, 'SttlmTxOrCorpActnEvtTp', SettlementOrCorporateActionEvent26Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@property
	def TxActvty(self):
		return self._TxActvty

	@TxActvty.setter
	def TxActvty(self, value):
		self._TxActvty = value if value is not None else base_types.UninitialisedField(self, 'TxActvty', TransactionActivity3Choice, False)

	@TxActvty.deleter
	def TxActvty(self):
		del self._TxActvty
		self._TxActvty = base_types.UninitialisedField(self, 'TxActvty', TransactionActivity3Choice, False)

	@property
	def TxAddtlDtls(self):
		return self._TxAddtlDtls

	@TxAddtlDtls.setter
	def TxAddtlDtls(self, value):
		self._TxAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'TxAddtlDtls', Max350Text, False)

	@TxAddtlDtls.deleter
	def TxAddtlDtls(self):
		del self._TxAddtlDtls
		self._TxAddtlDtls = base_types.UninitialisedField(self, 'TxAddtlDtls', Max350Text, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlSctiesDlvry', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties78, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=SettlementDate19Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties78, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngSttlmAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngToBeSttldQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails235, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxOrCorpActnEvtTp', type=SettlementOrCorporateActionEvent26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxActvty', type=TransactionActivity3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))