from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._OptionAvailabilityStatus4Choice import OptionAvailabilityStatus4Choice
from ._BidRangeType2Choice import BidRangeType2Choice
from ._FractionDispositionType31Choice import FractionDispositionType31Choice
from ._SecurityIdentification20 import SecurityIdentification20
from ._CorporateActionNarrative64 import CorporateActionNarrative64
from ._CountryCode import CountryCode
from ._CorporateActionOption46Choice import CorporateActionOption46Choice
from ._ProrationBelowMinimumQuantity1Choice import ProrationBelowMinimumQuantity1Choice
from ._CorporateActionPrice97 import CorporateActionPrice97
from ._BeneficiaryCertificationType15Choice import BeneficiaryCertificationType15Choice
from ._DefaultProcessingOrStandingInstruction2Choice import DefaultProcessingOrStandingInstruction2Choice
from ._YesNoIndicator import YesNoIndicator
from ._Exact3UpperCaseAlphaNumericText import Exact3UpperCaseAlphaNumericText
from ._OfferTypeFormat16Choice import OfferTypeFormat16Choice
from ._CashOption113 import CashOption113
from ._SecuritiesOption84 import SecuritiesOption84
from ._OptionFeaturesFormat31Choice import OptionFeaturesFormat31Choice
from ._Exact3NumericText import Exact3NumericText
from ._SecuritiesOption117 import SecuritiesOption117
from ._CorporateActionPeriod12 import CorporateActionPeriod12
from ._CorporateActionDate108 import CorporateActionDate108
from ._CorporateActionRate136 import CorporateActionRate136

