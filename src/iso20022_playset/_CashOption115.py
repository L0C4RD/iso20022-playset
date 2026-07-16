# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionAmounts77
from . import CorporateActionDate84
from . import CountryCode
from . import CreditDebitCode
from . import ForeignExchangeTerms39
from . import GenericIdentification30
from . import NonEligibleProceedsIndicator5Choice
from . import PriceCalculationMethod2Choice
from . import PriceDetails39
from . import Rate49
from . import YesNoIndicator

class CashOption115(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_CdtDbtInd", "_CtryOfIncmSrc", "_DtDtls", "_EstmtdRateInd", "_FXDtls", "_IncmTp", "_NRATaxRptblInd", "_NonElgblPrcdsInd", "_OthrIncmTp", "_PricClctnMtd", "_PricDtls", "_RateAndAmtDtls", "_XmptnTp"]
	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts77, False)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', CorporateActionAmounts77, False)

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
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate84, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate84, False)

	@property
	def EstmtdRateInd(self):
		return self._EstmtdRateInd

	@EstmtdRateInd.setter
	def EstmtdRateInd(self, value):
		self._EstmtdRateInd = value if value is not None else base_types.UninitialisedField(self, 'EstmtdRateInd', YesNoIndicator, False)

	@EstmtdRateInd.deleter
	def EstmtdRateInd(self):
		del self._EstmtdRateInd
		self._EstmtdRateInd = base_types.UninitialisedField(self, 'EstmtdRateInd', YesNoIndicator, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms39, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms39, False)

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
	def NRATaxRptblInd(self):
		return self._NRATaxRptblInd

	@NRATaxRptblInd.setter
	def NRATaxRptblInd(self, value):
		self._NRATaxRptblInd = value if value is not None else base_types.UninitialisedField(self, 'NRATaxRptblInd', YesNoIndicator, False)

	@NRATaxRptblInd.deleter
	def NRATaxRptblInd(self):
		del self._NRATaxRptblInd
		self._NRATaxRptblInd = base_types.UninitialisedField(self, 'NRATaxRptblInd', YesNoIndicator, False)

	@property
	def NonElgblPrcdsInd(self):
		return self._NonElgblPrcdsInd

	@NonElgblPrcdsInd.setter
	def NonElgblPrcdsInd(self, value):
		self._NonElgblPrcdsInd = value if value is not None else base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator5Choice, False)

	@NonElgblPrcdsInd.deleter
	def NonElgblPrcdsInd(self):
		del self._NonElgblPrcdsInd
		self._NonElgblPrcdsInd = base_types.UninitialisedField(self, 'NonElgblPrcdsInd', NonEligibleProceedsIndicator5Choice, False)

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
	def PricClctnMtd(self):
		return self._PricClctnMtd

	@PricClctnMtd.setter
	def PricClctnMtd(self, value):
		self._PricClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'PricClctnMtd', PriceCalculationMethod2Choice, False)

	@PricClctnMtd.deleter
	def PricClctnMtd(self):
		del self._PricClctnMtd
		self._PricClctnMtd = base_types.UninitialisedField(self, 'PricClctnMtd', PriceCalculationMethod2Choice, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceDetails39, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceDetails39, False)

	@property
	def RateAndAmtDtls(self):
		return self._RateAndAmtDtls

	@RateAndAmtDtls.setter
	def RateAndAmtDtls(self, value):
		self._RateAndAmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate49, False)

	@RateAndAmtDtls.deleter
	def RateAndAmtDtls(self):
		del self._RateAndAmtDtls
		self._RateAndAmtDtls = base_types.UninitialisedField(self, 'RateAndAmtDtls', Rate49, False)

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
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts77, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate84, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NRATaxRptblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricClctnMtd', type=PriceCalculationMethod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceDetails39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))