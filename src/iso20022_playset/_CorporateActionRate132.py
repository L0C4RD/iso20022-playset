# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage14Rate
from . import RateAndAmountFormat66Choice
from . import RateAndAmountFormat67Choice
from . import RateFormat28Choice
from . import RatioFormat21Choice
from . import RatioFormat22Choice

class CorporateActionRate132(base_types._BaseFieldType):

	__slots__ = ["_AddtlQtyForExstgScties", "_AddtlQtyForSbcbdRsltntScties", "_AplblRate", "_ChrgsFees", "_FinTxTaxRate", "_FsclStmp", "_NewToOd", "_ScndLvlTax", "_TaxCdtRate", "_WhldgTaxRate"]
	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat21Choice, False)

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat21Choice, False)

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat21Choice, False)

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat21Choice, False)

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
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat67Choice, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat67Choice, False)

	@property
	def FinTxTaxRate(self):
		return self._FinTxTaxRate

	@FinTxTaxRate.setter
	def FinTxTaxRate(self, value):
		self._FinTxTaxRate = value if value is not None else base_types.UninitialisedField(self, 'FinTxTaxRate', Percentage14Rate, False)

	@FinTxTaxRate.deleter
	def FinTxTaxRate(self):
		del self._FinTxTaxRate
		self._FinTxTaxRate = base_types.UninitialisedField(self, 'FinTxTaxRate', Percentage14Rate, False)

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
	def NewToOd(self):
		return self._NewToOd

	@NewToOd.setter
	def NewToOd(self, value):
		self._NewToOd = value if value is not None else base_types.UninitialisedField(self, 'NewToOd', RatioFormat22Choice, False)

	@NewToOd.deleter
	def NewToOd(self):
		del self._NewToOd
		self._NewToOd = base_types.UninitialisedField(self, 'NewToOd', RatioFormat22Choice, False)

	@property
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat66Choice, True)

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat66Choice, True)

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat28Choice, False)

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat28Choice, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat66Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat66Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlQtyForExstgScties', type=RatioFormat21Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQtyForSbcbdRsltntScties', type=RatioFormat21Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsFees', type=RateAndAmountFormat67Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinTxTaxRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclStmp', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewToOd', type=RatioFormat22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLvlTax', type=RateAndAmountFormat66Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxCdtRate', type=RateFormat28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhldgTaxRate', type=RateAndAmountFormat66Choice, min=0, max=None, mutex_group=None, array=True),
	))