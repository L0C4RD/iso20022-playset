from . import base_types
from ._RateFormat24Choice import RateFormat24Choice
from ._GrossDividendRateFormat36Choice import GrossDividendRateFormat36Choice
from ._RateAndAmountFormat57Choice import RateAndAmountFormat57Choice
from ._RateAndAmountFormat56Choice import RateAndAmountFormat56Choice
from ._NetDividendRateFormat38Choice import NetDividendRateFormat38Choice
from ._InterestRateUsedForPaymentFormat11Choice import InterestRateUsedForPaymentFormat11Choice
from ._RateTypeAndAmountAndStatus26 import RateTypeAndAmountAndStatus26

class CorporateActionRate119(base_types._BaseFieldType):

	__slots__ = ["_GrssDstrbtnRate", "_AddtlTax", "_TaxOnIncm", "_PrratnRate", "_ScndLvlTax", "_NetDstrbtnRate", "_MaxAllwdOvrsbcptRate", "_TaxblIncmPerDvddShr", "_WhldgTaxRate", "_GrssIntrstRateUsdForPmt"]
	@property
	def GrssDstrbtnRate(self):
		return self._GrssDstrbtnRate

	@GrssDstrbtnRate.setter
	def GrssDstrbtnRate(self, value):
		self._GrssDstrbtnRate = value if type(value) != base_types.auto else self.make_default("GrssDstrbtnRate")

	@GrssDstrbtnRate.deleter
	def GrssDstrbtnRate(self):
		del self._GrssDstrbtnRate
		self._GrssDstrbtnRate = None

	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if type(value) != base_types.auto else self.make_default("AddtlTax")

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = None

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if type(value) != base_types.auto else self.make_default("TaxOnIncm")

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = None

	@property
	def PrratnRate(self):
		return self._PrratnRate

	@PrratnRate.setter
	def PrratnRate(self, value):
		self._PrratnRate = value if type(value) != base_types.auto else self.make_default("PrratnRate")

	@PrratnRate.deleter
	def PrratnRate(self):
		del self._PrratnRate
		self._PrratnRate = None

	@property
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if type(value) != base_types.auto else self.make_default("ScndLvlTax")

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = None

	@property
	def NetDstrbtnRate(self):
		return self._NetDstrbtnRate

	@NetDstrbtnRate.setter
	def NetDstrbtnRate(self, value):
		self._NetDstrbtnRate = value if type(value) != base_types.auto else self.make_default("NetDstrbtnRate")

	@NetDstrbtnRate.deleter
	def NetDstrbtnRate(self):
		del self._NetDstrbtnRate
		self._NetDstrbtnRate = None

	@property
	def MaxAllwdOvrsbcptRate(self):
		return self._MaxAllwdOvrsbcptRate

	@MaxAllwdOvrsbcptRate.setter
	def MaxAllwdOvrsbcptRate(self, value):
		self._MaxAllwdOvrsbcptRate = value if type(value) != base_types.auto else self.make_default("MaxAllwdOvrsbcptRate")

	@MaxAllwdOvrsbcptRate.deleter
	def MaxAllwdOvrsbcptRate(self):
		del self._MaxAllwdOvrsbcptRate
		self._MaxAllwdOvrsbcptRate = None

	@property
	def TaxblIncmPerDvddShr(self):
		return self._TaxblIncmPerDvddShr

	@TaxblIncmPerDvddShr.setter
	def TaxblIncmPerDvddShr(self, value):
		self._TaxblIncmPerDvddShr = value if type(value) != base_types.auto else self.make_default("TaxblIncmPerDvddShr")

	@TaxblIncmPerDvddShr.deleter
	def TaxblIncmPerDvddShr(self):
		del self._TaxblIncmPerDvddShr
		self._TaxblIncmPerDvddShr = None

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if type(value) != base_types.auto else self.make_default("WhldgTaxRate")

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = None

	@property
	def GrssIntrstRateUsdForPmt(self):
		return self._GrssIntrstRateUsdForPmt

	@GrssIntrstRateUsdForPmt.setter
	def GrssIntrstRateUsdForPmt(self, value):
		self._GrssIntrstRateUsdForPmt = value if type(value) != base_types.auto else self.make_default("GrssIntrstRateUsdForPmt")

	@GrssIntrstRateUsdForPmt.deleter
	def GrssIntrstRateUsdForPmt(self):
		del self._GrssIntrstRateUsdForPmt
		self._GrssIntrstRateUsdForPmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssDstrbtnRate', type=GrossDividendRateFormat36Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrratnRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat56Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetDstrbtnRate', type=NetDividendRateFormat38Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxAllwdOvrsbcptRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvddShr', type=RateTypeAndAmountAndStatus26, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat56Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssIntrstRateUsdForPmt', type=InterestRateUsedForPaymentFormat11Choice, min=0, max=None, mutex_group=None, array=True),
	))

