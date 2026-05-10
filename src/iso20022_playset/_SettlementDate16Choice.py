from . import base_types
from ._SettlementDateCode12Choice import SettlementDateCode12Choice
from ._DateAndDateTime1Choice import DateAndDateTime1Choice

class SettlementDate16Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Cd"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=SettlementDateCode12Choice, min=0, max=1, mutex_group=1, array=False),
	))

