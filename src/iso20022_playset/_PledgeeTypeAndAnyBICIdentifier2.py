from . import base_types
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._PledgeeType1Code import PledgeeType1Code

class PledgeeTypeAndAnyBICIdentifier2(base_types._BaseFieldType):

	__slots__ = ["_PldgeeTp", "_Id"]
	@property
	def PldgeeTp(self):
		return self._PldgeeTp

	@PldgeeTp.setter
	def PldgeeTp(self, value):
		self._PldgeeTp = value if type(value) != base_types.auto else self.make_default("PldgeeTp")

	@PldgeeTp.deleter
	def PldgeeTp(self):
		del self._PldgeeTp
		self._PldgeeTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PldgeeTp', type=PledgeeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AnyBICDec2014Identifier, min=1, max=1, mutex_group=None, array=False),
	))

