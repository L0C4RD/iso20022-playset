# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection18 import AmountAndDirection18
from ._AmountAndDirection59 import AmountAndDirection59
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._ISODateTime import ISODateTime
from ._Max3Number import Max3Number
from ._PlaceOfClearingIdentification2 import PlaceOfClearingIdentification2
from ._PlaceOfTradeIdentification2 import PlaceOfTradeIdentification2
from ._Quantity54Choice import Quantity54Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text
from ._SafeKeepingPlace4 import SafeKeepingPlace4
from ._SettlementDate20Choice import SettlementDate20Choice
from ._SettlementDetails198 import SettlementDetails198
from ._SettlementOrCorporateActionEvent33Choice import SettlementOrCorporateActionEvent33Choice
from ._SettlementParties109 import SettlementParties109
from ._TradeDate9Choice import TradeDate9Choice
from ._TransactionActivity4Choice import TransactionActivity4Choice
from ._YesNoIndicator import YesNoIndicator

class TransactionDetails165(base_types._BaseFieldType):

	__slots__ = ["_AckdStsTmStmp", "_AcrdIntrstAmt", "_DlvrgSttlmPties", "_FctvSttlmDt", "_MtchdStsTmStmp", "_NbOfDaysAcrd", "_PlcOfClr", "_PlcOfTrad", "_Pmt", "_PstngAmt", "_PstngQty", "_RcvgSttlmPties", "_RvslInd", "_SctiesMvmntTp", "_SfkpgPlc", "_SttlmDt", "_SttlmParams", "_SttlmTxOrCorpActnEvtTp", "_TradDt", "_TxActvty", "_TxAddtlDtls", "_ValDt"]
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
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != base_types.auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

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
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != base_types.auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if type(value) != base_types.auto else self.make_default("PlcOfClr")

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

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
	def RvslInd(self):
		return self._RvslInd

	@RvslInd.setter
	def RvslInd(self, value):
		self._RvslInd = value if type(value) != base_types.auto else self.make_default("RvslInd")

	@RvslInd.deleter
	def RvslInd(self):
		del self._RvslInd
		self._RvslInd = None

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
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

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
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != base_types.auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

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
	def TxActvty(self):
		return self._TxActvty

	@TxActvty.setter
	def TxActvty(self, value):
		self._TxActvty = value if type(value) != base_types.auto else self.make_default("TxActvty")

	@TxActvty.deleter
	def TxActvty(self):
		del self._TxActvty
		self._TxActvty = None

	@property
	def TxAddtlDtls(self):
		return self._TxAddtlDtls

	@TxAddtlDtls.setter
	def TxAddtlDtls(self, value):
		self._TxAddtlDtls = value if type(value) != base_types.auto else self.make_default("TxAddtlDtls")

	@TxAddtlDtls.deleter
	def TxAddtlDtls(self):
		del self._TxAddtlDtls
		self._TxAddtlDtls = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=AmountAndDirection18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=Quantity54Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties109, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails198, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxOrCorpActnEvtTp', type=SettlementOrCorporateActionEvent33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxActvty', type=TransactionActivity4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))