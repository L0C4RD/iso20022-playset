import base_types
import OfferType1FormatChoice
import CorporateActionPeriod2
import OptionFeatures1FormatChoice
import FractionDispositionType1FormatChoice
import BeneficiaryCertificationType1FormatChoice
import SecurityIdentification7
import CorporateActionAgent1
import CorporateActionOption1FormatChoice
import CashOption1
import YesNoIndicator
import Exact3NumericText
import Max35Text
import CorporateActionDate4
import CorporateActionEventStatus2FormatChoice
import IntermediateSecurityDistributionType1FormatChoice
import SecurityOption1
import CorporateActionRate2
import CorporateActionPrice1
import CorporateActionNarrative1
import AccountIdentification2Choice

class CorporateActionOption1(base_types._BaseFieldType):

	__slots__ = ["_PricDtls", "_ChngAllwdInd", "_AgtCshAcctId", "_CorpActnOthrAgtDtls", "_WdrwlAllwdInd", "_AssntdLineSctyId", "_OptnFeatrs", "_IntrmdtSctiesDstrbtnTp", "_CertfctnInd", "_OptnTp", "_CorpActnAddtlInf", "_CertfctnTp", "_RateAndAmtDtls", "_FrctnDspstn", "_SctiesMvmntDtls", "_OptnAvlbtySts", "_DtDtls", "_AgtSctiesAcctId", "_PrdDtls", "_RedChrgsApldInd", "_OptnNb", "_CshMvmntDtls", "_OfferTp"]
	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def ChngAllwdInd(self):
		return self._ChngAllwdInd

	@ChngAllwdInd.setter
	def ChngAllwdInd(self, value):
		self._ChngAllwdInd = value if type(value) != auto else self.make_default("ChngAllwdInd")

	@ChngAllwdInd.deleter
	def ChngAllwdInd(self):
		del self._ChngAllwdInd
		self._ChngAllwdInd = None

	@property
	def AgtCshAcctId(self):
		return self._AgtCshAcctId

	@AgtCshAcctId.setter
	def AgtCshAcctId(self, value):
		self._AgtCshAcctId = value if type(value) != auto else self.make_default("AgtCshAcctId")

	@AgtCshAcctId.deleter
	def AgtCshAcctId(self):
		del self._AgtCshAcctId
		self._AgtCshAcctId = None

	@property
	def CorpActnOthrAgtDtls(self):
		return self._CorpActnOthrAgtDtls

	@CorpActnOthrAgtDtls.setter
	def CorpActnOthrAgtDtls(self, value):
		self._CorpActnOthrAgtDtls = value if type(value) != auto else self.make_default("CorpActnOthrAgtDtls")

	@CorpActnOthrAgtDtls.deleter
	def CorpActnOthrAgtDtls(self):
		del self._CorpActnOthrAgtDtls
		self._CorpActnOthrAgtDtls = None

	@property
	def WdrwlAllwdInd(self):
		return self._WdrwlAllwdInd

	@WdrwlAllwdInd.setter
	def WdrwlAllwdInd(self, value):
		self._WdrwlAllwdInd = value if type(value) != auto else self.make_default("WdrwlAllwdInd")

	@WdrwlAllwdInd.deleter
	def WdrwlAllwdInd(self):
		del self._WdrwlAllwdInd
		self._WdrwlAllwdInd = None

	@property
	def AssntdLineSctyId(self):
		return self._AssntdLineSctyId

	@AssntdLineSctyId.setter
	def AssntdLineSctyId(self, value):
		self._AssntdLineSctyId = value if type(value) != auto else self.make_default("AssntdLineSctyId")

	@AssntdLineSctyId.deleter
	def AssntdLineSctyId(self):
		del self._AssntdLineSctyId
		self._AssntdLineSctyId = None

	@property
	def OptnFeatrs(self):
		return self._OptnFeatrs

	@OptnFeatrs.setter
	def OptnFeatrs(self, value):
		self._OptnFeatrs = value if type(value) != auto else self.make_default("OptnFeatrs")

	@OptnFeatrs.deleter
	def OptnFeatrs(self):
		del self._OptnFeatrs
		self._OptnFeatrs = None

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if type(value) != auto else self.make_default("IntrmdtSctiesDstrbtnTp")

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = None

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if type(value) != auto else self.make_default("CertfctnInd")

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def CorpActnAddtlInf(self):
		return self._CorpActnAddtlInf

	@CorpActnAddtlInf.setter
	def CorpActnAddtlInf(self, value):
		self._CorpActnAddtlInf = value if type(value) != auto else self.make_default("CorpActnAddtlInf")

	@CorpActnAddtlInf.deleter
	def CorpActnAddtlInf(self):
		del self._CorpActnAddtlInf
		self._CorpActnAddtlInf = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if type(value) != auto else self.make_default("RateAndAmtDtls")

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = None

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	@property
	def SctiesMvmntDtls(self):
		return self._SctiesMvmntDtls

	@SctiesMvmntDtls.setter
	def SctiesMvmntDtls(self, value):
		self._SctiesMvmntDtls = value if type(value) != auto else self.make_default("SctiesMvmntDtls")

	@SctiesMvmntDtls.deleter
	def SctiesMvmntDtls(self):
		del self._SctiesMvmntDtls
		self._SctiesMvmntDtls = None

	@property
	def OptnAvlbtySts(self):
		return self._OptnAvlbtySts

	@OptnAvlbtySts.setter
	def OptnAvlbtySts(self, value):
		self._OptnAvlbtySts = value if type(value) != auto else self.make_default("OptnAvlbtySts")

	@OptnAvlbtySts.deleter
	def OptnAvlbtySts(self):
		del self._OptnAvlbtySts
		self._OptnAvlbtySts = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

	@property
	def AgtSctiesAcctId(self):
		return self._AgtSctiesAcctId

	@AgtSctiesAcctId.setter
	def AgtSctiesAcctId(self, value):
		self._AgtSctiesAcctId = value if type(value) != auto else self.make_default("AgtSctiesAcctId")

	@AgtSctiesAcctId.deleter
	def AgtSctiesAcctId(self):
		del self._AgtSctiesAcctId
		self._AgtSctiesAcctId = None

	@property
	def PrdDtls(self):
		return self._PrdDtls

	@PrdDtls.setter
	def PrdDtls(self, value):
		self._PrdDtls = value if type(value) != auto else self.make_default("PrdDtls")

	@PrdDtls.deleter
	def PrdDtls(self):
		del self._PrdDtls
		self._PrdDtls = None

	@property
	def RedChrgsApldInd(self):
		return self._RedChrgsApldInd

	@RedChrgsApldInd.setter
	def RedChrgsApldInd(self, value):
		self._RedChrgsApldInd = value if type(value) != auto else self.make_default("RedChrgsApldInd")

	@RedChrgsApldInd.deleter
	def RedChrgsApldInd(self):
		del self._RedChrgsApldInd
		self._RedChrgsApldInd = None

	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def CshMvmntDtls(self):
		return self._CshMvmntDtls

	@CshMvmntDtls.setter
	def CshMvmntDtls(self, value):
		self._CshMvmntDtls = value if type(value) != auto else self.make_default("CshMvmntDtls")

	@CshMvmntDtls.deleter
	def CshMvmntDtls(self):
		del self._CshMvmntDtls
		self._CshMvmntDtls = None

	@property
	def OfferTp(self):
		return self._OfferTp

	@OfferTp.setter
	def OfferTp(self, value):
		self._OfferTp = value if type(value) != auto else self.make_default("OfferTp")

	@OfferTp.deleter
	def OfferTp(self):
		del self._OfferTp
		self._OfferTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngAllwdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCshAcctId', type=AccountIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOthrAgtDtls', type=CorporateActionAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlAllwdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssntdLineSctyId', type=SecurityIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnFeatrs', type=OptionFeatures1FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecurityDistributionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnAddtlInf', type=CorporateActionNarrative1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=BeneficiaryCertificationType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=CorporateActionRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntDtls', type=SecurityOption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnAvlbtySts', type=CorporateActionEventStatus2FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtSctiesAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdDtls', type=CorporateActionPeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedChrgsApldInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshMvmntDtls', type=CashOption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OfferTp', type=OfferType1FormatChoice, min=0, max=None, mutex_group=None, array=True),
	))

