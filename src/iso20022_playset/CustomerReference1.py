from . import base_types
import Max35Text
import Max70Text

class CustomerReference1(base_types._BaseFieldType):

	__slots__ = ["_Dtl", "_Id"]
	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if type(value) != auto else self.make_default("Dtl")

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = None

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
		base_types.FieldEntry(name='Dtl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

