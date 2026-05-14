# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateOrDateTimePeriodChoice import DateOrDateTimePeriodChoice
from ._PercentageRate import PercentageRate
from ._PriceValue5 import PriceValue5
from ._PriceValueChange1 import PriceValueChange1

class StatisticsByUserDefinedTimePeriod2(base_types._BaseFieldType):

	__slots__ = ["_HghstPricVal", "_LwstPricVal", "_Prd", "_PricChng", "_Yld"]
	@property
	def HghstPricVal(self):
		return self._HghstPricVal

	@HghstPricVal.setter
	def HghstPricVal(self, value):
		self._HghstPricVal = value if type(value) != base_types.auto else self.make_default("HghstPricVal")

	@HghstPricVal.deleter
	def HghstPricVal(self):
		del self._HghstPricVal
		self._HghstPricVal = None

	@property
	def LwstPricVal(self):
		return self._LwstPricVal

	@LwstPricVal.setter
	def LwstPricVal(self, value):
		self._LwstPricVal = value if type(value) != base_types.auto else self.make_default("LwstPricVal")

	@LwstPricVal.deleter
	def LwstPricVal(self):
		del self._LwstPricVal
		self._LwstPricVal = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if type(value) != base_types.auto else self.make_default("PricChng")

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = None

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if type(value) != base_types.auto else self.make_default("Yld")

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghstPricVal', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwstPricVal', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DateOrDateTimePeriodChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=PriceValueChange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))