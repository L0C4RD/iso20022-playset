from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._BeneficiaryCertificationType13Choice import BeneficiaryCertificationType13Choice
from ._CashOption108 import CashOption108
from ._CorporateActionDate104 import CorporateActionDate104
from ._CorporateActionNarrative66 import CorporateActionNarrative66
from ._CorporateActionOption37Choice import CorporateActionOption37Choice
from ._CorporateActionPeriod12 import CorporateActionPeriod12
from ._CorporateActionPrice87 import CorporateActionPrice87
from ._CorporateActionRate124 import CorporateActionRate124
from ._DecimalNumber import DecimalNumber
from ._Exact3NumericText import Exact3NumericText
from ._Exact3UpperCaseAlphaNumericText import Exact3UpperCaseAlphaNumericText
from ._ExtendedOptionFeature2Code import ExtendedOptionFeature2Code
from ._FractionDispositionType12Code import FractionDispositionType12Code
from ._FractionDispositionType26Choice import FractionDispositionType26Choice
from ._OfferTypeFormat14Choice import OfferTypeFormat14Choice
from ._OptionAvailabilityStatus3Choice import OptionAvailabilityStatus3Choice
from ._OptionFeaturesFormat28Choice import OptionFeaturesFormat28Choice
from ._ProrationBelowMinimumQuantity2Choice import ProrationBelowMinimumQuantity2Choice
from ._ProrationReturnQuantityTreatment1Code import ProrationReturnQuantityTreatment1Code
from ._SecuritiesOption114 import SecuritiesOption114
from ._SecuritiesOption81 import SecuritiesOption81
from ._SecurityIdentification19 import SecurityIdentification19
from ._TaxCategory1 import TaxCategory1
from ._YesNoIndicator import YesNoIndicator

