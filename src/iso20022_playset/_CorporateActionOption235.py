# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BeneficiaryCertificationType13Choice
from . import CashOption108
from . import CorporateActionDate104
from . import CorporateActionNarrative66
from . import CorporateActionOption37Choice
from . import CorporateActionPeriod12
from . import CorporateActionPrice87
from . import CorporateActionRate124
from . import DecimalNumber
from . import Exact3NumericText
from . import Exact3UpperCaseAlphaNumericText
from . import ExtendedOptionFeature2Code
from . import FractionDispositionType12Code
from . import FractionDispositionType26Choice
from . import OfferTypeFormat14Choice
from . import OptionAvailabilityStatus3Choice
from . import OptionFeaturesFormat28Choice
from . import ProrationBelowMinimumQuantity2Choice
from . import ProrationReturnQuantityTreatment1Code
from . import SecuritiesOption114
from . import SecuritiesOption81
from . import SecurityIdentification19
from . import TaxCategory1
from . import YesNoIndicator

class CorporateActionOption235(base_types._BaseFieldType):

	__slots__ = ["_AccptncPrtyLvl", "_AddtlInf", "_CcyOptn", "_CertfctnBrkdwnInd", "_CertfctnBrkdwnTp", "_CshMvmntDtls", "_DfltOptnInd", "_DtDtls", "_FinInstrmId", "_FrctnDspstn", "_OfferTp", "_OptnAvlbtySts", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_OvrsbcptChrgInd", "_PrdDtls", "_PricDtls", "_PrratnBlwMinQty", "_PrratnFrctn", "_PrratnRndgInd", "_PrratnRtrMinQtyTrtmnt", "_PrtctChrgInd", "_RateAndAmtDtls", "_SbcptChrgInd", "_SctiesMvmntDtls", "_SctiesQty", "_SplmtryOptnFeatrs", "_StepUpChrgInd", "_TaxCtgy", "_WdrwlAllwdInd"]
	@property
	def AccptncPrtyLvl(self):
		return self._AccptncPrtyLvl

	@AccptncPrtyLvl.setter
	def AccptncPrtyLvl(self, value):
		self._AccptncPrtyLvl = value if value is not None else base_types.UninitialisedField(self, 'AccptncPrtyLvl', Exact3UpperCaseAlphaNumericText, False)

	@AccptncPrtyLvl.deleter
	def AccptncPrtyLvl(self):
		del self._AccptncPrtyLvl
		self._AccptncPrtyLvl = base_types.UninitialisedField(self, 'AccptncPrtyLvl', Exact3UpperCaseAlphaNumericText, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative66, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative66, False)

	@property
	def CcyOptn(self):
		return self._CcyOptn

	@CcyOptn.setter
	def CcyOptn(self, value):
		self._CcyOptn = value if value is not None else base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

	@CcyOptn.deleter
	def CcyOptn(self):
		del self._CcyOptn
		self._CcyOptn = base_types.UninitialisedField(self, 'CcyOptn', ActiveCurrencyCode, False)

	@property
	def CertfctnBrkdwnInd(self):
		return self._CertfctnBrkdwnInd

	@CertfctnBrkdwnInd.setter
	def CertfctnBrkdwnInd(self, value):
		self._CertfctnBrkdwnInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwnInd', YesNoIndicator, False)

	@CertfctnBrkdwnInd.deleter
	def CertfctnBrkdwnInd(self):
		del self._CertfctnBrkdwnInd
		self._CertfctnBrkdwnInd = base_types.UninitialisedField(self, 'CertfctnBrkdwnInd', YesNoIndicator, False)

	@property
	def CertfctnBrkdwnTp(self):
		return self._CertfctnBrkdwnTp

	@CertfctnBrkdwnTp.setter
	def CertfctnBrkdwnTp(self, value):
		self._CertfctnBrkdwnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnBrkdwnTp', BeneficiaryCertificationType13Choice, True)

	@CertfctnBrkdwnTp.deleter
	def CertfctnBrkdwnTp(self):
		del self._CertfctnBrkdwnTp
		self._CertfctnBrkdwnTp = base_types.UninitialisedField(self, 'CertfctnBrkdwnTp', BeneficiaryCertificationType13Choice, True)

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption108, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption108, True)

	@property
	def DfltOptnInd(self):
		return self._DfltOptnInd

	@DfltOptnInd.setter
	def DfltOptnInd(self, value):
		self._DfltOptnInd = value if value is not None else base_types.UninitialisedField(self, 'DfltOptnInd', YesNoIndicator, False)

	@DfltOptnInd.deleter
	def DfltOptnInd(self):
		del self._DfltOptnInd
		self._DfltOptnInd = base_types.UninitialisedField(self, 'DfltOptnInd', YesNoIndicator, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate104, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate104, False)

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
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType26Choice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType26Choice, False)

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if value is not None else base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat14Choice, True)

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = base_types.UninitialisedField(self, 'OfferTp', OfferTypeFormat14Choice, True)

	@property
	def OptnAvlbtySts(self):
		return self._OptnAvlbtySts

	@OptnAvlbtySts.setter
	def OptnAvlbtySts(self, value):
		self._OptnAvlbtySts = value if value is not None else base_types.UninitialisedField(self, 'OptnAvlbtySts', OptionAvailabilityStatus3Choice, False)

	@OptnAvlbtySts.deleter
	def OptnAvlbtySts(self):
		del self._OptnAvlbtySts
		self._OptnAvlbtySts = base_types.UninitialisedField(self, 'OptnAvlbtySts', OptionAvailabilityStatus3Choice, False)

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat28Choice, True)

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat28Choice, True)

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption37Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption37Choice, False)

	@property
	def OvrsbcptChrgInd(self):
		return self._OvrsbcptChrgInd

	@OvrsbcptChrgInd.setter
	def OvrsbcptChrgInd(self, value):
		self._OvrsbcptChrgInd = value if value is not None else base_types.UninitialisedField(self, 'OvrsbcptChrgInd', YesNoIndicator, False)

	@OvrsbcptChrgInd.deleter
	def OvrsbcptChrgInd(self):
		del self._OvrsbcptChrgInd
		self._OvrsbcptChrgInd = base_types.UninitialisedField(self, 'OvrsbcptChrgInd', YesNoIndicator, False)

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod12, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod12, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice87, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice87, False)

	@property
	def PrratnBlwMinQty(self):
		return self._PrratnBlwMinQty

	@PrratnBlwMinQty.setter
	def PrratnBlwMinQty(self, value):
		self._PrratnBlwMinQty = value if value is not None else base_types.UninitialisedField(self, 'PrratnBlwMinQty', ProrationBelowMinimumQuantity2Choice, False)

	@PrratnBlwMinQty.deleter
	def PrratnBlwMinQty(self):
		del self._PrratnBlwMinQty
		self._PrratnBlwMinQty = base_types.UninitialisedField(self, 'PrratnBlwMinQty', ProrationBelowMinimumQuantity2Choice, False)

	@property
	def PrratnFrctn(self):
		return self._PrratnFrctn

	@PrratnFrctn.setter
	def PrratnFrctn(self, value):
		self._PrratnFrctn = value if value is not None else base_types.UninitialisedField(self, 'PrratnFrctn', DecimalNumber, False)

	@PrratnFrctn.deleter
	def PrratnFrctn(self):
		del self._PrratnFrctn
		self._PrratnFrctn = base_types.UninitialisedField(self, 'PrratnFrctn', DecimalNumber, False)

	@property
	def PrratnRndgInd(self):
		return self._PrratnRndgInd

	@PrratnRndgInd.setter
	def PrratnRndgInd(self, value):
		self._PrratnRndgInd = value if value is not None else base_types.UninitialisedField(self, 'PrratnRndgInd', FractionDispositionType12Code, False)

	@PrratnRndgInd.deleter
	def PrratnRndgInd(self):
		del self._PrratnRndgInd
		self._PrratnRndgInd = base_types.UninitialisedField(self, 'PrratnRndgInd', FractionDispositionType12Code, False)

	@property
	def PrratnRtrMinQtyTrtmnt(self):
		return self._PrratnRtrMinQtyTrtmnt

	@PrratnRtrMinQtyTrtmnt.setter
	def PrratnRtrMinQtyTrtmnt(self, value):
		self._PrratnRtrMinQtyTrtmnt = value if value is not None else base_types.UninitialisedField(self, 'PrratnRtrMinQtyTrtmnt', ProrationReturnQuantityTreatment1Code, False)

	@PrratnRtrMinQtyTrtmnt.deleter
	def PrratnRtrMinQtyTrtmnt(self):
		del self._PrratnRtrMinQtyTrtmnt
		self._PrratnRtrMinQtyTrtmnt = base_types.UninitialisedField(self, 'PrratnRtrMinQtyTrtmnt', ProrationReturnQuantityTreatment1Code, False)

	@property
	def PrtctChrgInd(self):
		return self._PrtctChrgInd

	@PrtctChrgInd.setter
	def PrtctChrgInd(self, value):
		self._PrtctChrgInd = value if value is not None else base_types.UninitialisedField(self, 'PrtctChrgInd', YesNoIndicator, False)

	@PrtctChrgInd.deleter
	def PrtctChrgInd(self):
		del self._PrtctChrgInd
		self._PrtctChrgInd = base_types.UninitialisedField(self, 'PrtctChrgInd', YesNoIndicator, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate124, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate124, False)

	@property
	def SbcptChrgInd(self):
		return self._SbcptChrgInd

	@SbcptChrgInd.setter
	def SbcptChrgInd(self, value):
		self._SbcptChrgInd = value if value is not None else base_types.UninitialisedField(self, 'SbcptChrgInd', YesNoIndicator, False)

	@SbcptChrgInd.deleter
	def SbcptChrgInd(self):
		del self._SbcptChrgInd
		self._SbcptChrgInd = base_types.UninitialisedField(self, 'SbcptChrgInd', YesNoIndicator, False)

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption114, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption114, True)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', SecuritiesOption81, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', SecuritiesOption81, False)

	@property
	def SplmtryOptnFeatrs(self):
		return self._SplmtryOptnFeatrs

	@SplmtryOptnFeatrs.setter
	def SplmtryOptnFeatrs(self, value):
		self._SplmtryOptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'SplmtryOptnFeatrs', ExtendedOptionFeature2Code, True)

	@SplmtryOptnFeatrs.deleter
	def SplmtryOptnFeatrs(self):
		del self._SplmtryOptnFeatrs
		self._SplmtryOptnFeatrs = base_types.UninitialisedField(self, 'SplmtryOptnFeatrs', ExtendedOptionFeature2Code, True)

	@property
	def StepUpChrgInd(self):
		return self._StepUpChrgInd

	@StepUpChrgInd.setter
	def StepUpChrgInd(self, value):
		self._StepUpChrgInd = value if value is not None else base_types.UninitialisedField(self, 'StepUpChrgInd', YesNoIndicator, False)

	@StepUpChrgInd.deleter
	def StepUpChrgInd(self):
		del self._StepUpChrgInd
		self._StepUpChrgInd = base_types.UninitialisedField(self, 'StepUpChrgInd', YesNoIndicator, False)

	@property
	def TaxCtgy(self):
		return self._TaxCtgy

	@TaxCtgy.setter
	def TaxCtgy(self, value):
		self._TaxCtgy = value if value is not None else base_types.UninitialisedField(self, 'TaxCtgy', TaxCategory1, True)

	@TaxCtgy.deleter
	def TaxCtgy(self):
		del self._TaxCtgy
		self._TaxCtgy = base_types.UninitialisedField(self, 'TaxCtgy', TaxCategory1, True)

	@property
	def WdrwlAllwdInd(self):
		return self._WdrwlAllwdInd

	@WdrwlAllwdInd.setter
	def WdrwlAllwdInd(self, value):
		self._WdrwlAllwdInd = value if value is not None else base_types.UninitialisedField(self, 'WdrwlAllwdInd', YesNoIndicator, False)

	@WdrwlAllwdInd.deleter
	def WdrwlAllwdInd(self):
		del self._WdrwlAllwdInd
		self._WdrwlAllwdInd = base_types.UninitialisedField(self, 'WdrwlAllwdInd', YesNoIndicator, False)

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