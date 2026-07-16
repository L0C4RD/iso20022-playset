# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GrossDividendRateFormat41Choice
from . import InterestRateUsedForPaymentFormat18Choice
from . import NetDividendRateFormat43Choice
from . import RateAndAmountFormat69Choice
from . import RateAndAmountFormat70Choice
from . import RateFormat24Choice
from . import RateTypeAndAmountAndStatus33

class CorporateActionRate133(base_types._BaseFieldType):

	__slots__ = ["_AddtlTax", "_GrssDstrbtnRate", "_GrssIntrstRateUsdForPmt", "_MaxAllwdOvrsbcptRate", "_NetDstrbtnRate", "_PrratnRate", "_ScndLvlTax", "_TaxOnIncm", "_TaxblIncmPerDvddShr", "_WhldgTaxRate"]
	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if value is not None else base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat69Choice, False)

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat69Choice, False)

	@property
	def GrssDstrbtnRate(self):
		return self._GrssDstrbtnRate

	@GrssDstrbtnRate.setter
	def GrssDstrbtnRate(self, value):
		self._GrssDstrbtnRate = value if value is not None else base_types.UninitialisedField(self, 'GrssDstrbtnRate', GrossDividendRateFormat41Choice, True)

	@GrssDstrbtnRate.deleter
	def GrssDstrbtnRate(self):
		del self._GrssDstrbtnRate
		self._GrssDstrbtnRate = base_types.UninitialisedField(self, 'GrssDstrbtnRate', GrossDividendRateFormat41Choice, True)

	@property
	def GrssIntrstRateUsdForPmt(self):
		return self._GrssIntrstRateUsdForPmt

	@GrssIntrstRateUsdForPmt.setter
	def GrssIntrstRateUsdForPmt(self, value):
		self._GrssIntrstRateUsdForPmt = value if value is not None else base_types.UninitialisedField(self, 'GrssIntrstRateUsdForPmt', InterestRateUsedForPaymentFormat18Choice, True)

	@GrssIntrstRateUsdForPmt.deleter
	def GrssIntrstRateUsdForPmt(self):
		del self._GrssIntrstRateUsdForPmt
		self._GrssIntrstRateUsdForPmt = base_types.UninitialisedField(self, 'GrssIntrstRateUsdForPmt', InterestRateUsedForPaymentFormat18Choice, True)

	@property
	def MaxAllwdOvrsbcptRate(self):
		return self._MaxAllwdOvrsbcptRate

	@MaxAllwdOvrsbcptRate.setter
	def MaxAllwdOvrsbcptRate(self, value):
		self._MaxAllwdOvrsbcptRate = value if value is not None else base_types.UninitialisedField(self, 'MaxAllwdOvrsbcptRate', RateFormat24Choice, False)

	@MaxAllwdOvrsbcptRate.deleter
	def MaxAllwdOvrsbcptRate(self):
		del self._MaxAllwdOvrsbcptRate
		self._MaxAllwdOvrsbcptRate = base_types.UninitialisedField(self, 'MaxAllwdOvrsbcptRate', RateFormat24Choice, False)

	@property
	def NetDstrbtnRate(self):
		return self._NetDstrbtnRate

	@NetDstrbtnRate.setter
	def NetDstrbtnRate(self, value):
		self._NetDstrbtnRate = value if value is not None else base_types.UninitialisedField(self, 'NetDstrbtnRate', NetDividendRateFormat43Choice, True)

	@NetDstrbtnRate.deleter
	def NetDstrbtnRate(self):
		del self._NetDstrbtnRate
		self._NetDstrbtnRate = base_types.UninitialisedField(self, 'NetDstrbtnRate', NetDividendRateFormat43Choice, True)

	@property
	def PrratnRate(self):
		return self._PrratnRate

	@PrratnRate.setter
	def PrratnRate(self, value):
		self._PrratnRate = value if value is not None else base_types.UninitialisedField(self, 'PrratnRate', RateFormat24Choice, False)

	@PrratnRate.deleter
	def PrratnRate(self):
		del self._PrratnRate
		self._PrratnRate = base_types.UninitialisedField(self, 'PrratnRate', RateFormat24Choice, False)

	@property
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat70Choice, True)

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat70Choice, True)

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if value is not None else base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat69Choice, False)

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat69Choice, False)

	@property
	def TaxblIncmPerDvddShr(self):
		return self._TaxblIncmPerDvddShr

	@TaxblIncmPerDvddShr.setter
	def TaxblIncmPerDvddShr(self, value):
		self._TaxblIncmPerDvddShr = value if value is not None else base_types.UninitialisedField(self, 'TaxblIncmPerDvddShr', RateTypeAndAmountAndStatus33, True)

	@TaxblIncmPerDvddShr.deleter
	def TaxblIncmPerDvddShr(self):
		del self._TaxblIncmPerDvddShr
		self._TaxblIncmPerDvddShr = base_types.UninitialisedField(self, 'TaxblIncmPerDvddShr', RateTypeAndAmountAndStatus33, True)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat70Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat70Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat69Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDstrbtnRate', type=GrossDividendRateFormat41Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssIntrstRateUsdForPmt', type=InterestRateUsedForPaymentFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxAllwdOvrsbcptRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDstrbtnRate', type=NetDividendRateFormat43Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrratnRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat70Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxOnIncm', type=RateAndAmountFormat69Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblIncmPerDvddShr', type=RateTypeAndAmountAndStatus33, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat70Choice, min=0, max=None, mutex_group=None, array=True),
	))