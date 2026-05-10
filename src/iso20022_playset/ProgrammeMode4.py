import base_types
import Max35Text
import AdditionalData1
import PartyType20Code

class ProgrammeMode4(base_types._BaseFieldType):

	__slots__ = ["_IdSelctdBy", "_AddtlId", "_PropsdId", "_ApldId"]
	@property
	def IdSelctdBy(self):
		return self._IdSelctdBy

	@IdSelctdBy.setter
	def IdSelctdBy(self, value):
		self._IdSelctdBy = value if type(value) != auto else self.make_default("IdSelctdBy")

	@IdSelctdBy.deleter
	def IdSelctdBy(self):
		del self._IdSelctdBy
		self._IdSelctdBy = None

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

	@property
	def PropsdId(self):
		return self._PropsdId

	@PropsdId.setter
	def PropsdId(self, value):
		self._PropsdId = value if type(value) != auto else self.make_default("PropsdId")

	@PropsdId.deleter
	def PropsdId(self):
		del self._PropsdId
		self._PropsdId = None

	@property
	def ApldId(self):
		return self._ApldId

	@ApldId.setter
	def ApldId(self, value):
		self._ApldId = value if type(value) != auto else self.make_default("ApldId")

	@ApldId.deleter
	def ApldId(self):
		del self._ApldId
		self._ApldId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdSelctdBy', type=PartyType20Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApldId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

