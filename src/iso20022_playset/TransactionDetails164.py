from . import base_types
import RestrictedFINXMax350Text
import DateAndDateTime2Choice
import PlaceOfTradeIdentification2
import ISODateTime
import Quantity54Choice
import DeliveryReceiptType2Code
import AmountAndDirection67
import SettlementParties109
import SettlementDate32Choice
import SettlementDetails197
import PlaceOfClearingIdentification2
import TransactionActivity4Choice
import ReceiveDelivery1Code
import SafeKeepingPlace4
import TradeDate9Choice
import SupplementaryData1
import SecurityIdentification20
import SettlementOrCorporateActionEvent32Choice

class TransactionDetails164(base_types._BaseFieldType):

	__slots__ = ["_TxAddtlDtls", "_SfkpgPlc", "_AckdStsTmStmp", "_SttlmParams", "_PlcOfTrad", "_MtchdStsTmStmp", "_SttlmDt", "_DlvrgSttlmPties", "_TxActvty", "_LateDlvryDt", "_PlcOfClr", "_FinInstrmId", "_SctiesMvmntTp", "_PstngQty", "_Pmt", "_SplmtryData", "_PstngAmt", "_XpctdValDt", "_TradDt", "_RcvgSttlmPties", "_XpctdSttlmDt", "_SttlmTxOrCorpActnEvtTp", "_PrtlyRlsdQty"]
	@property
	def TxAddtlDtls(self):
		return self._TxAddtlDtls

	@TxAddtlDtls.setter
	def TxAddtlDtls(self, value):
		self._TxAddtlDtls = value if type(value) != auto else self.make_default("TxAddtlDtls")

	@TxAddtlDtls.deleter
	def TxAddtlDtls(self):
		del self._TxAddtlDtls
		self._TxAddtlDtls = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if type(value) != auto else self.make_default("AckdStsTmStmp")

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = None

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def MtchdStsTmStmp(self):
		return self._MtchdStsTmStmp

	@MtchdStsTmStmp.setter
	def MtchdStsTmStmp(self, value):
		self._MtchdStsTmStmp = value if type(value) != auto else self.make_default("MtchdStsTmStmp")

	@MtchdStsTmStmp.deleter
	def MtchdStsTmStmp(self):
		del self._MtchdStsTmStmp
		self._MtchdStsTmStmp = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def TxActvty(self):
		return self._TxActvty

	@TxActvty.setter
	def TxActvty(self, value):
		self._TxActvty = value if type(value) != auto else self.make_default("TxActvty")

	@TxActvty.deleter
	def TxActvty(self):
		del self._TxActvty
		self._TxActvty = None

	@property
	def LateDlvryDt(self):
		return self._LateDlvryDt

	@LateDlvryDt.setter
	def LateDlvryDt(self, value):
		self._LateDlvryDt = value if type(value) != auto else self.make_default("LateDlvryDt")

	@LateDlvryDt.deleter
	def LateDlvryDt(self):
		del self._LateDlvryDt
		self._LateDlvryDt = None

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if type(value) != auto else self.make_default("PlcOfClr")

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if type(value) != auto else self.make_default("PstngQty")

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if type(value) != auto else self.make_default("PstngAmt")

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = None

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if type(value) != auto else self.make_default("XpctdValDt")

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def XpctdSttlmDt(self):
		return self._XpctdSttlmDt

	@XpctdSttlmDt.setter
	def XpctdSttlmDt(self, value):
		self._XpctdSttlmDt = value if type(value) != auto else self.make_default("XpctdSttlmDt")

	@XpctdSttlmDt.deleter
	def XpctdSttlmDt(self):
		del self._XpctdSttlmDt
		self._XpctdSttlmDt = None

	@property
	def SttlmTxOrCorpActnEvtTp(self):
		return self._SttlmTxOrCorpActnEvtTp

	@SttlmTxOrCorpActnEvtTp.setter
	def SttlmTxOrCorpActnEvtTp(self, value):
		self._SttlmTxOrCorpActnEvtTp = value if type(value) != auto else self.make_default("SttlmTxOrCorpActnEvtTp")

	@SttlmTxOrCorpActnEvtTp.deleter
	def SttlmTxOrCorpActnEvtTp(self):
		del self._SttlmTxOrCorpActnEvtTp
		self._SttlmTxOrCorpActnEvtTp = None

	@property
	def PrtlyRlsdQty(self):
		return self._PrtlyRlsdQty

	@PrtlyRlsdQty.setter
	def PrtlyRlsdQty(self, value):
		self._PrtlyRlsdQty = value if type(value) != auto else self.make_default("PrtlyRlsdQty")

	@PrtlyRlsdQty.deleter
	def PrtlyRlsdQty(self):
		del self._PrtlyRlsdQty
		self._PrtlyRlsdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails197, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate32Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxActvty', type=TransactionActivity4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateDlvryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=Quantity54Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PstngAmt', type=AmountAndDirection67, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxOrCorpActnEvtTp', type=SettlementOrCorporateActionEvent32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyRlsdQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
	))

