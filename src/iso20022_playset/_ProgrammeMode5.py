from . import base_types
from ._Max35Text import Max35Text
from ._AdditionalData1 import AdditionalData1

class ProgrammeMode5(base_types._BaseFieldType):

	__slots__ = ["_ApldId", "_AddtlId"]
	@property
	def ApldId(self):
		return self._ApldId

	@ApldId.setter
	def ApldId(self, value):
		self._ApldId = value if type(value) != base_types.auto else self.make_default("ApldId")

	@ApldId.deleter
	def ApldId(self):
		del self._ApldId
		self._ApldId = None

	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != base_types.auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApldId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
	))

