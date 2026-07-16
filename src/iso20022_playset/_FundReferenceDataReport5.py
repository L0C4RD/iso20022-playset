# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalProductInformation3
from . import CashAccount205
from . import ContactAttributes5
from . import ContactAttributes6
from . import CostsAndCharges2
from . import DistributionStrategy1
from . import Extension1
from . import FinancialInstrument96
from . import FundParties1
from . import ISODate
from . import InvestmentPlanCharacteristics1
from . import InvestmentRestrictions3
from . import LocalMarketAnnex6
from . import MarketPracticeVersion1
from . import Max35Text
from . import OrderDesk1
from . import PaymentInstrument16
from . import ProcessingCharacteristics11
from . import ProcessingCharacteristics12
from . import ProcessingCharacteristics9
from . import SecurityIdentification47
from . import TargetMarket4
from . import ValuationDealingProcessingCharacteristics3
from . import ValueForMoney1
from . import YesNoIndicator

class FundReferenceDataReport5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInfUKMkt", "_AuthrsdPrxy", "_CostsAndChrgs", "_CshSttlmDtls", "_DstrbtnStrtgy", "_ExAnteInd", "_ExPstInd", "_FndDtls", "_FndMgmtCpny", "_FndPties", "_GnlRefDt", "_Id", "_InvstmtRstrctns", "_LclMktAnx", "_MainFndOrdrDsk", "_PlanChrtcs", "_PmtInstrm", "_RedPrcgChrtcs", "_SbcptPrcgChrtcs", "_SctyId", "_SwtchPrcgChrtcs", "_TrgtMkt", "_TrgtMktInd", "_ValForMny", "_ValtnDealgChrtcs", "_Vrsn", "_Xtnsn"]
	@property
	def AddtlInfUKMkt(self):
		return self._AddtlInfUKMkt

	@AddtlInfUKMkt.setter
	def AddtlInfUKMkt(self, value):
		self._AddtlInfUKMkt = value if value is not None else base_types.UninitialisedField(self, 'AddtlInfUKMkt', AdditionalProductInformation3, False)

	@AddtlInfUKMkt.deleter
	def AddtlInfUKMkt(self):
		del self._AddtlInfUKMkt
		self._AddtlInfUKMkt = base_types.UninitialisedField(self, 'AddtlInfUKMkt', AdditionalProductInformation3, False)

	@property
	def AuthrsdPrxy(self):
		return self._AuthrsdPrxy

	@AuthrsdPrxy.setter
	def AuthrsdPrxy(self, value):
		self._AuthrsdPrxy = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdPrxy', ContactAttributes6, False)

	@AuthrsdPrxy.deleter
	def AuthrsdPrxy(self):
		del self._AuthrsdPrxy
		self._AuthrsdPrxy = base_types.UninitialisedField(self, 'AuthrsdPrxy', ContactAttributes6, False)

	@property
	def CostsAndChrgs(self):
		return self._CostsAndChrgs

	@CostsAndChrgs.setter
	def CostsAndChrgs(self, value):
		self._CostsAndChrgs = value if value is not None else base_types.UninitialisedField(self, 'CostsAndChrgs', CostsAndCharges2, True)

	@CostsAndChrgs.deleter
	def CostsAndChrgs(self):
		del self._CostsAndChrgs
		self._CostsAndChrgs = base_types.UninitialisedField(self, 'CostsAndChrgs', CostsAndCharges2, True)

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDtls', CashAccount205, True)

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = base_types.UninitialisedField(self, 'CshSttlmDtls', CashAccount205, True)

	@property
	def DstrbtnStrtgy(self):
		return self._DstrbtnStrtgy

	@DstrbtnStrtgy.setter
	def DstrbtnStrtgy(self, value):
		self._DstrbtnStrtgy = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnStrtgy', DistributionStrategy1, False)

	@DstrbtnStrtgy.deleter
	def DstrbtnStrtgy(self):
		del self._DstrbtnStrtgy
		self._DstrbtnStrtgy = base_types.UninitialisedField(self, 'DstrbtnStrtgy', DistributionStrategy1, False)

	@property
	def ExAnteInd(self):
		return self._ExAnteInd

	@ExAnteInd.setter
	def ExAnteInd(self, value):
		self._ExAnteInd = value if value is not None else base_types.UninitialisedField(self, 'ExAnteInd', YesNoIndicator, False)

	@ExAnteInd.deleter
	def ExAnteInd(self):
		del self._ExAnteInd
		self._ExAnteInd = base_types.UninitialisedField(self, 'ExAnteInd', YesNoIndicator, False)

	@property
	def ExPstInd(self):
		return self._ExPstInd

	@ExPstInd.setter
	def ExPstInd(self, value):
		self._ExPstInd = value if value is not None else base_types.UninitialisedField(self, 'ExPstInd', YesNoIndicator, False)

	@ExPstInd.deleter
	def ExPstInd(self):
		del self._ExPstInd
		self._ExPstInd = base_types.UninitialisedField(self, 'ExPstInd', YesNoIndicator, False)

	@property
	def FndDtls(self):
		return self._FndDtls

	@FndDtls.setter
	def FndDtls(self, value):
		self._FndDtls = value if value is not None else base_types.UninitialisedField(self, 'FndDtls', FinancialInstrument96, False)

	@FndDtls.deleter
	def FndDtls(self):
		del self._FndDtls
		self._FndDtls = base_types.UninitialisedField(self, 'FndDtls', FinancialInstrument96, False)

	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if value is not None else base_types.UninitialisedField(self, 'FndMgmtCpny', ContactAttributes5, False)

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = base_types.UninitialisedField(self, 'FndMgmtCpny', ContactAttributes5, False)

	@property
	def FndPties(self):
		return self._FndPties

	@FndPties.setter
	def FndPties(self, value):
		self._FndPties = value if value is not None else base_types.UninitialisedField(self, 'FndPties', FundParties1, False)

	@FndPties.deleter
	def FndPties(self):
		del self._FndPties
		self._FndPties = base_types.UninitialisedField(self, 'FndPties', FundParties1, False)

	@property
	def GnlRefDt(self):
		return self._GnlRefDt

	@GnlRefDt.setter
	def GnlRefDt(self, value):
		self._GnlRefDt = value if value is not None else base_types.UninitialisedField(self, 'GnlRefDt', ISODate, False)

	@GnlRefDt.deleter
	def GnlRefDt(self):
		del self._GnlRefDt
		self._GnlRefDt = base_types.UninitialisedField(self, 'GnlRefDt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def InvstmtRstrctns(self):
		return self._InvstmtRstrctns

	@InvstmtRstrctns.setter
	def InvstmtRstrctns(self, value):
		self._InvstmtRstrctns = value if value is not None else base_types.UninitialisedField(self, 'InvstmtRstrctns', InvestmentRestrictions3, False)

	@InvstmtRstrctns.deleter
	def InvstmtRstrctns(self):
		del self._InvstmtRstrctns
		self._InvstmtRstrctns = base_types.UninitialisedField(self, 'InvstmtRstrctns', InvestmentRestrictions3, False)

	@property
	def LclMktAnx(self):
		return self._LclMktAnx

	@LclMktAnx.setter
	def LclMktAnx(self, value):
		self._LclMktAnx = value if value is not None else base_types.UninitialisedField(self, 'LclMktAnx', LocalMarketAnnex6, True)

	@LclMktAnx.deleter
	def LclMktAnx(self):
		del self._LclMktAnx
		self._LclMktAnx = base_types.UninitialisedField(self, 'LclMktAnx', LocalMarketAnnex6, True)

	@property
	def MainFndOrdrDsk(self):
		return self._MainFndOrdrDsk

	@MainFndOrdrDsk.setter
	def MainFndOrdrDsk(self, value):
		self._MainFndOrdrDsk = value if value is not None else base_types.UninitialisedField(self, 'MainFndOrdrDsk', OrderDesk1, False)

	@MainFndOrdrDsk.deleter
	def MainFndOrdrDsk(self):
		del self._MainFndOrdrDsk
		self._MainFndOrdrDsk = base_types.UninitialisedField(self, 'MainFndOrdrDsk', OrderDesk1, False)

	@property
	def PlanChrtcs(self):
		return self._PlanChrtcs

	@PlanChrtcs.setter
	def PlanChrtcs(self, value):
		self._PlanChrtcs = value if value is not None else base_types.UninitialisedField(self, 'PlanChrtcs', InvestmentPlanCharacteristics1, True)

	@PlanChrtcs.deleter
	def PlanChrtcs(self):
		del self._PlanChrtcs
		self._PlanChrtcs = base_types.UninitialisedField(self, 'PlanChrtcs', InvestmentPlanCharacteristics1, True)

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrument16, True)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrument16, True)

	@property
	def RedPrcgChrtcs(self):
		return self._RedPrcgChrtcs

	@RedPrcgChrtcs.setter
	def RedPrcgChrtcs(self, value):
		self._RedPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'RedPrcgChrtcs', ProcessingCharacteristics12, False)

	@RedPrcgChrtcs.deleter
	def RedPrcgChrtcs(self):
		del self._RedPrcgChrtcs
		self._RedPrcgChrtcs = base_types.UninitialisedField(self, 'RedPrcgChrtcs', ProcessingCharacteristics12, False)

	@property
	def SbcptPrcgChrtcs(self):
		return self._SbcptPrcgChrtcs

	@SbcptPrcgChrtcs.setter
	def SbcptPrcgChrtcs(self, value):
		self._SbcptPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SbcptPrcgChrtcs', ProcessingCharacteristics11, False)

	@SbcptPrcgChrtcs.deleter
	def SbcptPrcgChrtcs(self):
		del self._SbcptPrcgChrtcs
		self._SbcptPrcgChrtcs = base_types.UninitialisedField(self, 'SbcptPrcgChrtcs', ProcessingCharacteristics11, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification47, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification47, False)

	@property
	def SwtchPrcgChrtcs(self):
		return self._SwtchPrcgChrtcs

	@SwtchPrcgChrtcs.setter
	def SwtchPrcgChrtcs(self, value):
		self._SwtchPrcgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'SwtchPrcgChrtcs', ProcessingCharacteristics9, False)

	@SwtchPrcgChrtcs.deleter
	def SwtchPrcgChrtcs(self):
		del self._SwtchPrcgChrtcs
		self._SwtchPrcgChrtcs = base_types.UninitialisedField(self, 'SwtchPrcgChrtcs', ProcessingCharacteristics9, False)

	@property
	def TrgtMkt(self):
		return self._TrgtMkt

	@TrgtMkt.setter
	def TrgtMkt(self, value):
		self._TrgtMkt = value if value is not None else base_types.UninitialisedField(self, 'TrgtMkt', TargetMarket4, False)

	@TrgtMkt.deleter
	def TrgtMkt(self):
		del self._TrgtMkt
		self._TrgtMkt = base_types.UninitialisedField(self, 'TrgtMkt', TargetMarket4, False)

	@property
	def TrgtMktInd(self):
		return self._TrgtMktInd

	@TrgtMktInd.setter
	def TrgtMktInd(self, value):
		self._TrgtMktInd = value if value is not None else base_types.UninitialisedField(self, 'TrgtMktInd', YesNoIndicator, False)

	@TrgtMktInd.deleter
	def TrgtMktInd(self):
		del self._TrgtMktInd
		self._TrgtMktInd = base_types.UninitialisedField(self, 'TrgtMktInd', YesNoIndicator, False)

	@property
	def ValForMny(self):
		return self._ValForMny

	@ValForMny.setter
	def ValForMny(self, value):
		self._ValForMny = value if value is not None else base_types.UninitialisedField(self, 'ValForMny', ValueForMoney1, False)

	@ValForMny.deleter
	def ValForMny(self):
		del self._ValForMny
		self._ValForMny = base_types.UninitialisedField(self, 'ValForMny', ValueForMoney1, False)

	@property
	def ValtnDealgChrtcs(self):
		return self._ValtnDealgChrtcs

	@ValtnDealgChrtcs.setter
	def ValtnDealgChrtcs(self, value):
		self._ValtnDealgChrtcs = value if value is not None else base_types.UninitialisedField(self, 'ValtnDealgChrtcs', ValuationDealingProcessingCharacteristics3, False)

	@ValtnDealgChrtcs.deleter
	def ValtnDealgChrtcs(self):
		del self._ValtnDealgChrtcs
		self._ValtnDealgChrtcs = base_types.UninitialisedField(self, 'ValtnDealgChrtcs', ValuationDealingProcessingCharacteristics3, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', MarketPracticeVersion1, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', MarketPracticeVersion1, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInfUKMkt', type=AdditionalProductInformation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdPrxy', type=ContactAttributes6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostsAndChrgs', type=CostsAndCharges2, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshSttlmDtls', type=CashAccount205, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DstrbtnStrtgy', type=DistributionStrategy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExPstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndDtls', type=FinancialInstrument96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndMgmtCpny', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndPties', type=FundParties1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlRefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtRstrctns', type=InvestmentRestrictions3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclMktAnx', type=LocalMarketAnnex6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MainFndOrdrDsk', type=OrderDesk1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanChrtcs', type=InvestmentPlanCharacteristics1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RedPrcgChrtcs', type=ProcessingCharacteristics12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPrcgChrtcs', type=ProcessingCharacteristics11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification47, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchPrcgChrtcs', type=ProcessingCharacteristics9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtMkt', type=TargetMarket4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtMktInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValForMny', type=ValueForMoney1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDealgChrtcs', type=ValuationDealingProcessingCharacteristics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))