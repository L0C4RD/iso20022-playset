from . import base_types
from ._AdditionalProductInformation3 import AdditionalProductInformation3
from ._ProcessingCharacteristics11 import ProcessingCharacteristics11
from ._ValuationDealingProcessingCharacteristics3 import ValuationDealingProcessingCharacteristics3
from ._InvestmentPlanCharacteristics1 import InvestmentPlanCharacteristics1
from ._ProcessingCharacteristics12 import ProcessingCharacteristics12
from ._Max35Text import Max35Text
from ._DistributionStrategy1 import DistributionStrategy1
from ._CostsAndCharges2 import CostsAndCharges2
from ._SecurityIdentification47 import SecurityIdentification47
from ._Extension1 import Extension1
from ._PaymentInstrument16 import PaymentInstrument16
from ._InvestmentRestrictions3 import InvestmentRestrictions3
from ._ISODate import ISODate
from ._OrderDesk1 import OrderDesk1
from ._LocalMarketAnnex6 import LocalMarketAnnex6
from ._FundParties1 import FundParties1
from ._FinancialInstrument96 import FinancialInstrument96
from ._ValueForMoney1 import ValueForMoney1
from ._CashAccount205 import CashAccount205
from ._MarketPracticeVersion1 import MarketPracticeVersion1
from ._ContactAttributes6 import ContactAttributes6
from ._TargetMarket4 import TargetMarket4
from ._YesNoIndicator import YesNoIndicator
from ._ProcessingCharacteristics9 import ProcessingCharacteristics9
from ._ContactAttributes5 import ContactAttributes5

