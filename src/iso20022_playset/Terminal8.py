import base_types
import Max16Text
import AdditionalData1

class Terminal8(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AddtlId"]
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
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
	))

