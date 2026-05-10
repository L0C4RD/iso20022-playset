from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._RateAndAmountFormat64Choice import RateAndAmountFormat64Choice
from ._RateAndAmountFormat65Choice import RateAndAmountFormat65Choice

class CorporateActionRate130(base_types._BaseFieldType):

	__slots__ = ["_OvrsbcptRate", "_ReqdScndLvlTaxRate", "_PropsdRate", "_ReqdWhldgTaxRate"]
	@property
	def OvrsbcptRate(self):
		return self._OvrsbcptRate

	@OvrsbcptRate.setter
	def OvrsbcptRate(self, value):
		self._OvrsbcptRate = value if type(value) != base_types.auto else self.make_default("OvrsbcptRate")

	@OvrsbcptRate.deleter
	def OvrsbcptRate(self):
		del self._OvrsbcptRate
		self._OvrsbcptRate = None

	@property
	def PropsdRate(self):
		return self._PropsdRate

	@PropsdRate.setter
	def PropsdRate(self, value):
		self._PropsdRate = value if type(value) != base_types.auto else self.make_default("PropsdRate")

	@PropsdRate.deleter
	def PropsdRate(self):
		del self._PropsdRate
		self._PropsdRate = None

	@property
	def ReqdScndLvlTaxRate(self):
		return self._ReqdScndLvlTaxRate

	@ReqdScndLvlTaxRate.setter
	def ReqdScndLvlTaxRate(self, value):
		self._ReqdScndLvlTaxRate = value if type(value) != base_types.auto else self.make_default("ReqdScndLvlTaxRate")

	@ReqdScndLvlTaxRate.deleter
	def ReqdScndLvlTaxRate(self):
		del self._ReqdScndLvlTaxRate
		self._ReqdScndLvlTaxRate = None

	@property
	def ReqdWhldgTaxRate(self):
		return self._ReqdWhldgTaxRate

	@ReqdWhldgTaxRate.setter
	def ReqdWhldgTaxRate(self, value):
		self._ReqdWhldgTaxRate = value if type(value) != base_types.auto else self.make_default("ReqdWhldgTaxRate")

	@ReqdWhldgTaxRate.deleter
	def ReqdWhldgTaxRate(self):
		del self._ReqdWhldgTaxRate
		self._ReqdWhldgTaxRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OvrsbcptRate', type=RateAndAmountFormat64Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdScndLvlTaxRate', type=RateAndAmountFormat65Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdWhldgTaxRate', type=RateAndAmountFormat65Choice, min=0, max=None, mutex_group=None, array=True),
	))

