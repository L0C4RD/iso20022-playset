from . import base_types
from ._ClosureReason2Choice import ClosureReason2Choice
from ._DateTimePeriod1Choice import DateTimePeriod1Choice

class SystemClosure2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Prd"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

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
		base_types.FieldEntry(name='Rsn', type=ClosureReason2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))

