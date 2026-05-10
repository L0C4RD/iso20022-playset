from . import base_types
from ._RestrictedFINDecimalNumber import RestrictedFINDecimalNumber

class QuantityToQuantityRatio2(base_types._BaseFieldType):

	__slots__ = ["_Qty2", "_Qty1"]
	@property
	def Qty2(self):
		return self._Qty2

	@Qty2.setter
	def Qty2(self, value):
		self._Qty2 = value if type(value) != base_types.auto else self.make_default("Qty2")

	@Qty2.deleter
	def Qty2(self):
		del self._Qty2
		self._Qty2 = None

	@property
	def Qty1(self):
		return self._Qty1

	@Qty1.setter
	def Qty1(self, value):
		self._Qty1 = value if type(value) != base_types.auto else self.make_default("Qty1")

	@Qty1.deleter
	def Qty1(self):
		del self._Qty1
		self._Qty1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty2', type=RestrictedFINDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty1', type=RestrictedFINDecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

