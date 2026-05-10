import base_types
import Max35Text
import ISODate

class DocumentIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Id", "_DtOfIsse"]
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

	@property
	def DtOfIsse(self):
		return self._DtOfIsse

	@DtOfIsse.setter
	def DtOfIsse(self, value):
		self._DtOfIsse = value if type(value) != auto else self.make_default("DtOfIsse")

	@DtOfIsse.deleter
	def DtOfIsse(self):
		del self._DtOfIsse
		self._DtOfIsse = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfIsse', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