class CorporateActionOption247(base_types._BaseFieldType):

	__slots__ = ["_CshMvmntDtls", "_AccptncPrtyLvl", "_WdrwlAllwdInd", "_DtDtls", "_FinInstrmId", "_NonDmclCtry", "_DfltPrcgOrStgInstr", "_OptnFeatrs", "_AddtlInf", "_PricDtls", "_OfferTp", "_PrdDtls", "_OptnAvlbtySts", "_ChngAllwdInd", "_CcyOptn", "_CertfctnBrkdwnInd", "_ApldOptnInd", "_CertfctnBrkdwnTp", "_SctiesMvmntDtls", "_SctiesQty", "_ChrgsApldInd", "_OptnTp", "_PrratnBlwMinQty", "_VldDmclCtry", "_BidRgTp", "_OptnNb", "_FrctnDspstn", "_RateAndAmtDtls"]
	@property
	def AccptncPrtyLvl(self):
		return self._AccptncPrtyLvl

	@AccptncPrtyLvl.setter
	def AccptncPrtyLvl(self, value):
		self._AccptncPrtyLvl = value if type(value) != base_types.auto else self.make_default("AccptncPrtyLvl")

	@AccptncPrtyLvl.deleter
	def AccptncPrtyLvl(self):
		del self._AccptncPrtyLvl
		self._AccptncPrtyLvl = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ApldOptnInd(self):
		return self._ApldOptnInd

	@ApldOptnInd.setter
	def ApldOptnInd(self, value):
		self._ApldOptnInd = value if type(value) != base_types.auto else self.make_default("ApldOptnInd")

	@ApldOptnInd.deleter
	def ApldOptnInd(self):
		del self._ApldOptnInd
		self._ApldOptnInd = None

	@property
	def BidRgTp(self):
		return self._BidRgTp

	@BidRgTp.setter
	def BidRgTp(self, value):
		self._BidRgTp = value if type(value) != base_types.auto else self.make_default("BidRgTp")

	@BidRgTp.deleter
	def BidRgTp(self):
		del self._BidRgTp
		self._BidRgTp = None

	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if type(value) != base_types.auto else self.make_default("CcyOptn")

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = None

	@property
	def CertfctnBrkdwnInd(self):
		return self._CertfctnBrkdwnInd

	@CertfctnBrkdwnInd.setter
	def CertfctnBrkdwnInd(self, value):
		self._CertfctnBrkdwnInd = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwnInd")

	@CertfctnBrkdwnInd.deleter
	def CertfctnBrkdwnInd(self):
		del self._CertfctnBrkdwnInd
		self._CertfctnBrkdwnInd = None

	@property
	def CertfctnBrkdwnTp(self):
		return self._CertfctnBrkdwnTp

	@CertfctnBrkdwnTp.setter
	def CertfctnBrkdwnTp(self, value):
		self._CertfctnBrkdwnTp = value if type(value) != base_types.auto else self.make_default("CertfctnBrkdwnTp")

	@CertfctnBrkdwnTp.deleter
	def CertfctnBrkdwnTp(self):
		del self._CertfctnBrkdwnTp
		self._CertfctnBrkdwnTp = None

	@property
	def ChngAllwdInd(self):
		return self._ChngAllwdInd

	@ChngAllwdInd.setter
	def ChngAllwdInd(self, value):
		self._ChngAllwdInd = value if type(value) != base_types.auto else self.make_default("ChngAllwdInd")

	@ChngAllwdInd.deleter
	def ChngAllwdInd(self):
		del self._ChngAllwdInd
		self._ChngAllwdInd = None

	@property
	def ChrgsApldInd(self):
		return self._ChrgsApldInd

	@ChrgsApldInd.setter
	def ChrgsApldInd(self, value):
		self._ChrgsApldInd = value if type(value) != base_types.auto else self.make_default("ChrgsApldInd")

	@ChrgsApldInd.deleter
	def ChrgsApldInd(self):
		del self._ChrgsApldInd
		self._ChrgsApldInd = None

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if type(value) != base_types.auto else self.make_default("CshMvmntDtls")

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = None

	@property
	def DfltPrcgOrStgInstr(self):
		return self._DfltPrcgOrStgInstr

	@DfltPrcgOrStgInstr.setter
	def DfltPrcgOrStgInstr(self, value):
		self._DfltPrcgOrStgInstr = value if type(value) != base_types.auto else self.make_default("DfltPrcgOrStgInstr")

	@DfltPrcgOrStgInstr.deleter
	def DfltPrcgOrStgInstr(self):
		del self._DfltPrcgOrStgInstr
		self._DfltPrcgOrStgInstr = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != base_types.auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

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
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != base_types.auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	@property
	def NonDmclCtry(self):
		return self._NonDmclCtry

	@NonDmclCtry.setter
	def NonDmclCtry(self, value):
		self._NonDmclCtry = value if type(value) != base_types.auto else self.make_default("NonDmclCtry")

	@NonDmclCtry.deleter
	def NonDmclCtry(self):
		del self._NonDmclCtry
		self._NonDmclCtry = None

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if type(value) != base_types.auto else self.make_default("OfferTp")

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = None

	@property
	def OptnAvlbtySts(self):
		return self._OptnAvlbtySts

	@OptnAvlbtySts.setter
	def OptnAvlbtySts(self, value):
		self._OptnAvlbtySts = value if type(value) != base_types.auto else self.make_default("OptnAvlbtySts")

	@OptnAvlbtySts.deleter
	def OptnAvlbtySts(self):
		del self._OptnAvlbtySts
		self._OptnAvlbtySts = None

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if type(value) != base_types.auto else self.make_default("OptnFeatrs")

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if type(value) != base_types.auto else self.make_default("PrdDtls")

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def PrratnBlwMinQty(self):
		return self._PrratnBlwMinQty

	@PrratnBlwMinQty.setter
	def PrratnBlwMinQty(self, value):
		self._PrratnBlwMinQty = value if type(value) != base_types.auto else self.make_default("PrratnBlwMinQty")

	@PrratnBlwMinQty.deleter
	def PrratnBlwMinQty(self):
		del self._PrratnBlwMinQty
		self._PrratnBlwMinQty = None

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != base_types.auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if type(value) != base_types.auto else self.make_default("SctiesMvmntDtls")

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != base_types.auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	@property
	def VldDmclCtry(self):
		return self._VldDmclCtry

	@VldDmclCtry.setter
	def VldDmclCtry(self, value):
		self._VldDmclCtry = value if type(value) != base_types.auto else self.make_default("VldDmclCtry")

	@VldDmclCtry.deleter
	def VldDmclCtry(self):
		del self._VldDmclCtry
		self._VldDmclCtry = None

	@property
	def WdrwlAllwdInd(self):
		return self._WdrwlAllwdInd

	@WdrwlAllwdInd.setter
	def WdrwlAllwdInd(self, value):
		self._WdrwlAllwdInd = value if type(value) != base_types.auto else self.make_default("WdrwlAllwdInd")

	@WdrwlAllwdInd.deleter
	def WdrwlAllwdInd(self):
		del self._WdrwlAllwdInd
		self._WdrwlAllwdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncPrtyLvl', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative64, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldOptnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BidRgTp', type=BidRangeType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnTp', type=BeneficiaryCertificationType15Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChngAllwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption113, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltPrcgOrStgInstr', type=DefaultProcessingOrStandingInstruction2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate108, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDmclCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAvlbtySts', type=OptionAvailabilityStatus4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat31Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice97, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnBlwMinQty', type=ProrationBelowMinimumQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecuritiesOption117, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption84, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldDmclCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlAllwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

