# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection95 import AmountAndDirection95
from ._CashParties41 import CashParties41
from ._FinancialInstrumentAttributes111 import FinancialInstrumentAttributes111
from ._Linkages63 import Linkages63
from ._OtherAmounts39 import OtherAmounts39
from ._OtherParties43 import OtherParties43
from ._QuantityAndAccount118 import QuantityAndAccount118
from ._RegistrationParameters6 import RegistrationParameters6
from ._SecuritiesTradeDetails146 import SecuritiesTradeDetails146
from ._SettlementDetails218 import SettlementDetails218
from ._SettlementParties98 import SettlementParties98
from ._SettlementTypeAndAdditionalParameters13 import SettlementTypeAndAdditionalParameters13
from ._StandingSettlementInstruction20 import StandingSettlementInstruction20
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesSettlementTransactionDetails56(base_types._BaseFieldType):

	__slots__ = ["_AddtlPhysOrRegnDtls", "_CshPties", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_Lnkgs", "_OthrAmts", "_OthrBizPties", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SplmtryData", "_StgSttlmInstrDtls", "_SttlmAmt", "_SttlmParams", "_SttlmTpAndAddtlParams", "_TradDtls"]
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
	def StgSttlmInstrDtls(self):
		return self._StgSttlmInstrDtls

	@StgSttlmInstrDtls.setter
	def StgSttlmInstrDtls(self, value):
		self._StgSttlmInstrDtls = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrDtls")

	@StgSttlmInstrDtls.deleter
	def StgSttlmInstrDtls(self):
		del self._StgSttlmInstrDtls
		self._StgSttlmInstrDtls = None

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
	def SttlmTpAndAddtlParams(self):
		return self._SttlmTpAndAddtlParams

	@SttlmTpAndAddtlParams.setter
	def SttlmTpAndAddtlParams(self, value):
		self._SttlmTpAndAddtlParams = value if type(value) != base_types.auto else self.make_default("SttlmTpAndAddtlParams")

	@SttlmTpAndAddtlParams.deleter
	def SttlmTpAndAddtlParams(self):
		del self._SttlmTpAndAddtlParams
		self._SttlmTpAndAddtlParams = None

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
		base_types.FieldEntry(name='AddtlPhysOrRegnDtls', type=RegistrationParameters6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshPties', type=CashParties41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties98, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages63, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount118, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties98, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgSttlmInstrDtls', type=StandingSettlementInstruction20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection95, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails218, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTpAndAddtlParams', type=SettlementTypeAndAdditionalParameters13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails146, min=0, max=1, mutex_group=None, array=False),
	))