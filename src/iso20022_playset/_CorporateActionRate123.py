# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage14Rate
from . import RateAndAmountFormat56Choice
from . import RateAndAmountFormat57Choice
from . import RateFormat24Choice
from . import RateFormat26Choice
from . import RatioFormat17Choice
from . import RatioFormat18Choice

class CorporateActionRate123(base_types._BaseFieldType):

	__slots__ = ["_AddtlQtyForExstgScties", "_AddtlQtyForSbcbdRsltntScties", "_AplblRate", "_ChrgsFees", "_FinTxTaxRate", "_FsclStmp", "_NewToOd", "_ScndLvlTax", "_TaxCdtRate", "_TrfrmatnRate", "_WhldgTaxRate"]
	@property
	def AddtlQtyForExstgScties(self):
		return self._AddtlQtyForExstgScties

	@AddtlQtyForExstgScties.setter
	def AddtlQtyForExstgScties(self, value):
		self._AddtlQtyForExstgScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat17Choice, False)

	@AddtlQtyForExstgScties.deleter
	def AddtlQtyForExstgScties(self):
		del self._AddtlQtyForExstgScties
		self._AddtlQtyForExstgScties = base_types.UninitialisedField(self, 'AddtlQtyForExstgScties', RatioFormat17Choice, False)

	@property
	def AddtlQtyForSbcbdRsltntScties(self):
		return self._AddtlQtyForSbcbdRsltntScties

	@AddtlQtyForSbcbdRsltntScties.setter
	def AddtlQtyForSbcbdRsltntScties(self, value):
		self._AddtlQtyForSbcbdRsltntScties = value if value is not None else base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat17Choice, False)

	@AddtlQtyForSbcbdRsltntScties.deleter
	def AddtlQtyForSbcbdRsltntScties(self):
		del self._AddtlQtyForSbcbdRsltntScties
		self._AddtlQtyForSbcbdRsltntScties = base_types.UninitialisedField(self, 'AddtlQtyForSbcbdRsltntScties', RatioFormat17Choice, False)

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
		self._ChrgsFees = value if value is not None else base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat57Choice, False)

	@ChrgsFees.deleter
	def ChrgsFees(self):
		del self._ChrgsFees
		self._ChrgsFees = base_types.UninitialisedField(self, 'ChrgsFees', RateAndAmountFormat57Choice, False)

	@property
	def FinTxTaxRate(self):
		return self._FinTxTaxRate

	@FinTxTaxRate.setter
	def FinTxTaxRate(self, value):
		self._FinTxTaxRate = value if value is not None else base_types.UninitialisedField(self, 'FinTxTaxRate', RateFormat24Choice, False)

	@FinTxTaxRate.deleter
	def FinTxTaxRate(self):
		del self._FinTxTaxRate
		self._FinTxTaxRate = base_types.UninitialisedField(self, 'FinTxTaxRate', RateFormat24Choice, False)

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
	def NewToOd(self):
		return self._NewToOd

	@NewToOd.setter
	def NewToOd(self, value):
		self._NewToOd = value if value is not None else base_types.UninitialisedField(self, 'NewToOd', RatioFormat18Choice, False)

	@NewToOd.deleter
	def NewToOd(self):
		del self._NewToOd
		self._NewToOd = base_types.UninitialisedField(self, 'NewToOd', RatioFormat18Choice, False)

	@property
	def ScndLvlTax(self):
		return self._ScndLvlTax

	@ScndLvlTax.setter
	def ScndLvlTax(self, value):
		self._ScndLvlTax = value if value is not None else base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat56Choice, True)

	@ScndLvlTax.deleter
	def ScndLvlTax(self):
		del self._ScndLvlTax
		self._ScndLvlTax = base_types.UninitialisedField(self, 'ScndLvlTax', RateAndAmountFormat56Choice, True)

	@property
	def TaxCdtRate(self):
		return self._TaxCdtRate

	@TaxCdtRate.setter
	def TaxCdtRate(self, value):
		self._TaxCdtRate = value if value is not None else base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat26Choice, False)

	@TaxCdtRate.deleter
	def TaxCdtRate(self):
		del self._TaxCdtRate
		self._TaxCdtRate = base_types.UninitialisedField(self, 'TaxCdtRate', RateFormat26Choice, False)

	@property
	def TrfrmatnRate(self):
		return self._TrfrmatnRate

	@TrfrmatnRate.setter
	def TrfrmatnRate(self, value):
		self._TrfrmatnRate = value if value is not None else base_types.UninitialisedField(self, 'TrfrmatnRate', Percentage14Rate, False)

	@TrfrmatnRate.deleter
	def TrfrmatnRate(self):
		del self._TrfrmatnRate
		self._TrfrmatnRate = base_types.UninitialisedField(self, 'TrfrmatnRate', Percentage14Rate, False)

	@property
	def WhldgTaxRate(self):
		return self._WhldgTaxRate

	@WhldgTaxRate.setter
	def WhldgTaxRate(self, value):
		self._WhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat56Choice, True)

	@WhldgTaxRate.deleter
	def WhldgTaxRate(self):
		del self._WhldgTaxRate
		self._WhldgTaxRate = base_types.UninitialisedField(self, 'WhldgTaxRate', RateAndAmountFormat56Choice, True)

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