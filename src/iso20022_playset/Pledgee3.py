from . import base_types
from .LEIIdentifier import LEIIdentifier
from .PledgeeFormat5Choice import PledgeeFormat5Choice

class Pledgee3(base_types._BaseFieldType):

	__slots__ = ["_PldgeeTpAndId", "_LEI"]
	@property
	def PldgeeTpAndId(self):
		return self._PldgeeTpAndId

	@PldgeeTpAndId.setter
	def PldgeeTpAndId(self, value):
		self._PldgeeTpAndId = value if type(value) != base_types.auto else self.make_default("PldgeeTpAndId")

	@PldgeeTpAndId.deleter
	def PldgeeTpAndId(self):
		del self._PldgeeTpAndId
		self._PldgeeTpAndId = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PldgeeTpAndId', type=PledgeeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

