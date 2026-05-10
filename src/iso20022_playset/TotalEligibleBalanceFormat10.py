import base_types
import SignedQuantityFormat10
import Quantity49Choice

class TotalEligibleBalanceFormat10(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_FullPrdUnits", "_PartWayPrdUnits"]
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
	def PartWayPrdUnits(self):
		return self._PartWayPrdUnits

	@PartWayPrdUnits.setter
	def PartWayPrdUnits(self, value):
		self._PartWayPrdUnits = value if type(value) != auto else self.make_default("PartWayPrdUnits")

	@PartWayPrdUnits.deleter
	def PartWayPrdUnits(self):
		del self._PartWayPrdUnits
		self._PartWayPrdUnits = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=Quantity49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PartWayPrdUnits', type=SignedQuantityFormat10, min=0, max=1, mutex_group=None, array=False),
	))

