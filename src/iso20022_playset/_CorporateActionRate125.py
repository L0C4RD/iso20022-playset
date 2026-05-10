from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._RateAndAmountFormat55Choice import RateAndAmountFormat55Choice
from ._RateAndAmountFormat59Choice import RateAndAmountFormat59Choice
from ._RatioFormat20Choice import RatioFormat20Choice
from ._RatioFormat19Choice import RatioFormat19Choice
from ._RateFormat27Choice import RateFormat27Choice

class CorporateActionRate125(base_types._BaseFieldType):

	__slots__ = ["_TaxCdtRate", "_FinTxTaxRate", "_NewToOd", "_AddtlQtyForSbcbdRsltntScties", "_ChrgsFees", "_WhldgTaxRate", "_AplblRate", "_FsclStmp", "_ScndLvlTax", "_AddtlQtyForExstgScties"]
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
	def FinTxTaxRate(self):
		return self._FinTxTaxRate

	@FinTxTaxRate.setter
	def FinTxTaxRate(self, value):
		self._FinTxTaxRate = value if type(value) != base_types.auto else self.make_default("FinTxTaxRate")

	@FinTxTaxRate.deleter
	def FinTxTaxRate(self):
		del self._FinTxTaxRate
		self._FinTxTaxRate = None

	@property
	def NewToOd(self):
		return self._NewToOd

	@NewToOd.setter
	def NewToOd(self, value):
		self._NewToOd = value if type(value) != base_types.auto else self.make_default("NewToOd")

	@NewToOd.deleter
	def NewToOd(self):
		del self._NewToOd
		self._NewToOd = None

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if type(value) != base_types.auto else self.make_default("AddtlQtyForSbcbdRsltntScties")

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = None

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
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if type(value) != base_types.auto else self.make_default("AddtlQtyForExstgScties")

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinTxTaxRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewToOd', type=RatioFormat19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=RatioFormat20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AplblRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=RatioFormat20Choice, min=0, max=1, mutex_group=None, array=False),
	))

