# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateOrDateTimePeriodChoice
from . import PercentageRate
from . import PriceValue5
from . import PriceValueChange1

class StatisticsByUserDefinedTimePeriod2(base_types._BaseFieldType):

	__slots__ = ["_HghstPricVal", "_LwstPricVal", "_Prd", "_PricChng", "_Yld"]
	@property
	def HghstPricVal(self):
		return self._HghstPricVal

	@HghstPricVal.setter
	def HghstPricVal(self, value):
		self._HghstPricVal = value if value is not None else base_types.UninitialisedField(self, 'HghstPricVal', PriceValue5, False)

	@HghstPricVal.deleter
	def HghstPricVal(self):
		del self._HghstPricVal
		self._HghstPricVal = base_types.UninitialisedField(self, 'HghstPricVal', PriceValue5, False)

	@property
	def LwstPricVal(self):
		return self._LwstPricVal

	@LwstPricVal.setter
	def LwstPricVal(self, value):
		self._LwstPricVal = value if value is not None else base_types.UninitialisedField(self, 'LwstPricVal', PriceValue5, False)

	@LwstPricVal.deleter
	def LwstPricVal(self):
		del self._LwstPricVal
		self._LwstPricVal = base_types.UninitialisedField(self, 'LwstPricVal', PriceValue5, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', DateOrDateTimePeriodChoice, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', DateOrDateTimePeriodChoice, False)

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if value is not None else base_types.UninitialisedField(self, 'PricChng', PriceValueChange1, False)

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = base_types.UninitialisedField(self, 'PricChng', PriceValueChange1, False)

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if value is not None else base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghstPricVal', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwstPricVal', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DateOrDateTimePeriodChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=PriceValueChange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))