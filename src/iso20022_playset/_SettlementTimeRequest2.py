from . import base_types
from ._ISOTime import ISOTime

class SettlementTimeRequest2(base_types._BaseFieldType):

	__slots__ = ["_CLSTm", "_FrTm", "_RjctTm", "_TillTm"]
	@property
	def CLSTm(self):
		return self._CLSTm

	@CLSTm.setter
	def CLSTm(self, value):
		self._CLSTm = value if type(value) != base_types.auto else self.make_default("CLSTm")

	@CLSTm.deleter
	def CLSTm(self):
		del self._CLSTm
		self._CLSTm = None

	@property
	def FrTm(self):
		return self._FrTm

	@FrTm.setter
	def FrTm(self, value):
		self._FrTm = value if type(value) != base_types.auto else self.make_default("FrTm")

	@FrTm.deleter
	def FrTm(self):
		del self._FrTm
		self._FrTm = None

	@property
	def RjctTm(self):
		return self._RjctTm

	@RjctTm.setter
	def RjctTm(self, value):
		self._RjctTm = value if type(value) != base_types.auto else self.make_default("RjctTm")

	@RjctTm.deleter
	def RjctTm(self):
		del self._RjctTm
		self._RjctTm = None

	@property
	def TillTm(self):
		return self._TillTm

	@TillTm.setter
	def TillTm(self, value):
		self._TillTm = value if type(value) != base_types.auto else self.make_default("TillTm")

	@TillTm.deleter
	def TillTm(self):
		del self._TillTm
		self._TillTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CLSTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TillTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))

