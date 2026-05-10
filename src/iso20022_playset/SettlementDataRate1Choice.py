from . import base_types
from .PercentageRate import PercentageRate

class SettlementDataRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_ValOfInstrs", "_NbOfInstrs"]
	@property
	def ValOfInstrs(self):
		return self._ValOfInstrs

	@ValOfInstrs.setter
	def ValOfInstrs(self, value):
		self._ValOfInstrs = value if type(value) != base_types.auto else self.make_default("ValOfInstrs")

	@ValOfInstrs.deleter
	def ValOfInstrs(self):
		del self._ValOfInstrs
		self._ValOfInstrs = None

	@property
	def NbOfInstrs(self):
		return self._NbOfInstrs

	@NbOfInstrs.setter
	def NbOfInstrs(self, value):
		self._NbOfInstrs = value if type(value) != base_types.auto else self.make_default("NbOfInstrs")

	@NbOfInstrs.deleter
	def NbOfInstrs(self):
		del self._NbOfInstrs
		self._NbOfInstrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValOfInstrs', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NbOfInstrs', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

