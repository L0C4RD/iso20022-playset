# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import GrossDividendRateFormat37Choice
from . import InterestRateUsedForPaymentFormat12Choice
from . import NetDividendRateFormat40Choice
from . import Percentage14Rate
from . import RateAndAmountFormat55Choice
from . import RateAndAmountFormat59Choice
from . import RateAndAmountFormat62Choice
from . import RateFormat27Choice
from . import SolicitationFeeRateFormat12Choice

class Rate41(base_types._BaseFieldType):

	__slots__ = ["_AddtlTax", "_AplblRate", "_ChrgsFees", "_DmdRate", "_EarlySlctnFeeRate", "_EqulstnRate", "_FsclStmp", "_GrssDstrbtnRate", "_GrssIntrstRateUsdForPmt", "_NetDstrbtnRate", "_ScndLvlTax", "_SlctnFeeRate", "_TaxCdtRate", "_TaxOnIncm", "_TaxOnPrfts", "_TaxRclmRate", "_ThrdPtyIncntivRate", "_WhldgTaxRate"]
	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if value is not None else base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat59Choice, False)

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat59Choice, False)

	@property
	def AplblRate(self):
		return self._AplblRate

	@AplblRate.setter
	def AplblRate(self, value):
		self._AplblRate = value if value is not None else base_types.UninitialisedField(self, 'AplblRate', Percentage14Rate, False)

	@AplblRate.deleter
	def AplblRate(self):
		del self._AplblRate
		self._AplblRate = base_types.UninitialisedField(self, 'AplblRate', Percentage14Rate, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat59Choice, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat59Choice, False)

	@property
	def DmdRate(self):
		return self._DmdRate

	@DmdRate.setter
	def DmdRate(self, value):
		self._DmdRate = value if value is not None else base_types.UninitialisedField(self, 'DmdRate', RateAndAmountFormat62Choice, True)

	@DmdRate.deleter
	def DmdRate(self):
		del self._DmdRate
		self._DmdRate = base_types.UninitialisedField(self, 'DmdRate', RateAndAmountFormat62Choice, True)

	@property
	def EarlySlctnFeeRate(self):
		return self._EarlySlctnFeeRate

	@EarlySlctnFeeRate.setter
	def EarlySlctnFeeRate(self, value):
		self._EarlySlctnFeeRate = value if value is not None else base_types.UninitialisedField(self, 'EarlySlctnFeeRate', SolicitationFeeRateFormat12Choice, False)

	@EarlySlctnFeeRate.deleter
	def EarlySlctnFeeRate(self):
		del self._EarlySlctnFeeRate
		self._EarlySlctnFeeRate = base_types.UninitialisedField(self, 'EarlySlctnFeeRate', SolicitationFeeRateFormat12Choice, False)

	@property
	def EqulstnRate(self):
		return self._EqulstnRate

	@EqulstnRate.setter
	def EqulstnRate(self, value):
		self._EqulstnRate = value if value is not None else base_types.UninitialisedField(self, 'EqulstnRate', ActiveCurrencyAnd13DecimalAmount, False)

	@EqulstnRate.deleter
	def EqulstnRate(self):
		del self._EqulstnRate
		self._EqulstnRate = base_types.UninitialisedField(self, 'EqulstnRate', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def FsclStmp(self):
		return self._FsclStmp

	@FsclStmp.setter
	def FsclStmp(self, value):
		self._FsclStmp = value if value is not None else base_types.UninitialisedField(self, 'FsclStmp', Percentage14Rate, False)

	@FsclStmp.deleter
	def FsclStmp(self):
		del self._FsclStmp
		self._FsclStmp = base_types.UninitialisedField(self, 'FsclStmp', Percentage14Rate, False)

	@property
	def GrssDstrbtnRate(self):
		return self._GrssDstrbtnRate

	@GrssDstrbtnRate.setter
	def GrssDstrbtnRate(self, value):
		self._GrssDstrbtnRate = value if value is not None else base_types.UninitialisedField(self, 'GrssDstrbtnRate', GrossDividendRateFormat37Choice, True)

	@GrssDstrbtnRate.deleter
	def GrssDstrbtnRate(self):
		del self._GrssDstrbtnRate
		self._GrssDstrbtnRate = base_types.UninitialisedField(self, 'GrssDstrbtnRate', GrossDividendRateFormat37Choice, True)

	@property
	def GrssIntrstRateUsdForPmt(self):
		return self._GrssIntrstRateUsdForPmt

	@GrssIntrstRateUsdForPmt.setter
	def GrssIntrstRateUsdForPmt(self, value):
		self._GrssIntrstRateUsdForPmt = value if value is not None else base_types.UninitialisedField(self, 'GrssIntrstRateUsdForPmt', InterestRateUsedForPaymentFormat12Choice, True)

	@GrssIntrstRateUsdForPmt.deleter
	def GrssIntrstRateUsdForPmt(self):
		del self._GrssIntrstRateUsdForPmt
		self._GrssIntrstRateUsdForPmt = base_types.UninitialisedField(self, 'GrssIntrstRateUsdForPmt', InterestRateUsedForPaymentFormat12Choice, True)

	@property
	def NetDstrbtnRate(self):
		return self._NetDstrbtnRate

	@NetDstrbtnRate.setter
	def NetDstrbtnRate(self, value):
		self._NetDstrbtnRate = value if value is not None else base_types.UninitialisedField(self, 'NetDstrbtnRate', NetDividendRateFormat40Choice, True)

	@NetDstrbtnRate.deleter
	def NetDstrbtnRate(self):
		del self._NetDstrbtnRate
		self._NetDstrbtnRate = base_types.UninitialisedField(self, 'NetDstrbtnRate', NetDividendRateFormat40Choice, True)

	@property
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat55Choice, True)

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat55Choice, True)

	@property
	def SlctnFeeRate(self):
		return self._SlctnFeeRate

	@SlctnFeeRate.setter
	def SlctnFeeRate(self, value):
		self._SlctnFeeRate = value if value is not None else base_types.UninitialisedField(self, 'SlctnFeeRate', SolicitationFeeRateFormat12Choice, False)

	@SlctnFeeRate.deleter
	def SlctnFeeRate(self):
		del self._SlctnFeeRate
		self._SlctnFeeRate = base_types.UninitialisedField(self, 'SlctnFeeRate', SolicitationFeeRateFormat12Choice, False)

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat27Choice, False)

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat27Choice, False)

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if value is not None else base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat59Choice, False)

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat59Choice, False)

	@property
	def TaxOnPrfts(self):
		return self._TaxOnPrfts

	@TaxOnPrfts.setter
	def TaxOnPrfts(self, value):
		self._TaxOnPrfts = value if value is not None else base_types.UninitialisedField(self, 'TaxOnPrfts', Percentage14Rate, False)

	@TaxOnPrfts.deleter
	def TaxOnPrfts(self):
		del self._TaxOnPrfts
		self._TaxOnPrfts = base_types.UninitialisedField(self, 'TaxOnPrfts', Percentage14Rate, False)

	@property
	def TaxRclmRate(self):
		return self._TaxRclmRate

	@TaxRclmRate.setter
	def TaxRclmRate(self, value):
		self._TaxRclmRate = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmRate', Percentage14Rate, False)

	@TaxRclmRate.deleter
	def TaxRclmRate(self):
		del self._TaxRclmRate
		self._TaxRclmRate = base_types.UninitialisedField(self, 'TaxRclmRate', Percentage14Rate, False)

	@property
	def ThrdPtyIncntivRate(self):
		return self._ThrdPtyIncntivRate

	@ThrdPtyIncntivRate.setter
	def ThrdPtyIncntivRate(self, value):
		self._ThrdPtyIncntivRate = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyIncntivRate', RateAndAmountFormat59Choice, False)

	@ThrdPtyIncntivRate.deleter
	def ThrdPtyIncntivRate(self):
		del self._ThrdPtyIncntivRate
		self._ThrdPtyIncntivRate = base_types.UninitialisedField(self, 'ThrdPtyIncntivRate', RateAndAmountFormat59Choice, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat55Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat55Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdRate', type=RateAndAmountFormat62Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlySlctnFeeRate', type=SolicitationFeeRateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnRate', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDstrbtnRate', type=GrossDividendRateFormat37Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssIntrstRateUsdForPmt', type=InterestRateUsedForPaymentFormat12Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetDstrbtnRate', type=NetDividendRateFormat40Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnFeeRate', type=SolicitationFeeRateFormat12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnPrfts', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyIncntivRate', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
	))