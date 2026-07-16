# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GrossDividendRateFormat41Choice
from . import InterestRateUsedForPaymentFormat18Choice
from . import NetDividendRateFormat43Choice
from . import RateAndAmountFormat48Choice
from . import RateAndAmountFormat72Choice
from . import RateAndAmountFormat76Choice
from . import RateAndAmountFormat77Choice
from . import RateFormat24Choice
from . import RateFormat30Choice
from . import SolicitationFeeRateFormat15Choice

class Rate47(base_types._BaseFieldType):

	__slots__ = ["_AddtlTax", "_AplblRate", "_ChrgsFees", "_DmdRate", "_EarlySlctnFeeRate", "_EqulstnRate", "_FsclStmp", "_GrssDstrbtnRate", "_GrssIntrstRateUsdForPmt", "_NetDstrbtnRate", "_ScndLvlTax", "_SlctnFeeRate", "_TaxCdtRate", "_TaxOnIncm", "_TaxOnPrfts", "_TaxRclmRate", "_ThrdPtyIncntivRate", "_WhldgTaxRate"]
	@property
	def AddtlTax(self):
		return self._AddtlTax

	@AddtlTax.setter
	def AddtlTax(self, value):
		self._AddtlTax = value if value is not None else base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat72Choice, False)

	@AddtlTax.deleter
	def AddtlTax(self):
		del self._AddtlTax
		self._AddtlTax = base_types.UninitialisedField(self, 'AddtlTax', RateAndAmountFormat72Choice, False)

	@property
	def AplblRate(self):
		return self._AplblRate

	@AplblRate.setter
	def AplblRate(self, value):
		self._AplblRate = value if value is not None else base_types.UninitialisedField(self, 'AplblRate', RateFormat24Choice, False)

	@AplblRate.deleter
	def AplblRate(self):
		del self._AplblRate
		self._AplblRate = base_types.UninitialisedField(self, 'AplblRate', RateFormat24Choice, False)

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat72Choice, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat72Choice, False)

	@property
	def DmdRate(self):
		return self._DmdRate

	@DmdRate.setter
	def DmdRate(self, value):
		self._DmdRate = value if value is not None else base_types.UninitialisedField(self, 'DmdRate', RateAndAmountFormat77Choice, True)

	@DmdRate.deleter
	def DmdRate(self):
		del self._DmdRate
		self._DmdRate = base_types.UninitialisedField(self, 'DmdRate', RateAndAmountFormat77Choice, True)

	@property
	def EarlySlctnFeeRate(self):
		return self._EarlySlctnFeeRate

	@EarlySlctnFeeRate.setter
	def EarlySlctnFeeRate(self, value):
		self._EarlySlctnFeeRate = value if value is not None else base_types.UninitialisedField(self, 'EarlySlctnFeeRate', SolicitationFeeRateFormat15Choice, False)

	@EarlySlctnFeeRate.deleter
	def EarlySlctnFeeRate(self):
		del self._EarlySlctnFeeRate
		self._EarlySlctnFeeRate = base_types.UninitialisedField(self, 'EarlySlctnFeeRate', SolicitationFeeRateFormat15Choice, False)

	@property
	def EqulstnRate(self):
		return self._EqulstnRate

	@EqulstnRate.setter
	def EqulstnRate(self, value):
		self._EqulstnRate = value if value is not None else base_types.UninitialisedField(self, 'EqulstnRate', RateAndAmountFormat48Choice, False)

	@EqulstnRate.deleter
	def EqulstnRate(self):
		del self._EqulstnRate
		self._EqulstnRate = base_types.UninitialisedField(self, 'EqulstnRate', RateAndAmountFormat48Choice, False)

	@property
	def FsclStmp(self):
		return self._FsclStmp

	@FsclStmp.setter
	def FsclStmp(self, value):
		self._FsclStmp = value if value is not None else base_types.UninitialisedField(self, 'FsclStmp', RateFormat24Choice, False)

	@FsclStmp.deleter
	def FsclStmp(self):
		del self._FsclStmp
		self._FsclStmp = base_types.UninitialisedField(self, 'FsclStmp', RateFormat24Choice, False)

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
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat76Choice, True)

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat76Choice, True)

	@property
	def SlctnFeeRate(self):
		return self._SlctnFeeRate

	@SlctnFeeRate.setter
	def SlctnFeeRate(self, value):
		self._SlctnFeeRate = value if value is not None else base_types.UninitialisedField(self, 'SlctnFeeRate', SolicitationFeeRateFormat15Choice, False)

	@SlctnFeeRate.deleter
	def SlctnFeeRate(self):
		del self._SlctnFeeRate
		self._SlctnFeeRate = base_types.UninitialisedField(self, 'SlctnFeeRate', SolicitationFeeRateFormat15Choice, False)

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat30Choice, False)

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat30Choice, False)

	@property
	def TaxOnIncm(self):
		return self._TaxOnIncm

	@TaxOnIncm.setter
	def TaxOnIncm(self, value):
		self._TaxOnIncm = value if value is not None else base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat72Choice, False)

	@TaxOnIncm.deleter
	def TaxOnIncm(self):
		del self._TaxOnIncm
		self._TaxOnIncm = base_types.UninitialisedField(self, 'TaxOnIncm', RateAndAmountFormat72Choice, False)

	@property
	def TaxOnPrfts(self):
		return self._TaxOnPrfts

	@TaxOnPrfts.setter
	def TaxOnPrfts(self, value):
		self._TaxOnPrfts = value if value is not None else base_types.UninitialisedField(self, 'TaxOnPrfts', RateFormat24Choice, False)

	@TaxOnPrfts.deleter
	def TaxOnPrfts(self):
		del self._TaxOnPrfts
		self._TaxOnPrfts = base_types.UninitialisedField(self, 'TaxOnPrfts', RateFormat24Choice, False)

	@property
	def TaxRclmRate(self):
		return self._TaxRclmRate

	@TaxRclmRate.setter
	def TaxRclmRate(self, value):
		self._TaxRclmRate = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmRate', RateFormat24Choice, False)

	@TaxRclmRate.deleter
	def TaxRclmRate(self):
		del self._TaxRclmRate
		self._TaxRclmRate = base_types.UninitialisedField(self, 'TaxRclmRate', RateFormat24Choice, False)

	@property
	def ThrdPtyIncntivRate(self):
		return self._ThrdPtyIncntivRate

	@ThrdPtyIncntivRate.setter
	def ThrdPtyIncntivRate(self, value):
		self._ThrdPtyIncntivRate = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyIncntivRate', RateFormat30Choice, False)

	@ThrdPtyIncntivRate.deleter
	def ThrdPtyIncntivRate(self):
		del self._ThrdPtyIncntivRate
		self._ThrdPtyIncntivRate = base_types.UninitialisedField(self, 'ThrdPtyIncntivRate', RateFormat30Choice, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat76Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat76Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat72Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat72Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdRate', type=RateAndAmountFormat77Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlySlctnFeeRate', type=SolicitationFeeRateFormat15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnRate', type=RateAndAmountFormat48Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDstrbtnRate', type=GrossDividendRateFormat41Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssIntrstRateUsdForPmt', type=InterestRateUsedForPaymentFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetDstrbtnRate', type=NetDividendRateFormat43Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat76Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnFeeRate', type=SolicitationFeeRateFormat15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateAndAmountFormat72Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnPrfts', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyIncntivRate', type=RateFormat30Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat76Choice, min=0, max=None, mutex_group=None, array=True),
	))