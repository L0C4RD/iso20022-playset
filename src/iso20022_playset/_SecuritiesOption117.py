# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._CorporateActionAmounts61 import CorporateActionAmounts61
from ._CorporateActionPrice98 import CorporateActionPrice98
from ._CorporateActionRate137 import CorporateActionRate137
from ._CountryCode import CountryCode
from ._CreditDebitCode import CreditDebitCode
from ._FinancialInstrumentAttributes137 import FinancialInstrumentAttributes137
from ._FractionDispositionType31Choice import FractionDispositionType31Choice
from ._GenericIdentification47 import GenericIdentification47
from ._IssuerOfferorTaxabilityIndicator1Choice import IssuerOfferorTaxabilityIndicator1Choice
from ._NewSecuritiesIssuanceType5Code import NewSecuritiesIssuanceType5Code
from ._NonEligibleProceedsIndicator6Choice import NonEligibleProceedsIndicator6Choice
from ._Period6Choice import Period6Choice
from ._Quantity54Choice import Quantity54Choice
from ._SafekeepingPlaceFormat56Choice import SafekeepingPlaceFormat56Choice
from ._SecurityDate24 import SecurityDate24
from ._TemporaryFinancialInstrumentIndicator4Choice import TemporaryFinancialInstrumentIndicator4Choice

class SecuritiesOption117(base_types._BaseFieldType):

	__slots__ = ["_AmtDtls", "_CcyOptn", "_CdtDbtInd", "_CtryOfIncmSrc", "_DtDtls", "_EntitldQty", "_FrctnDspstn", "_IncmTp", "_IssrOfferrTaxbltyInd", "_NewSctiesIssncInd", "_NonElgblPrcdsInd", "_OthrIncmTp", "_PricDtls", "_RateDtls", "_SctyDtls", "_SfkpgPlc", "_TempFinInstrmInd", "_TradgPrd", "_XmptnTp"]
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
	def EntitldQty(self):
		return self._EntitldQty

	@EntitldQty.setter
	def EntitldQty(self, value):
		self._EntitldQty = value if type(value) != base_types.auto else self.make_default("EntitldQty")

	@EntitldQty.deleter
	def EntitldQty(self):
		del self._EntitldQty
		self._EntitldQty = None

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
	def IssrOfferrTaxbltyInd(self):
		return self._IssrOfferrTaxbltyInd

	@IssrOfferrTaxbltyInd.setter
	def IssrOfferrTaxbltyInd(self, value):
		self._IssrOfferrTaxbltyInd = value if type(value) != base_types.auto else self.make_default("IssrOfferrTaxbltyInd")

	@IssrOfferrTaxbltyInd.deleter
	def IssrOfferrTaxbltyInd(self):
		del self._IssrOfferrTaxbltyInd
		self._IssrOfferrTaxbltyInd = None

	@property
	def NewSctiesIssncInd(self):
		return self._NewSctiesIssncInd

	@NewSctiesIssncInd.setter
	def NewSctiesIssncInd(self, value):
		self._NewSctiesIssncInd = value if type(value) != base_types.auto else self.make_default("NewSctiesIssncInd")

	@NewSctiesIssncInd.deleter
	def NewSctiesIssncInd(self):
		del self._NewSctiesIssncInd
		self._NewSctiesIssncInd = None

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
	def RateDtls(self):
		return self._RateDtls

	@RateDtls.setter
	def RateDtls(self, value):
		self._RateDtls = value if type(value) != base_types.auto else self.make_default("RateDtls")

	@RateDtls.deleter
	def RateDtls(self):
		del self._RateDtls
		self._RateDtls = None

	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if type(value) != base_types.auto else self.make_default("SctyDtls")

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def TempFinInstrmInd(self):
		return self._TempFinInstrmInd

	@TempFinInstrmInd.setter
	def TempFinInstrmInd(self, value):
		self._TempFinInstrmInd = value if type(value) != base_types.auto else self.make_default("TempFinInstrmInd")

	@TempFinInstrmInd.deleter
	def TempFinInstrmInd(self):
		del self._TempFinInstrmInd
		self._TempFinInstrmInd = None

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if type(value) != base_types.auto else self.make_default("TradgPrd")

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = None

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
		base_types.FieldEntry(name='AmtDtls', type=CorporateActionAmounts61, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOptn', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIncmSrc', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=SecurityDate24, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitldQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmTp', type=GenericIdentification47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOfferrTaxbltyInd', type=IssuerOfferorTaxabilityIndicator1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSctiesIssncInd', type=NewSecuritiesIssuanceType5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonElgblPrcdsInd', type=NonEligibleProceedsIndicator6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrIncmTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricDtls', type=CorporateActionPrice98, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateDtls', type=CorporateActionRate137, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=FinancialInstrumentAttributes137, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat56Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TempFinInstrmInd', type=TemporaryFinancialInstrumentIndicator4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnTp', type=GenericIdentification47, min=0, max=None, mutex_group=None, array=True),
	))