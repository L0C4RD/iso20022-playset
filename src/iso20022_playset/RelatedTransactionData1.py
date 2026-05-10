import base_types
import UUIDv4Identifier

class RelatedTransactionData1(base_types._BaseFieldType):

	__slots__ = ["_SubUETR", "_MstrUETR"]
	@property
	def SubUETR(self):
		return self._SubUETR

	@SubUETR.setter
	def SubUETR(self, value):
		self._SubUETR = value if type(value) != auto else self.make_default("SubUETR")

	@SubUETR.deleter
	def SubUETR(self):
		del self._SubUETR
		self._SubUETR = None

	@property
	def MstrUETR(self):
		return self._MstrUETR

	@MstrUETR.setter
	def MstrUETR(self, value):
		self._MstrUETR = value if type(value) != auto else self.make_default("MstrUETR")

	@MstrUETR.deleter
	def MstrUETR(self):
		del self._MstrUETR
		self._MstrUETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubUETR', type=UUIDv4Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