class FundReferenceDataReport5(base_types._BaseFieldType):

	__slots__ = ["_ValtnDealgChrtcs", "_FndMgmtCpny", "_CshSttlmDtls", "_InvstmtRstrctns", "_FndDtls", "_SwtchPrcgChrtcs", "_ExAnteInd", "_PmtInstrm", "_ExPstInd", "_LclMktAnx", "_RedPrcgChrtcs", "_MainFndOrdrDsk", "_AuthrsdPrxy", "_Xtnsn", "_TrgtMktInd", "_Vrsn", "_ValForMny", "_Id", "_SctyId", "_TrgtMkt", "_GnlRefDt", "_FndPties", "_DstrbtnStrtgy", "_PlanChrtcs", "_AddtlInfUKMkt", "_SbcptPrcgChrtcs", "_CostsAndChrgs"]
	@property
	def ValtnDealgChrtcs(self):
		return self._ValtnDealgChrtcs

	@ValtnDealgChrtcs.setter
	def ValtnDealgChrtcs(self, value):
		self._ValtnDealgChrtcs = value if type(value) != base_types.auto else self.make_default("ValtnDealgChrtcs")

	@ValtnDealgChrtcs.deleter
	def ValtnDealgChrtcs(self):
		del self._ValtnDealgChrtcs
		self._ValtnDealgChrtcs = None

	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if type(value) != base_types.auto else self.make_default("FndMgmtCpny")

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = None

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if type(value) != base_types.auto else self.make_default("CshSttlmDtls")

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = None

	@property
	def InvstmtRstrctns(self):
		return self._InvstmtRstrctns

	@InvstmtRstrctns.setter
	def InvstmtRstrctns(self, value):
		self._InvstmtRstrctns = value if type(value) != base_types.auto else self.make_default("InvstmtRstrctns")

	@InvstmtRstrctns.deleter
	def InvstmtRstrctns(self):
		del self._InvstmtRstrctns
		self._InvstmtRstrctns = None

	@property
	def FndDtls(self):
		return self._FndDtls

	@FndDtls.setter
	def FndDtls(self, value):
		self._FndDtls = value if type(value) != base_types.auto else self.make_default("FndDtls")

	@FndDtls.deleter
	def FndDtls(self):
		del self._FndDtls
		self._FndDtls = None

	@property
	def SwtchPrcgChrtcs(self):
		return self._SwtchPrcgChrtcs

	@SwtchPrcgChrtcs.setter
	def SwtchPrcgChrtcs(self, value):
		self._SwtchPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("SwtchPrcgChrtcs")

	@SwtchPrcgChrtcs.deleter
	def SwtchPrcgChrtcs(self):
		del self._SwtchPrcgChrtcs
		self._SwtchPrcgChrtcs = None

	@property
	def ExAnteInd(self):
		return self._ExAnteInd

	@ExAnteInd.setter
	def ExAnteInd(self, value):
		self._ExAnteInd = value if type(value) != base_types.auto else self.make_default("ExAnteInd")

	@ExAnteInd.deleter
	def ExAnteInd(self):
		del self._ExAnteInd
		self._ExAnteInd = None

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != base_types.auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	@property
	def ExPstInd(self):
		return self._ExPstInd

	@ExPstInd.setter
	def ExPstInd(self, value):
		self._ExPstInd = value if type(value) != base_types.auto else self.make_default("ExPstInd")

	@ExPstInd.deleter
	def ExPstInd(self):
		del self._ExPstInd
		self._ExPstInd = None

	@property
	def LclMktAnx(self):
		return self._LclMktAnx

	@LclMktAnx.setter
	def LclMktAnx(self, value):
		self._LclMktAnx = value if type(value) != base_types.auto else self.make_default("LclMktAnx")

	@LclMktAnx.deleter
	def LclMktAnx(self):
		del self._LclMktAnx
		self._LclMktAnx = None

	@property
	def RedPrcgChrtcs(self):
		return self._RedPrcgChrtcs

	@RedPrcgChrtcs.setter
	def RedPrcgChrtcs(self, value):
		self._RedPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("RedPrcgChrtcs")

	@RedPrcgChrtcs.deleter
	def RedPrcgChrtcs(self):
		del self._RedPrcgChrtcs
		self._RedPrcgChrtcs = None

	@property
	def MainFndOrdrDsk(self):
		return self._MainFndOrdrDsk

	@MainFndOrdrDsk.setter
	def MainFndOrdrDsk(self, value):
		self._MainFndOrdrDsk = value if type(value) != base_types.auto else self.make_default("MainFndOrdrDsk")

	@MainFndOrdrDsk.deleter
	def MainFndOrdrDsk(self):
		del self._MainFndOrdrDsk
		self._MainFndOrdrDsk = None

	@property
	def AuthrsdPrxy(self):
		return self._AuthrsdPrxy

	@AuthrsdPrxy.setter
	def AuthrsdPrxy(self, value):
		self._AuthrsdPrxy = value if type(value) != base_types.auto else self.make_default("AuthrsdPrxy")

	@AuthrsdPrxy.deleter
	def AuthrsdPrxy(self):
		del self._AuthrsdPrxy
		self._AuthrsdPrxy = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def TrgtMktInd(self):
		return self._TrgtMktInd

	@TrgtMktInd.setter
	def TrgtMktInd(self, value):
		self._TrgtMktInd = value if type(value) != base_types.auto else self.make_default("TrgtMktInd")

	@TrgtMktInd.deleter
	def TrgtMktInd(self):
		del self._TrgtMktInd
		self._TrgtMktInd = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def ValForMny(self):
		return self._ValForMny

	@ValForMny.setter
	def ValForMny(self, value):
		self._ValForMny = value if type(value) != base_types.auto else self.make_default("ValForMny")

	@ValForMny.deleter
	def ValForMny(self):
		del self._ValForMny
		self._ValForMny = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def TrgtMkt(self):
		return self._TrgtMkt

	@TrgtMkt.setter
	def TrgtMkt(self, value):
		self._TrgtMkt = value if type(value) != base_types.auto else self.make_default("TrgtMkt")

	@TrgtMkt.deleter
	def TrgtMkt(self):
		del self._TrgtMkt
		self._TrgtMkt = None

	@property
	def GnlRefDt(self):
		return self._GnlRefDt

	@GnlRefDt.setter
	def GnlRefDt(self, value):
		self._GnlRefDt = value if type(value) != base_types.auto else self.make_default("GnlRefDt")

	@GnlRefDt.deleter
	def GnlRefDt(self):
		del self._GnlRefDt
		self._GnlRefDt = None

	@property
	def FndPties(self):
		return self._FndPties

	@FndPties.setter
	def FndPties(self, value):
		self._FndPties = value if type(value) != base_types.auto else self.make_default("FndPties")

	@FndPties.deleter
	def FndPties(self):
		del self._FndPties
		self._FndPties = None

	@property
	def DstrbtnStrtgy(self):
		return self._DstrbtnStrtgy

	@DstrbtnStrtgy.setter
	def DstrbtnStrtgy(self, value):
		self._DstrbtnStrtgy = value if type(value) != base_types.auto else self.make_default("DstrbtnStrtgy")

	@DstrbtnStrtgy.deleter
	def DstrbtnStrtgy(self):
		del self._DstrbtnStrtgy
		self._DstrbtnStrtgy = None

	@property
	def PlanChrtcs(self):
		return self._PlanChrtcs

	@PlanChrtcs.setter
	def PlanChrtcs(self, value):
		self._PlanChrtcs = value if type(value) != base_types.auto else self.make_default("PlanChrtcs")

	@PlanChrtcs.deleter
	def PlanChrtcs(self):
		del self._PlanChrtcs
		self._PlanChrtcs = None

	@property
	def AddtlInfUKMkt(self):
		return self._AddtlInfUKMkt

	@AddtlInfUKMkt.setter
	def AddtlInfUKMkt(self, value):
		self._AddtlInfUKMkt = value if type(value) != base_types.auto else self.make_default("AddtlInfUKMkt")

	@AddtlInfUKMkt.deleter
	def AddtlInfUKMkt(self):
		del self._AddtlInfUKMkt
		self._AddtlInfUKMkt = None

	@property
	def SbcptPrcgChrtcs(self):
		return self._SbcptPrcgChrtcs

	@SbcptPrcgChrtcs.setter
	def SbcptPrcgChrtcs(self, value):
		self._SbcptPrcgChrtcs = value if type(value) != base_types.auto else self.make_default("SbcptPrcgChrtcs")

	@SbcptPrcgChrtcs.deleter
	def SbcptPrcgChrtcs(self):
		del self._SbcptPrcgChrtcs
		self._SbcptPrcgChrtcs = None

	@property
	def CostsAndChrgs(self):
		return self._CostsAndChrgs

	@CostsAndChrgs.setter
	def CostsAndChrgs(self, value):
		self._CostsAndChrgs = value if type(value) != base_types.auto else self.make_default("CostsAndChrgs")

	@CostsAndChrgs.deleter
	def CostsAndChrgs(self):
		del self._CostsAndChrgs
		self._CostsAndChrgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValtnDealgChrtcs', type=ValuationDealingProcessingCharacteristics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndMgmtCpny', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=CashAccount205, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtRstrctns', type=InvestmentRestrictions3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndDtls', type=FinancialInstrument96, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwtchPrcgChrtcs', type=ProcessingCharacteristics9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExAnteInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ExPstInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclMktAnx', type=LocalMarketAnnex6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RedPrcgChrtcs', type=ProcessingCharacteristics12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainFndOrdrDsk', type=OrderDesk1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdPrxy', type=ContactAttributes6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrgtMktInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValForMny', type=ValueForMoney1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification47, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtMkt', type=TargetMarket4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnlRefDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndPties', type=FundParties1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnStrtgy', type=DistributionStrategy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanChrtcs', type=InvestmentPlanCharacteristics1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInfUKMkt', type=AdditionalProductInformation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPrcgChrtcs', type=ProcessingCharacteristics11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CostsAndChrgs', type=CostsAndCharges2, min=0, max=2, mutex_group=None, array=True),
	))

