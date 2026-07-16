# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification2Choice
from . import BeneficiaryCertificationType1FormatChoice
from . import CashOption1
from . import CorporateActionAgent1
from . import CorporateActionDate4
from . import CorporateActionEventStatus2FormatChoice
from . import CorporateActionNarrative1
from . import CorporateActionOption1FormatChoice
from . import CorporateActionPeriod2
from . import CorporateActionPrice1
from . import CorporateActionRate2
from . import Exact3NumericText
from . import FractionDispositionType1FormatChoice
from . import IntermediateSecurityDistributionType1FormatChoice
from . import Max35Text
from . import OfferType1FormatChoice
from . import OptionFeatures1FormatChoice
from . import SecurityIdentification7
from . import SecurityOption1
from . import YesNoIndicator

class CorporateActionOption1(base_types._BaseFieldType):

	__slots__ = ["_AgtCshAcctId", "_AgtSctiesAcctId", "_AssntdLineSctyId", "_CertfctnInd", "_CertfctnTp", "_ChngAllwdInd", "_CorpActnAddtlInf", "_CorpActnOthrAgtDtls", "_CshMvmntDtls", "_DtDtls", "_FrctnDspstn", "_IntrmdtSctiesDstrbtnTp", "_OfferTp", "_OptnAvlbtySts", "_OptnFeatrs", "_OptnNb", "_OptnTp", "_PrdDtls", "_PricDtls", "_RateAndAmtDtls", "_RedChrgsApldInd", "_SctiesMvmntDtls", "_WdrwlAllwdInd"]
	@property
	def AgtCshAcctId(self):
		return self._AgtCshAcctId

	@AgtCshAcctId.setter
	def AgtCshAcctId(self, value):
		self._AgtCshAcctId = value if value is not None else base_types.UninitialisedField(self, 'AgtCshAcctId', AccountIdentification2Choice, False)

	@AgtCshAcctId.deleter
	def AgtCshAcctId(self):
		del self._AgtCshAcctId
		self._AgtCshAcctId = base_types.UninitialisedField(self, 'AgtCshAcctId', AccountIdentification2Choice, False)

	@property
	def AgtSctiesAcctId(self):
		return self._AgtSctiesAcctId

	@AgtSctiesAcctId.setter
	def AgtSctiesAcctId(self, value):
		self._AgtSctiesAcctId = value if value is not None else base_types.UninitialisedField(self, 'AgtSctiesAcctId', Max35Text, False)

	@AgtSctiesAcctId.deleter
	def AgtSctiesAcctId(self):
		del self._AgtSctiesAcctId
		self._AgtSctiesAcctId = base_types.UninitialisedField(self, 'AgtSctiesAcctId', Max35Text, False)

	@property
	def AssntdLineSctyId(self):
		return self._AssntdLineSctyId

	@AssntdLineSctyId.setter
	def AssntdLineSctyId(self, value):
		self._AssntdLineSctyId = value if value is not None else base_types.UninitialisedField(self, 'AssntdLineSctyId', SecurityIdentification7, False)

	@AssntdLineSctyId.deleter
	def AssntdLineSctyId(self):
		del self._AssntdLineSctyId
		self._AssntdLineSctyId = base_types.UninitialisedField(self, 'AssntdLineSctyId', SecurityIdentification7, False)

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', BeneficiaryCertificationType1FormatChoice, False)

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
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionNarrative1, False)

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = base_types.UninitialisedField(self, 'CorpActnAddtlInf', CorporateActionNarrative1, False)

	@property
	def CorpActnOthrAgtDtls(self):
		return self._CorpActnOthrAgtDtls

	@CorpActnOthrAgtDtls.setter
	def CorpActnOthrAgtDtls(self, value):
		self._CorpActnOthrAgtDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnOthrAgtDtls', CorporateActionAgent1, True)

	@CorpActnOthrAgtDtls.deleter
	def CorpActnOthrAgtDtls(self):
		del self._CorpActnOthrAgtDtls
		self._CorpActnOthrAgtDtls = base_types.UninitialisedField(self, 'CorpActnOthrAgtDtls', CorporateActionAgent1, True)

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption1, True)

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = base_types.UninitialisedField(self, 'CshMvmntDtls', CashOption1, True)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate4, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate4, False)

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType1FormatChoice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType1FormatChoice, False)

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if value is not None else base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecurityDistributionType1FormatChoice, False)

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = base_types.UninitialisedField(self, 'IntrmdtSctiesDstrbtnTp', IntermediateSecurityDistributionType1FormatChoice, False)

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if value is not None else base_types.UninitialisedField(self, 'OfferTp', OfferType1FormatChoice, True)

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = base_types.UninitialisedField(self, 'OfferTp', OfferType1FormatChoice, True)

	@property
	def OptnAvlbtySts(self):
		return self._OptnAvlbtySts

	@OptnAvlbtySts.setter
	def OptnAvlbtySts(self, value):
		self._OptnAvlbtySts = value if value is not None else base_types.UninitialisedField(self, 'OptnAvlbtySts', CorporateActionEventStatus2FormatChoice, False)

	@OptnAvlbtySts.deleter
	def OptnAvlbtySts(self):
		del self._OptnAvlbtySts
		self._OptnAvlbtySts = base_types.UninitialisedField(self, 'OptnAvlbtySts', CorporateActionEventStatus2FormatChoice, False)

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if value is not None else base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeatures1FormatChoice, True)

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = base_types.UninitialisedField(self, 'OptnFeatrs', OptionFeatures1FormatChoice, True)

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
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if value is not None else base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod2, False)

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = base_types.UninitialisedField(self, 'PrdDtls', CorporateActionPeriod2, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice1, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice1, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate2, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', CorporateActionRate2, False)

	@property
	def RedChrgsApldInd(self):
		return self._RedChrgsApldInd

	@RedChrgsApldInd.setter
	def RedChrgsApldInd(self, value):
		self._RedChrgsApldInd = value if value is not None else base_types.UninitialisedField(self, 'RedChrgsApldInd', YesNoIndicator, False)

	@RedChrgsApldInd.deleter
	def RedChrgsApldInd(self):
		del self._RedChrgsApldInd
		self._RedChrgsApldInd = base_types.UninitialisedField(self, 'RedChrgsApldInd', YesNoIndicator, False)

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecurityOption1, True)

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = base_types.UninitialisedField(self, 'SctiesMvmntDtls', SecurityOption1, True)

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
		base_types.FieldEntry(name='AgtCshAcctId', type=AccountIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtSctiesAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssntdLineSctyId', type=SecurityIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngAllwdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnAddtlInf', type=CorporateActionNarrative1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOthrAgtDtls', type=CorporateActionAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecurityDistributionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OfferTp', type=OfferType1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAvlbtySts', type=CorporateActionEventStatus2FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeatures1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecurityOption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlAllwdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))