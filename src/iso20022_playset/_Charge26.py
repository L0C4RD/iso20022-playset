from . import base_types
from .AmountOrRate3Choice import AmountOrRate3Choice
from .ChargeType4Choice import ChargeType4Choice

class Charge26(base_types._BaseFieldType):

	__slots__ = ["_ChrgApld", "_Tp"]
	@property
	def ChrgApld(self):
		return self._ChrgApld

	@ChrgApld.setter
	def ChrgApld(self, value):
		self._ChrgApld = value if type(value) != base_types.auto else self.make_default("ChrgApld")

	@ChrgApld.deleter
	def ChrgApld(self):
		del self._ChrgApld
		self._ChrgApld = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgApld', type=AmountOrRate3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType4Choice, min=1, max=1, mutex_group=None, array=False),
	))

