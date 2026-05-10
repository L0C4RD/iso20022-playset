from . import base_types
from .Max35Text import Max35Text

class SequenceRange1(base_types._BaseFieldType):

	__slots__ = ["_ToSeq", "_FrSeq"]
	@property
	def ToSeq(self):
		return self._ToSeq

	@ToSeq.setter
	def ToSeq(self, value):
		self._ToSeq = value if type(value) != base_types.auto else self.make_default("ToSeq")

	@ToSeq.deleter
	def ToSeq(self):
		del self._ToSeq
		self._ToSeq = None

	@property
	def FrSeq(self):
		return self._FrSeq

	@FrSeq.setter
	def FrSeq(self, value):
		self._FrSeq = value if type(value) != base_types.auto else self.make_default("FrSeq")

	@FrSeq.deleter
	def FrSeq(self):
		del self._FrSeq
		self._FrSeq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ToSeq', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrSeq', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

