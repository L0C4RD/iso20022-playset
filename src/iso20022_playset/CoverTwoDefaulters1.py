import base_types
import LEIIdentifier

class CoverTwoDefaulters1(base_types._BaseFieldType):

	__slots__ = ["_Cover2Id", "_Cover1Id"]
	@property
	def Cover2Id(self):
		return self._Cover2Id

	@Cover2Id.setter
	def Cover2Id(self, value):
		self._Cover2Id = value if type(value) != auto else self.make_default("Cover2Id")

	@Cover2Id.deleter
	def Cover2Id(self):
		del self._Cover2Id
		self._Cover2Id = None

	@property
	def Cover1Id(self):
		return self._Cover1Id

	@Cover1Id.setter
	def Cover1Id(self, value):
		self._Cover1Id = value if type(value) != auto else self.make_default("Cover1Id")

	@Cover1Id.deleter
	def Cover1Id(self):
		del self._Cover1Id
		self._Cover1Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cover2Id', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cover1Id', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

