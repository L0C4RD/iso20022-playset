# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BeneficiaryCertificationType13Choice
from . import BidRangeType1Choice
from . import CashOption116
from . import CorporateActionDate110
from . import CorporateActionNarrative59
from . import CorporateActionOption37Choice
from . import CorporateActionPeriod18
from . import CorporateActionPrice87
from . import CorporateActionRate139
from . import CountryCode
from . import DefaultProcessingOrStandingInstruction2Choice
from . import Exact3NumericText
from . import FractionDispositionType26Choice
from . import OptionAvailabilityStatus3Choice
from . import OptionFeaturesFormat32Choice
from . import ProrationBelowMinimumQuantity3Choice
from . import SecuritiesOption121
from . import SecuritiesOption81
from . import SecurityIdentification19
from . import YesNoIndicator

class CorporateActionOption251(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ApldOptnInd", "_BidRgTp", "_CcyOptn", "_CertfctnBrkdwnInd", "_CertfctnBrkdwnTp", "_ChngAllwdInd", "_ChrgsApldInd", "_CshMvmntDtls", "_DfltPrcgOrStgInstr", "_DtDtls", "_FinInstrmId", "_FrctnDspstn", "_NonDmclCtry", "_OptnAvlbtySts", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_PrdDtls", "_PricDtls", "_PrratnBlwMinQty", "_RateAndAmtDtls", "_SctiesMvmntDtls", "_SctiesQty", "_VldDmclCtry", "_WdrwlAllwdInd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative59, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative59, False)

	@property
	def ApldOptnInd(self):
		return self._ApldOptnInd

	@ApldOptnInd.setter
	def ApldOptnInd(self, value):
		self._ApldOptnInd = value if value is not None else base_types.UninitialisedField(self, 'ApldOptnInd', YesNoIndicator, False)

	@ApldOptnInd.deleter
	def ApldOptnInd(self):
		del self._ApldOptnInd
		self._ApldOptnInd = base_types.UninitialisedField(self, 'ApldOptnInd', YesNoIndicator, False)

	@property
	def BidRgTp(self):
		return self._BidRgTp

	@BidRgTp.setter
	def BidRgTp(self, value):
		self._BidRgTp = value if value is not None else base_types.UninitialisedField(self, 'BidRgTp', BidRangeType1Choice, False)

	@BidRgTp.deleter
	def BidRgTp(self):
		del self._BidRgTp
		self._BidRgTp = base_types.UninitialisedField(self, 'BidRgTp', BidRangeType1Choice, False)

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
	def ChngAllwdInd(self):
		return self._ChngAllwdInd

	@ChngAllwdInd.setter
	def ChngAllwdInd(self, value):
		self._ChngAllwdInd = value if value is not None else base_types.UninitialisedField(self, 'ChngAllwdInd', YesNoIndicator, False)

	@ChngAllwdInd.deleter
	def ChngAllwdInd(self):
		del self._ChngAllwdInd
		self._ChngAllwdInd = base_types.UninitialisedField(self, 'ChngAllwdInd', YesNoIndicator, False)

	@property
	def ChrgsApldInd(self):
		return self._ChrgsApldInd

	@ChrgsApldInd.setter
	def ChrgsApldInd(self, value):
		self._ChrgsApldInd = value if value is not None else base_types.UninitialisedField(self, 'ChrgsApldInd', YesNoIndicator, False)

	@ChrgsApldInd.deleter
	def ChrgsApldInd(self):
		del self._ChrgsApldInd
		self._ChrgsApldInd = base_types.UninitialisedField(self, 'ChrgsApldInd', YesNoIndicator, False)

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption116, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption116, True)

	@property
	def DfltPrcgOrStgInstr(self):
		return self._DfltPrcgOrStgInstr

	@DfltPrcgOrStgInstr.setter
	def DfltPrcgOrStgInstr(self, value):
		self._DfltPrcgOrStgInstr = value if value is not None else base_types.UninitialisedField(self, 'DfltPrcgOrStgInstr', DefaultProcessingOrStandingInstruction2Choice, False)

	@DfltPrcgOrStgInstr.deleter
	def DfltPrcgOrStgInstr(self):
		del self._DfltPrcgOrStgInstr
		self._DfltPrcgOrStgInstr = base_types.UninitialisedField(self, 'DfltPrcgOrStgInstr', DefaultProcessingOrStandingInstruction2Choice, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate110, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate110, False)

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
	def NonDmclCtry(self):
		return self._NonDmclCtry

	@NonDmclCtry.setter
	def NonDmclCtry(self, value):
		self._NonDmclCtry = value if value is not None else base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, True)

	@NonDmclCtry.deleter
	def NonDmclCtry(self):
		del self._NonDmclCtry
		self._NonDmclCtry = base_types.UninitialisedField(self, 'NonDmclCtry', CountryCode, True)

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
		self._OptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat32Choice, True)

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeaturesFormat32Choice, True)

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
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod18, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod18, False)

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
		self._PrratnBlwMinQty = value if value is not None else base_types.UninitialisedField(self, 'PrratnBlwMinQty', ProrationBelowMinimumQuantity3Choice, False)

	@PrratnBlwMinQty.deleter
	def PrratnBlwMinQty(self):
		del self._PrratnBlwMinQty
		self._PrratnBlwMinQty = base_types.UninitialisedField(self, 'PrratnBlwMinQty', ProrationBelowMinimumQuantity3Choice, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate139, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate139, False)

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption121, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecuritiesOption121, True)

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
	def VldDmclCtry(self):
		return self._VldDmclCtry

	@VldDmclCtry.setter
	def VldDmclCtry(self, value):
		self._VldDmclCtry = value if value is not None else base_types.UninitialisedField(self, 'VldDmclCtry', CountryCode, True)

	@VldDmclCtry.deleter
	def VldDmclCtry(self):
		del self._VldDmclCtry
		self._VldDmclCtry = base_types.UninitialisedField(self, 'VldDmclCtry', CountryCode, True)

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
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldOptnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BidRgTp', type=BidRangeType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnBrkdwnTp', type=BeneficiaryCertificationType13Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChngAllwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption116, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltPrcgOrStgInstr', type=DefaultProcessingOrStandingInstruction2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate110, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonDmclCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAvlbtySts', type=OptionAvailabilityStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeaturesFormat32Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption37Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice87, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnBlwMinQty', type=ProrationBelowMinimumQuantity3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecuritiesOption121, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesQty', type=SecuritiesOption81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldDmclCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlAllwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))