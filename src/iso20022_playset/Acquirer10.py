import base_types
import GenericIdentification177
import Max256Text

class Acquirer10(base_types._BaseFieldType):

	__slots__ = ["_ParamsVrsn", "_Id"]
	@property
	def ParamsVrsn(self):
		return self._ParamsVrsn

	@ParamsVrsn.setter
	def ParamsVrsn(self, value):
		self._ParamsVrsn = value if type(value) != auto else self.make_default("ParamsVrsn")

	@ParamsVrsn.deleter
	def ParamsVrsn(self):
		del self._ParamsVrsn
		self._ParamsVrsn = None

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
		base_types.FieldEntry(name='ParamsVrsn', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification177, min=0, max=1, mutex_group=None, array=False),
	))

