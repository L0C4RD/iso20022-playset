from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._RateAndAmountFormat56Choice import RateAndAmountFormat56Choice
from ._RateAndAmountFormat57Choice import RateAndAmountFormat57Choice
from ._RateFormat24Choice import RateFormat24Choice
from ._RateFormat26Choice import RateFormat26Choice
from ._RatioFormat17Choice import RatioFormat17Choice
from ._RatioFormat18Choice import RatioFormat18Choice

class CorporateActionRate123(base_types._BaseFieldType):

	__slots__ = ["_AddtlQtyForExstgScties", "_AddtlQtyForSbcbdRsltntScties", "_AplblRate", "_ChrgsFees", "_FinTxTaxRate", "_FsclStmp", "_NewToOd", "_ScndLvlTax", "_TaxCdtRate", "_TrfrmatnRate", "_WhldgTaxRate"]
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
	def TrfrmatnRate(self):
		return self._TrfrmatnRate

	@TrfrmatnRate.setter
	def TrfrmatnRate(self, value):
		self._TrfrmatnRate = value if type(value) != base_types.auto else self.make_default("TrfrmatnRate")

	@TrfrmatnRate.deleter
	def TrfrmatnRate(self):
		del self._TrfrmatnRate
		self._TrfrmatnRate = None

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
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=RatioFormat17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=RatioFormat17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat57Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinTxTaxRate', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=RateFormat24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewToOd', type=RatioFormat18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat56Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrmatnRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat56Choice, min=0, max=None, mutex_group=None, array=True),
	))

