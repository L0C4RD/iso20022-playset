# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection94
from . import CashParties41
from . import FinancialInstrumentAttributes111
from . import GeneratedReason5
from . import Linkages61
from . import NetworkFee1
from . import NumberCount2Choice
from . import OtherAmounts45
from . import OtherParties43
from . import QuantityAndAccount117
from . import RegistrationParameters6
from . import SecuritiesTradeDetails145
from . import SecurityIdentification19
from . import SettlementDetails217
from . import SettlementParties126
from . import SettlementTypeAndIdentification29
from . import StatusAndReason48
from . import SupplementaryData1

class SecuritiesSettlementTransactionGenerationNotificationV12(base_types._BaseFieldType):

	__slots__ = ["_AddtlPhysOrRegnDtls", "_CshPties", "_DgtlNtwkFee", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_GnrtdRsn", "_Lnkgs", "_NbCounts", "_OthrAmts", "_OthrBizPties", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SplmtryData", "_StsAndRsn", "_SttlmAmt", "_SttlmParams", "_TradDtls", "_TxIdDtls"]
	@property
	def AddtlPhysOrRegnDtls(self):
		return self._AddtlPhysOrRegnDtls

	@AddtlPhysOrRegnDtls.setter
	def AddtlPhysOrRegnDtls(self, value):
		self._AddtlPhysOrRegnDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlPhysOrRegnDtls', RegistrationParameters6, False)

	@AddtlPhysOrRegnDtls.deleter
	def AddtlPhysOrRegnDtls(self):
		del self._AddtlPhysOrRegnDtls
		self._AddtlPhysOrRegnDtls = base_types.UninitialisedField(self, 'AddtlPhysOrRegnDtls', RegistrationParameters6, False)

	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if value is not None else base_types.UninitialisedField(self, 'CshPties', CashParties41, False)

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = base_types.UninitialisedField(self, 'CshPties', CashParties41, False)

	@property
	def DgtlNtwkFee(self):
		return self._DgtlNtwkFee

	@DgtlNtwkFee.setter
	def DgtlNtwkFee(self, value):
		self._DgtlNtwkFee = value if value is not None else base_types.UninitialisedField(self, 'DgtlNtwkFee', NetworkFee1, False)

	@DgtlNtwkFee.deleter
	def DgtlNtwkFee(self):
		del self._DgtlNtwkFee
		self._DgtlNtwkFee = base_types.UninitialisedField(self, 'DgtlNtwkFee', NetworkFee1, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

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
	def GnrtdRsn(self):
		return self._GnrtdRsn

	@GnrtdRsn.setter
	def GnrtdRsn(self, value):
		self._GnrtdRsn = value if value is not None else base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReason5, True)

	@GnrtdRsn.deleter
	def GnrtdRsn(self):
		del self._GnrtdRsn
		self._GnrtdRsn = base_types.UninitialisedField(self, 'GnrtdRsn', GeneratedReason5, True)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages61, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages61, True)

	@property
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if value is not None else base_types.UninitialisedField(self, 'NbCounts', NumberCount2Choice, False)

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = base_types.UninitialisedField(self, 'NbCounts', NumberCount2Choice, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts45, False)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts45, False)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties43, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties43, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount117, True)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount117, True)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

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
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', StatusAndReason48, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', StatusAndReason48, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection94, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection94, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails217, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails217, False)

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails145, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails145, False)

	@property
	def TxIdDtls(self):
		return self._TxIdDtls

	@TxIdDtls.setter
	def TxIdDtls(self, value):
		self._TxIdDtls = value if value is not None else base_types.UninitialisedField(self, 'TxIdDtls', SettlementTypeAndIdentification29, False)

	@TxIdDtls.deleter
	def TxIdDtls(self):
		del self._TxIdDtls
		self._TxIdDtls = base_types.UninitialisedField(self, 'TxIdDtls', SettlementTypeAndIdentification29, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlNtwkFee', type=NetworkFee1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnrtdRsn', type=GeneratedReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lnkgs', type=Linkages61, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbCounts', type=NumberCount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount117, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAndRsn', type=StatusAndReason48, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails217, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails145, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdDtls', type=SettlementTypeAndIdentification29, min=1, max=1, mutex_group=None, array=False),
	))