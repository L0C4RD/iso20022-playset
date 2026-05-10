from . import base_types
from ._SolicitationFeeRateFormat14Choice import SolicitationFeeRateFormat14Choice
from ._RateFormat29Choice import RateFormat29Choice
from ._RateAndAmountFormat69Choice import RateAndAmountFormat69Choice
from ._InterestRateUsedForPaymentFormat18Choice import InterestRateUsedForPaymentFormat18Choice
from ._RateAndAmountFormat48Choice import RateAndAmountFormat48Choice
from ._RateFormat24Choice import RateFormat24Choice
from ._RateAndAmountFormat70Choice import RateAndAmountFormat70Choice
from ._RateAndAmountFormat71Choice import RateAndAmountFormat71Choice
from ._GrossDividendRateFormat41Choice import GrossDividendRateFormat41Choice
from ._NetDividendRateFormat43Choice import NetDividendRateFormat43Choice

class Rate46(base_types._BaseFieldType):

	__slots__ = ["_GrssIntrstRateUsdForPmt", "_FsclStmp", "_NetDstrbtnRate", "_SlctnFeeRate", "_EarlySlctnFeeRate", "_TaxOnPrfts", "_ThrdPtyIncntivRate", "_ScndLvlTax", "_WhldgTaxRate", "_AplblRate", "_TaxOnIncm", "_TaxRclmRate", "_ChrgsFees", "_GrssDstrbtnRate", "_EqulstnRate", "_AddtlTax", "_DmdRate", "_TaxCdtRate"]
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
	def AplblRate(self):
		return self._AplblRate

	@AplblRate.setter
	def AplblRate(self, value):
		self._AplblRate = value if type(value) != base_types.auto else self.make_default("AplblRate")

	@AplblRate.deleter
	def AplblRate(self):
		del self._AplblRate
		self._AplblRate = None

	@property
	def ChrgsFees(self):
		return self._ChrgsFees

	@ChrgsFees.setter
	def ChrgsFees(self, value):
		self._ChrgsFees = value if type(value) != base_types.auto else self.make_default("ChrgsFees")

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = None

	@property
	def DmdRate(self):
		return self._DmdRate

	@DmdRate.setter
	def DmdRate(self, value):
		self._DmdRate = value if type(value) != base_types.auto else self.make_default("DmdRate")

	@DmdRate.deleter
	def DmdRate(self):
		del self._DmdRate
		self._DmdRate = None

	@property
	def EarlySlctnFeeRate(self):
		return self._EarlySlctnFeeRate

	@EarlySlctnFeeRate.setter
	def EarlySlctnFeeRate(self, value):
		self._EarlySlctnFeeRate = value if type(value) != base_types.auto else self.make_default("EarlySlctnFeeRate")

	@EarlySlctnFeeRate.deleter
	def EarlySlctnFeeRate(self):
		del self._EarlySlctnFeeRate
		self._EarlySlctnFeeRate = None

	@property
	def EqulstnRate(self):
		return self._EqulstnRate

	@EqulstnRate.setter
	def EqulstnRate(self, value):
		self._EqulstnRate = value if type(value) != base_types.auto else self.make_default("EqulstnRate")

	@EqulstnRate.deleter
	def EqulstnRate(self):
		del self._EqulstnRate
		self._EqulstnRate = None

	@property
	def FsclStmp(self):
		return self._FsclStmp

	@FsclStmp.setter
	def FsclStmp(self, value):
		self._FsclStmp = value if type(value) != base_types.auto else self.make_default("FsclStmp")

	@FsclStmp.deleter
	def FsclStmp(self):
		del self._FsclStmp
		self._FsclStmp = None

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
	def GrssIntrstRateUsdForPmt(self):
		return self._GrssIntrstRateUsdForPmt

	@GrssIntrstRateUsdForPmt.setter
	def GrssIntrstRateUsdForPmt(self, value):
		self._GrssIntrstRateUsdForPmt = value if type(value) != base_types.auto else self.make_default("GrssIntrstRateUsdForPmt")

	@GrssIntrstRateUsdForPmt.deleter
	def GrssIntrstRateUsdForPmt(self):
		del self._GrssIntrstRateUsdForPmt
		self._GrssIntrstRateUsdForPmt = None

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
	def SlctnFeeRate(self):
		return self._SlctnFeeRate

	@SlctnFeeRate.setter
	def SlctnFeeRate(self, value):
		self._SlctnFeeRate = value if type(value) != base_types.auto else self.make_default("SlctnFeeRate")

	@SlctnFeeRate.deleter
	def SlctnFeeRate(self):
		del self._SlctnFeeRate
		self._SlctnFeeRate = None

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if type(value) != base_types.auto else self.make_default("TaxCdtRate")

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = None

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
	def TaxOnPrfts(self):
		return self._TaxOnPrfts

	@TaxOnPrfts.setter
	def TaxOnPrfts(self, value):
		self._TaxOnPrfts = value if type(value) != base_types.auto else self.make_default("TaxOnPrfts")

	@TaxOnPrfts.deleter
	def TaxOnPrfts(self):
		del self._TaxOnPrfts
		self._TaxOnPrfts = None

	@property
	def TaxRclmRate(self):
		return self._TaxRclmRate

	@TaxRclmRate.setter
	def TaxRclmRate(self, value):
		self._TaxRclmRate = value if type(value) != base_types.auto else self.make_default("TaxRclmRate")

	@TaxRclmRate.deleter
	def TaxRclmRate(self):
		del self._TaxRclmRate
		self._TaxRclmRate = None

	@property
	def ThrdPtyIncntivRate(self):
		return self._ThrdPtyIncntivRate

	@ThrdPtyIncntivRate.setter
	def ThrdPtyIncntivRate(self, value):
		self._ThrdPtyIncntivRate = value if type(value) != base_types.auto else self.make_default("ThrdPtyIncntivRate")

	@ThrdPtyIncntivRate.deleter
	def ThrdPtyIncntivRate(self):
		del self._ThrdPtyIncntivRate
		self._ThrdPtyIncntivRate = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTax', type=RateAndAmountFormat69Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat69Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmdRate', type=RateAndAmountFormat71Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EarlySlctnFeeRate', type=SolicitationFeeRateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnRate', type=RateAndAmountFormat48Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDstrbtnRate', type=GrossDividendRateFormat41Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssIntrstRateUsdForPmt', type=InterestRateUsedForPaymentFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetDstrbtnRate', type=NetDividendRateFormat43Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat70Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnFeeRate', type=SolicitationFeeRateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnIncm', type=RateAndAmountFormat69Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnPrfts', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyIncntivRate', type=RateFormat29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat70Choice, min=0, max=None, mutex_group=None, array=True),
	))

