import base_types
import Position1
import GenericIdentification165

class PositionAccount2(base_types._BaseFieldType):

	__slots__ = ["_Pos", "_Id"]
	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if type(value) != auto else self.make_default("Pos")

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = None

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
		base_types.FieldEntry(name='Pos', type=Position1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
	))

