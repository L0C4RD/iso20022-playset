from . import base_types
from ._CashParties38 import CashParties38
from ._RegistrationParameters7 import RegistrationParameters7
from ._OtherParties44 import OtherParties44
from ._Linkages68 import Linkages68
from ._SettlementParties105 import SettlementParties105
from ._SecuritiesTradeDetails130 import SecuritiesTradeDetails130
from ._SettlementDetails212 import SettlementDetails212
from ._AmountAndDirection96 import AmountAndDirection96
from ._FinancialInstrumentAttributes122 import FinancialInstrumentAttributes122
from ._OtherAmounts43 import OtherAmounts43
from ._GeneratedReason6 import GeneratedReason6
from ._StatusAndReason29 import StatusAndReason29
from ._QuantityAndAccount104 import QuantityAndAccount104
from ._NumberCount2Choice import NumberCount2Choice
from ._SettlementTypeAndIdentification28 import SettlementTypeAndIdentification28
from ._SupplementaryData1 import SupplementaryData1
from ._SecurityIdentification20 import SecurityIdentification20

class SecuritiesSettlementTransactionGenerationNotification002V11(base_types._BaseFieldType):

	__slots__ = ["_NbCounts", "_GnrtdRsn", "_DlvrgSttlmPties", "_TxIdDtls", "_OthrBizPties", "_OthrAmts", "_QtyAndAcctDtls", "_Lnkgs", "_SttlmAmt", "_CshPties", "_AddtlPhysOrRegnDtls", "_FinInstrmAttrbts", "_FinInstrmId", "_StsAndRsn", "_SttlmParams", "_RcvgSttlmPties", "_SplmtryData", "_TradDtls"]
	@property
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if type(value) != base_types.auto else self.make_default("NbCounts")

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = None

	@property
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if type(value) != base_types.auto else self.make_default("GnrtdRsn")

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = None

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
	def TxIdDtls(self):
		return self._TxIdDtls

	@TxIdDtls.setter
	def TxIdDtls(self, value):
		self._TxIdDtls = value if type(value) != base_types.auto else self.make_default("TxIdDtls")

	@TxIdDtls.deleter
	def TxIdDtls(self):
		del self._TxIdDtls
		self._TxIdDtls = None

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if type(value) != base_types.auto else self.make_default("OthrBizPties")

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = None

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if type(value) != base_types.auto else self.make_default("OthrAmts")

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = None

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if type(value) != base_types.auto else self.make_default("QtyAndAcctDtls")

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = None

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != base_types.auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

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
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if type(value) != base_types.auto else self.make_default("CshPties")

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = None

	@property
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if type(value) != base_types.auto else self.make_default("AddtlPhysOrRegnDtls")

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = None

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

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
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if type(value) != base_types.auto else self.make_default("TradDtls")

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbCounts', type=NumberCount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnrtdRsn', type=GeneratedReason6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdDtls', type=SettlementTypeAndIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount104, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lnkgs', type=Linkages68, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=StatusAndReason29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails212, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails130, min=1, max=1, mutex_group=None, array=False),
	))

