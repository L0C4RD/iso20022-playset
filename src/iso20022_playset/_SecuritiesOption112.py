# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import CorporateActionAmounts60
from . import CorporateActionPrice83
from . import CorporateActionRate125
from . import CountryCode
from . import CreditDebitCode
from . import FractionDispositionType27Choice
from . import GenericIdentification30
from . import IssuerOfferorTaxabilityIndicator2Choice
from . import NewSecuritiesIssuanceType6Code
from . import Quantity51Choice
from . import SafekeepingPlaceFormat41Choice
from . import SecurityDate25
from . import SecurityIdentification19
from . import SettlementParties129
from . import TemporaryFinancialInstrumentIndicator3Choice

class SecuritiesOption112(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_CcyOptn", "_CdtDbtInd", "_CtryOfIncmSrc", "_DlvrgSttlmPties", "_DtDtls", "_FinInstrmId", "_FrctnDspstn", "_IncmTp", "_IssrOfferrTaxbltyInd", "_NewSctiesIssncInd", "_OthrIncmTp", "_PricDtls", "_PstngQty", "_RateDtls", "_RcvgSttlmPties", "_SfkpgPlc", "_TempFinInstrmInd", "_XmptnTp"]
	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts60, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts60, False)

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
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def CtryOfIncmSrc(self):
		return self._CtryOfIncmSrc

	@CtryOfIncmSrc.setter
	def CtryOfIncmSrc(self, value):
		self._CtryOfIncmSrc = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIncmSrc', CountryCode, False)

	@CtryOfIncmSrc.deleter
	def CtryOfIncmSrc(self):
		del self._CtryOfIncmSrc
		self._CtryOfIncmSrc = base_types.UninitialisedField(self, 'CtryOfIncmSrc', CountryCode, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties129, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties129, False)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', SecurityDate25, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', SecurityDate25, False)

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
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType27Choice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType27Choice, False)

	@property
	def IncmTp(self):
		return self._IncmTp

	@IncmTp.setter
	def IncmTp(self, value):
		self._IncmTp = value if value is not None else base_types.UninitialisedField(self, 'IncmTp', GenericIdentification30, False)

	@IncmTp.deleter
	def IncmTp(self):
		del self._IncmTp
		self._IncmTp = base_types.UninitialisedField(self, 'IncmTp', GenericIdentification30, False)

	@property
	def IssrOfferrTaxbltyInd(self):
		return self._IssrOfferrTaxbltyInd

	@IssrOfferrTaxbltyInd.setter
	def IssrOfferrTaxbltyInd(self, value):
		self._IssrOfferrTaxbltyInd = value if value is not None else base_types.UninitialisedField(self, 'IssrOfferrTaxbltyInd', IssuerOfferorTaxabilityIndicator2Choice, False)

	@IssrOfferrTaxbltyInd.deleter
	def IssrOfferrTaxbltyInd(self):
		del self._IssrOfferrTaxbltyInd
		self._IssrOfferrTaxbltyInd = base_types.UninitialisedField(self, 'IssrOfferrTaxbltyInd', IssuerOfferorTaxabilityIndicator2Choice, False)

	@property
	def NewSctiesIssncInd(self):
		return self._NewSctiesIssncInd

	@NewSctiesIssncInd.setter
	def NewSctiesIssncInd(self, value):
		self._NewSctiesIssncInd = value if value is not None else base_types.UninitialisedField(self, 'NewSctiesIssncInd', NewSecuritiesIssuanceType6Code, False)

	@NewSctiesIssncInd.deleter
	def NewSctiesIssncInd(self):
		del self._NewSctiesIssncInd
		self._NewSctiesIssncInd = base_types.UninitialisedField(self, 'NewSctiesIssncInd', NewSecuritiesIssuanceType6Code, False)

	@property
	def OthrIncmTp(self):
		return self._OthrIncmTp

	@OthrIncmTp.setter
	def OthrIncmTp(self, value):
		self._OthrIncmTp = value if value is not None else base_types.UninitialisedField(self, 'OthrIncmTp', GenericIdentification30, True)

	@OthrIncmTp.deleter
	def OthrIncmTp(self):
		del self._OthrIncmTp
		self._OthrIncmTp = base_types.UninitialisedField(self, 'OthrIncmTp', GenericIdentification30, True)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice83, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', CorporateActionPrice83, False)

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if value is not None else base_types.UninitialisedField(self, 'PstngQty', Quantity51Choice, False)

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = base_types.UninitialisedField(self, 'PstngQty', Quantity51Choice, False)

	@property
	def RateDtls(self):
		return self._RateDtls

	@RateDtls.setter
	def RateDtls(self, value):
		self._RateDtls = value if value is not None else base_types.UninitialisedField(self, 'RateDtls', CorporateActionRate125, False)

	@RateDtls.deleter
	def RateDtls(self):
		del self._RateDtls
		self._RateDtls = base_types.UninitialisedField(self, 'RateDtls', CorporateActionRate125, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties129, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties129, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat41Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat41Choice, False)

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if value is not None else base_types.UninitialisedField(self, 'TempFinInstrmInd', TemporaryFinancialInstrumentIndicator3Choice, False)

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = base_types.UninitialisedField(self, 'TempFinInstrmInd', TemporaryFinancialInstrumentIndicator3Choice, False)

	@property
	def XmptnTp(self):
		return self._XmptnTp

	@XmptnTp.setter
	def XmptnTp(self, value):
		self._XmptnTp = value if value is not None else base_types.UninitialisedField(self, 'XmptnTp', GenericIdentification30, True)

	@XmptnTp.deleter
	def XmptnTp(self):
		del self._XmptnTp
		self._XmptnTp = base_types.UninitialisedField(self, 'XmptnTp', GenericIdentification30, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts60, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=SecurityDate25, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesIssncInd', type=NewSecuritiesIssuanceType6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateDtls', type=CorporateActionRate125, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties129, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat41Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=TemporaryFinancialInstrumentIndicator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))