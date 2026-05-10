import base_types
import PercentageRate
import YesNoIndicator

class PercentageRangeBoundary1(base_types._BaseFieldType):

	__slots__ = ["_BdryRate", "_Incl"]
	@property
	def BdryRate(self):
		return self._BdryRate

	@BdryRate.setter
	def BdryRate(self, value):
		self._BdryRate = value if type(value) != auto else self.make_default("BdryRate")

	@BdryRate.deleter
	def BdryRate(self):
		del self._BdryRate
		self._BdryRate = None

	@property
	def Incl(self):
		return self._Incl

	@Incl.setter
	def Incl(self, value):
		self._Incl = value if type(value) != auto else self.make_default("Incl")

	@Incl.deleter
	def Incl(self):
		del self._Incl
		self._Incl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BdryRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

