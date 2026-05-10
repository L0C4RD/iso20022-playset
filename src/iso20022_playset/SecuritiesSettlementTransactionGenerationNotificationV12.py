from . import base_types
import AmountAndDirection94
import SecuritiesTradeDetails145
import SettlementDetails217
import GeneratedReason5
import Linkages61
import RegistrationParameters6
import QuantityAndAccount117
import NumberCount2Choice
import CashParties41
import SettlementParties126
import StatusAndReason48
import SupplementaryData1
import OtherParties43
import SecurityIdentification19
import NetworkFee1
import FinancialInstrumentAttributes111
import SettlementTypeAndIdentification29
import OtherAmounts45

class SecuritiesSettlementTransactionGenerationNotificationV12(base_types._BaseFieldType):

	__slots__ = ["_QtyAndAcctDtls", "_CshPties", "_SttlmParams", "_DgtlNtwkFee", "_FinInstrmAttrbts", "_TxIdDtls", "_GnrtdRsn", "_StsAndRsn", "_RcvgSttlmPties", "_Lnkgs", "_SplmtryData", "_NbCounts", "_AddtlPhysOrRegnDtls", "_TradDtls", "_FinInstrmId", "_OthrBizPties", "_DlvrgSttlmPties", "_SttlmAmt", "_OthrAmts"]
	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if type(value) != auto else self.make_default("QtyAndAcctDtls")

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = None

	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if type(value) != auto else self.make_default("CshPties")

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = None

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
	def DgtlNtwkFee(self):
		return self._DgtlNtwkFee

	@DgtlNtwkFee.setter
	def DgtlNtwkFee(self, value):
		self._DgtlNtwkFee = value if type(value) != auto else self.make_default("DgtlNtwkFee")

	@DgtlNtwkFee.deleter
	def DgtlNtwkFee(self):
		del self._DgtlNtwkFee
		self._DgtlNtwkFee = None

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	@property
	def TxIdDtls(self):
		return self._TxIdDtls

	@TxIdDtls.setter
	def TxIdDtls(self, value):
		self._TxIdDtls = value if type(value) != auto else self.make_default("TxIdDtls")

	@TxIdDtls.deleter
	def TxIdDtls(self):
		del self._TxIdDtls
		self._TxIdDtls = None

	@property
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if type(value) != auto else self.make_default("GnrtdRsn")

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

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
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

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
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if type(value) != auto else self.make_default("NbCounts")

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = None

	@property
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if type(value) != auto else self.make_default("AddtlPhysOrRegnDtls")

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = None

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if type(value) != auto else self.make_default("TradDtls")

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = None

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
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if type(value) != auto else self.make_default("OthrBizPties")

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = None

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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if type(value) != auto else self.make_default("OthrAmts")

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount117, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshPties', type=CashParties41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails217, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlNtwkFee', type=NetworkFee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdDtls', type=SettlementTypeAndIdentification29, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnrtdRsn', type=GeneratedReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAndRsn', type=StatusAndReason48, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages61, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbCounts', type=NumberCount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails145, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts45, min=0, max=1, mutex_group=None, array=False),
	))

