import base_types
import Max3NumericText
import YesNoIndicator

class CrystallisationDay1(base_types._BaseFieldType):

	__slots__ = ["_Day", "_Prd"]
	@property
	def Day(self):
		return self._Day

	@Day.setter
	def Day(self, value):
		self._Day = value if type(value) != auto else self.make_default("Day")

	@Day.deleter
	def Day(self):
		del self._Day
		self._Day = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Day', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
	))

