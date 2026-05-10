from . import base_types
from .DatePeriod5 import DatePeriod5

class AdjustmentRequest1(base_types._BaseFieldType):

	__slots__ = ["_Prd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=DatePeriod5, min=0, max=1, mutex_group=None, array=False),
	))

