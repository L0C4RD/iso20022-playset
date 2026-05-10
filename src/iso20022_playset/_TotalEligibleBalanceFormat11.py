from . import base_types
from .Quantity80Choice import Quantity80Choice
from .SignedQuantityFormat13 import SignedQuantityFormat13

class TotalEligibleBalanceFormat11(base_types._BaseFieldType):

	__slots__ = ["_PartWayPrdUnits", "_FullPrdUnits", "_Bal"]
	@property
	def PartWayPrdUnits(self):
		return self._PartWayPrdUnits

	@PartWayPrdUnits.setter
	def PartWayPrdUnits(self, value):
		self._PartWayPrdUnits = value if type(value) != base_types.auto else self.make_default("PartWayPrdUnits")

	@PartWayPrdUnits.deleter
	def PartWayPrdUnits(self):
		del self._PartWayPrdUnits
		self._PartWayPrdUnits = None

	@property
	def FullPrdUnits(self):
		return self._FullPrdUnits

	@FullPrdUnits.setter
	def FullPrdUnits(self, value):
		self._FullPrdUnits = value if type(value) != base_types.auto else self.make_default("FullPrdUnits")

	@FullPrdUnits.deleter
	def FullPrdUnits(self):
		del self._FullPrdUnits
		self._FullPrdUnits = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=Quantity80Choice, min=0, max=1, mutex_group=None, array=False),
	))

