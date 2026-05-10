from . import base_types
from .Max35Text import Max35Text
from .DecimalNumber import DecimalNumber
from .MemoryUnit1Code import MemoryUnit1Code

class MemoryCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_FreeSz", "_TtlSz", "_Unit"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def FreeSz(self):
		return self._FreeSz

	@FreeSz.setter
	def FreeSz(self, value):
		self._FreeSz = value if type(value) != base_types.auto else self.make_default("FreeSz")

	@FreeSz.deleter
	def FreeSz(self):
		del self._FreeSz
		self._FreeSz = None

	@property
	def TtlSz(self):
		return self._TtlSz

	@TtlSz.setter
	def TtlSz(self, value):
		self._TtlSz = value if type(value) != base_types.auto else self.make_default("TtlSz")

	@TtlSz.deleter
	def TtlSz(self):
		del self._TtlSz
		self._TtlSz = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeSz', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSz', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=MemoryUnit1Code, min=1, max=1, mutex_group=None, array=False),
	))

