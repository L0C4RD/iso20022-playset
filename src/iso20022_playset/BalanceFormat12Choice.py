from . import base_types
from .SignedQuantityFormat11 import SignedQuantityFormat11
from .SignedQuantityFormat10 import SignedQuantityFormat10

class BalanceFormat12Choice(base_types._BaseFieldType):

	__slots__ = ["_PartWayPrdUnits", "_FullPrdUnits", "_Bal", "_NotElgblBal", "_ElgblBal"]
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

	@property
	def NotElgblBal(self):
		return self._NotElgblBal

	@NotElgblBal.setter
	def NotElgblBal(self, value):
		self._NotElgblBal = value if type(value) != base_types.auto else self.make_default("NotElgblBal")

	@NotElgblBal.deleter
	def NotElgblBal(self):
		del self._NotElgblBal
		self._NotElgblBal = None

	@property
	def ElgblBal(self):
		return self._ElgblBal

	@ElgblBal.setter
	def ElgblBal(self, value):
		self._ElgblBal = value if type(value) != base_types.auto else self.make_default("ElgblBal")

	@ElgblBal.deleter
	def ElgblBal(self):
		del self._ElgblBal
		self._ElgblBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElgblBal', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
	))