class CorporateActionOption235(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AddtlInf", "_CcyOptn", "_CertfctnBrkdwnInd", "_CertfctnBrkdwnTp", "_CshMvmntDtls", "_DfltOptnInd", "_DtDtls", "_FinInstrmId", "_FrctnDspstn", "_OfferTp", "_OptnAvlbtySts", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_OvrsbcptChrgInd", "_PrdDtls", "_PricDtls", "_PrratnBlwMinQty", "_PrratnFrctn", "_PrratnRndgInd", "_PrratnRtrMinQtyTrtmnt", "_PrtctChrgInd", "_RateAndAmtDtls", "_SbcptChrgInd", "_SctiesMvmntDtls", "_SctiesQty", "_SplmtryOptnFeatrs", "_StepUpChrgInd", "_TaxCtgy", "_WdrwlAllwdInd"]
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
	def DfltOptnInd(self):
		return self._DfltOptnInd

	@DfltOptnInd.setter
	def DfltOptnInd(self, value):
		self._DfltOptnInd = value if type(value) != base_types.auto else self.make_default("DfltOptnInd")

	@DfltOptnInd.deleter
	def DfltOptnInd(self):
		del self._DfltOptnInd
		self._DfltOptnInd = None

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
	def OvrsbcptChrgInd(self):
		return self._OvrsbcptChrgInd

	@OvrsbcptChrgInd.setter
	def OvrsbcptChrgInd(self, value):
		self._OvrsbcptChrgInd = value if type(value) != base_types.auto else self.make_default("OvrsbcptChrgInd")

	@OvrsbcptChrgInd.deleter
	def OvrsbcptChrgInd(self):
		del self._OvrsbcptChrgInd
		self._OvrsbcptChrgInd = None

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
	def PrratnFrctn(self):
		return self._PrratnFrctn

	@PrratnFrctn.setter
	def PrratnFrctn(self, value):
		self._PrratnFrctn = value if type(value) != base_types.auto else self.make_default("PrratnFrctn")

	@PrratnFrctn.deleter
	def PrratnFrctn(self):
		del self._PrratnFrctn
		self._PrratnFrctn = None

	@property
	def PrratnRndgInd(self):
		return self._PrratnRndgInd

	@PrratnRndgInd.setter
	def PrratnRndgInd(self, value):
		self._PrratnRndgInd = value if type(value) != base_types.auto else self.make_default("PrratnRndgInd")

	@PrratnRndgInd.deleter
	def PrratnRndgInd(self):
		del self._PrratnRndgInd
		self._PrratnRndgInd = None

	@property
	def PrratnRtrMinQtyTrtmnt(self):
		return self._PrratnRtrMinQtyTrtmnt

	@PrratnRtrMinQtyTrtmnt.setter
	def PrratnRtrMinQtyTrtmnt(self, value):
		self._PrratnRtrMinQtyTrtmnt = value if type(value) != base_types.auto else self.make_default("PrratnRtrMinQtyTrtmnt")

	@PrratnRtrMinQtyTrtmnt.deleter
	def PrratnRtrMinQtyTrtmnt(self):
		del self._PrratnRtrMinQtyTrtmnt
		self._PrratnRtrMinQtyTrtmnt = None

	@property
	def PrtctChrgInd(self):
		return self._PrtctChrgInd

	@PrtctChrgInd.setter
	def PrtctChrgInd(self, value):
		self._PrtctChrgInd = value if type(value) != base_types.auto else self.make_default("PrtctChrgInd")

	@PrtctChrgInd.deleter
	def PrtctChrgInd(self):
		del self._PrtctChrgInd
		self._PrtctChrgInd = None

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
	def SbcptChrgInd(self):
		return self._SbcptChrgInd

	@SbcptChrgInd.setter
	def SbcptChrgInd(self, value):
		self._SbcptChrgInd = value if type(value) != base_types.auto else self.make_default("SbcptChrgInd")

	@SbcptChrgInd.deleter
	def SbcptChrgInd(self):
		del self._SbcptChrgInd
		self._SbcptChrgInd = None

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
	def SplmtryOptnFeatrs(self):
		return self._SplmtryOptnFeatrs

	@SplmtryOptnFeatrs.setter
	def SplmtryOptnFeatrs(self, value):
		self._SplmtryOptnFeatrs = value if type(value) != base_types.auto else self.make_default("SplmtryOptnFeatrs")

	@SplmtryOptnFeatrs.deleter
	def SplmtryOptnFeatrs(self):
		del self._SplmtryOptnFeatrs
		self._SplmtryOptnFeatrs = None

	@property
	def StepUpChrgInd(self):
		return self._StepUpChrgInd

	@StepUpChrgInd.setter
	def StepUpChrgInd(self, value):
		self._StepUpChrgInd = value if type(value) != base_types.auto else self.make_default("StepUpChrgInd")

	@StepUpChrgInd.deleter
	def StepUpChrgInd(self):
		del self._StepUpChrgInd
		self._StepUpChrgInd = None

	@property
	def TaxCtgy(self):
		return self._TaxCtgy

	@TaxCtgy.setter
	def TaxCtgy(self, value):
		self._TaxCtgy = value if type(value) != base_types.auto else self.make_default("TaxCtgy")

	@TaxCtgy.deleter
	def TaxCtgy(self):
		del self._TaxCtgy
		self._TaxCtgy = None

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
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative66, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnTp', type=BeneficiaryCertificationType13Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption108, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltOptnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate104, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferTypeFormat14Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAvlbtySts', type=OptionAvailabilityStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat28Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption37Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrsbcptChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice87, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnBlwMinQty', type=ProrationBelowMinimumQuantity2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnFrctn', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnRndgInd', type=FractionDispositionType12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnRtrMinQtyTrtmnt', type=ProrationReturnQuantityTreatment1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecuritiesOption114, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryOptnFeatrs', type=ExtendedOptionFeature2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StepUpChrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCtgy', type=TaxCategory1, min=0, max=99, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlAllwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

