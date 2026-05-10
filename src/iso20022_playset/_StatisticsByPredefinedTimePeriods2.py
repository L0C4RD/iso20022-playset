from . import base_types
from ._PriceValueChange1 import PriceValueChange1
from ._PriceValue5 import PriceValue5

class StatisticsByPredefinedTimePeriods2(base_types._BaseFieldType):

	__slots__ = ["_OneYrPricChng", "_ThreeYrPricChng", "_HghstPricVal12Mnths", "_LwstPricVal12Mnths", "_FiveYrPricChng"]
	@property
	def OneYrPricChng(self):
		return self._OneYrPricChng

	@OneYrPricChng.setter
	def OneYrPricChng(self, value):
		self._OneYrPricChng = value if type(value) != base_types.auto else self.make_default("OneYrPricChng")

	@OneYrPricChng.deleter
	def OneYrPricChng(self):
		del self._OneYrPricChng
		self._OneYrPricChng = None

	@property
	def ThreeYrPricChng(self):
		return self._ThreeYrPricChng

	@ThreeYrPricChng.setter
	def ThreeYrPricChng(self, value):
		self._ThreeYrPricChng = value if type(value) != base_types.auto else self.make_default("ThreeYrPricChng")

	@ThreeYrPricChng.deleter
	def ThreeYrPricChng(self):
		del self._ThreeYrPricChng
		self._ThreeYrPricChng = None

	@property
	def HghstPricVal12Mnths(self):
		return self._HghstPricVal12Mnths

	@HghstPricVal12Mnths.setter
	def HghstPricVal12Mnths(self, value):
		self._HghstPricVal12Mnths = value if type(value) != base_types.auto else self.make_default("HghstPricVal12Mnths")

	@HghstPricVal12Mnths.deleter
	def HghstPricVal12Mnths(self):
		del self._HghstPricVal12Mnths
		self._HghstPricVal12Mnths = None

	@property
	def LwstPricVal12Mnths(self):
		return self._LwstPricVal12Mnths

	@LwstPricVal12Mnths.setter
	def LwstPricVal12Mnths(self, value):
		self._LwstPricVal12Mnths = value if type(value) != base_types.auto else self.make_default("LwstPricVal12Mnths")

	@LwstPricVal12Mnths.deleter
	def LwstPricVal12Mnths(self):
		del self._LwstPricVal12Mnths
		self._LwstPricVal12Mnths = None

	@property
	def FiveYrPricChng(self):
		return self._FiveYrPricChng

	@FiveYrPricChng.setter
	def FiveYrPricChng(self, value):
		self._FiveYrPricChng = value if type(value) != base_types.auto else self.make_default("FiveYrPricChng")

	@FiveYrPricChng.deleter
	def FiveYrPricChng(self):
		del self._FiveYrPricChng
		self._FiveYrPricChng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OneYrPricChng', type=PriceValueChange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThreeYrPricChng', type=PriceValueChange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghstPricVal12Mnths', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwstPricVal12Mnths', type=PriceValue5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FiveYrPricChng', type=PriceValueChange1, min=0, max=1, mutex_group=None, array=False),
	))

