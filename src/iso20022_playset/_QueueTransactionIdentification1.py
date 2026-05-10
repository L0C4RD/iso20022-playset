from . import base_types
from ._Max16Text import Max16Text

class QueueTransactionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_PosInQ", "_QId"]
	@property
	def PosInQ(self):
		return self._PosInQ

	@PosInQ.setter
	def PosInQ(self, value):
		self._PosInQ = value if type(value) != base_types.auto else self.make_default("PosInQ")

	@PosInQ.deleter
	def PosInQ(self):
		del self._PosInQ
		self._PosInQ = None

	@property
	def QId(self):
		return self._QId

	@QId.setter
	def QId(self, value):
		self._QId = value if type(value) != base_types.auto else self.make_default("QId")

	@QId.deleter
	def QId(self):
		del self._QId
		self._QId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PosInQ', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QId', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
	))

