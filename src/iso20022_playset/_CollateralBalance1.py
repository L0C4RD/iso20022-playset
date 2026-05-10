from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class CollateralBalance1(base_types._BaseFieldType):

	__slots__ = ["_HeldByPtyB", "_HeldByPtyA"]
	@property
	def HeldByPtyB(self):
		return self._HeldByPtyB

	@HeldByPtyB.setter
	def HeldByPtyB(self, value):
		self._HeldByPtyB = value if type(value) != base_types.auto else self.make_default("HeldByPtyB")

	@HeldByPtyB.deleter
	def HeldByPtyB(self):
		del self._HeldByPtyB
		self._HeldByPtyB = None

	@property
	def HeldByPtyA(self):
		return self._HeldByPtyA

	@HeldByPtyA.setter
	def HeldByPtyA(self, value):
		self._HeldByPtyA = value if type(value) != base_types.auto else self.make_default("HeldByPtyA")

	@HeldByPtyA.deleter
	def HeldByPtyA(self):
		del self._HeldByPtyA
		self._HeldByPtyA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HeldByPtyB', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HeldByPtyA', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

