from . import base_types
import SignedQuantityFormat13
import SignedQuantityFormat12

class BalanceFormat16Choice(base_types._BaseFieldType):

	__slots__ = ["_ElgblBal", "_NotElgblBal", "_PartWayPrdUnits", "_FullPrdUnits", "_Bal"]
	@property
	def ElgblBal(self):
		return self._ElgblBal

	@ElgblBal.setter
	def ElgblBal(self, value):
		self._ElgblBal = value if type(value) != auto else self.make_default("ElgblBal")

	@ElgblBal.deleter
	def ElgblBal(self):
		del self._ElgblBal
		self._ElgblBal = None

	@property
	def NotElgblBal(self):
		return self._NotElgblBal

	@NotElgblBal.setter
	def NotElgblBal(self, value):
		self._NotElgblBal = value if type(value) != auto else self.make_default("NotElgblBal")

	@NotElgblBal.deleter
	def NotElgblBal(self):
		del self._NotElgblBal
		self._NotElgblBal = None

	@property
	def PartWayPrdUnits(self):
		return self._PartWayPrdUnits

	@PartWayPrdUnits.setter
	def PartWayPrdUnits(self, value):
		self._PartWayPrdUnits = value if type(value) != auto else self.make_default("PartWayPrdUnits")

	@PartWayPrdUnits.deleter
	def PartWayPrdUnits(self):
		del self._PartWayPrdUnits
		self._PartWayPrdUnits = None

	@property
	def FullPrdUnits(self):
		return self._FullPrdUnits

	@FullPrdUnits.setter
	def FullPrdUnits(self, value):
		self._FullPrdUnits = value if type(value) != auto else self.make_default("FullPrdUnits")

	@FullPrdUnits.deleter
	def FullPrdUnits(self):
		del self._FullPrdUnits
		self._FullPrdUnits = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotElgblBal', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat12, min=0, max=1, mutex_group=1, array=False),
	))

