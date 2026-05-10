import base_types
import PledgeeType1Code
import Max35Text

class PledgeeTypeAndText1(base_types._BaseFieldType):

	__slots__ = ["_PldgeeTp", "_Id"]
	@property
	def PldgeeTp(self):
		return self._PldgeeTp

	@PldgeeTp.setter
	def PldgeeTp(self, value):
		self._PldgeeTp = value if type(value) != auto else self.make_default("PldgeeTp")

	@PldgeeTp.deleter
	def PldgeeTp(self):
		del self._PldgeeTp
		self._PldgeeTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PldgeeTp', type=PledgeeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

