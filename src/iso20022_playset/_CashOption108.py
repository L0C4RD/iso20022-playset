# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionAmounts71 import CorporateActionAmounts71
from ._CorporateActionDate84 import CorporateActionDate84
from ._CountryCode import CountryCode
from ._CreditDebitCode import CreditDebitCode
from ._ForeignExchangeTerms39 import ForeignExchangeTerms39
from ._GenericIdentification30 import GenericIdentification30
from ._NonEligibleProceedsIndicator5Choice import NonEligibleProceedsIndicator5Choice
from ._PriceCalculationMethod2Choice import PriceCalculationMethod2Choice
from ._PriceDetails39 import PriceDetails39
from ._Rate44 import Rate44
from ._YesNoIndicator import YesNoIndicator

class CashOption108(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_CdtDbtInd", "_CtryOfIncmSrc", "_DtDtls", "_EstmtdRateInd", "_FXDtls", "_IncmTp", "_NRATaxRptblInd", "_NonElgblPrcdsInd", "_OthrIncmTp", "_PricClctnMtd", "_PricDtls", "_RateAndAmtDtls", "_XmptnTp"]
	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != base_types.auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def CtryOfIncmSrc(self):
		return self._CtryOfIncmSrc

	@CtryOfIncmSrc.setter
	def CtryOfIncmSrc(self, value):
		self._CtryOfIncmSrc = value if type(value) != base_types.auto else self.make_default("CtryOfIncmSrc")

	@CtryOfIncmSrc.deleter
	def CtryOfIncmSrc(self):
		del self._CtryOfIncmSrc
		self._CtryOfIncmSrc = None

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
	def EstmtdRateInd(self):
		return self._EstmtdRateInd

	@EstmtdRateInd.setter
	def EstmtdRateInd(self, value):
		self._EstmtdRateInd = value if type(value) != base_types.auto else self.make_default("EstmtdRateInd")

	@EstmtdRateInd.deleter
	def EstmtdRateInd(self):
		del self._EstmtdRateInd
		self._EstmtdRateInd = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def IncmTp(self):
		return self._IncmTp

	@IncmTp.setter
	def IncmTp(self, value):
		self._IncmTp = value if type(value) != base_types.auto else self.make_default("IncmTp")

	@IncmTp.deleter
	def IncmTp(self):
		del self._IncmTp
		self._IncmTp = None

	@property
	def NRATaxRptblInd(self):
		return self._NRATaxRptblInd

	@NRATaxRptblInd.setter
	def NRATaxRptblInd(self, value):
		self._NRATaxRptblInd = value if type(value) != base_types.auto else self.make_default("NRATaxRptblInd")

	@NRATaxRptblInd.deleter
	def NRATaxRptblInd(self):
		del self._NRATaxRptblInd
		self._NRATaxRptblInd = None

	@property
	def NonElgblPrcdsInd(self):
		return self._NonElgblPrcdsInd

	@NonElgblPrcdsInd.setter
	def NonElgblPrcdsInd(self, value):
		self._NonElgblPrcdsInd = value if type(value) != base_types.auto else self.make_default("NonElgblPrcdsInd")

	@NonElgblPrcdsInd.deleter
	def NonElgblPrcdsInd(self):
		del self._NonElgblPrcdsInd
		self._NonElgblPrcdsInd = None

	@property
	def OthrIncmTp(self):
		return self._OthrIncmTp

	@OthrIncmTp.setter
	def OthrIncmTp(self, value):
		self._OthrIncmTp = value if type(value) != base_types.auto else self.make_default("OthrIncmTp")

	@OthrIncmTp.deleter
	def OthrIncmTp(self):
		del self._OthrIncmTp
		self._OthrIncmTp = None

	@property
	def PricClctnMtd(self):
		return self._PricClctnMtd

	@PricClctnMtd.setter
	def PricClctnMtd(self, value):
		self._PricClctnMtd = value if type(value) != base_types.auto else self.make_default("PricClctnMtd")

	@PricClctnMtd.deleter
	def PricClctnMtd(self):
		del self._PricClctnMtd
		self._PricClctnMtd = None

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
	def XmptnTp(self):
		return self._XmptnTp

	@XmptnTp.setter
	def XmptnTp(self, value):
		self._XmptnTp = value if type(value) != base_types.auto else self.make_default("XmptnTp")

	@XmptnTp.deleter
	def XmptnTp(self):
		del self._XmptnTp
		self._XmptnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts71, min=0, max=1, mutex_group=None, array=False),
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
		base_types.FieldEntry(name='RateAndAmtDtls', type=Rate44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification30, min=0, max=None, mutex_group=None, array=True),
	))