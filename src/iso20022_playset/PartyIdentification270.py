import base_types
import PartyAdditionalIdentification2Choice
import PartyIdentification246Choice

class PartyIdentification270(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AddtlIdInf"]
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
	def AddtlIdInf(self):
		return self._AddtlIdInf

	@AddtlIdInf.setter
	def AddtlIdInf(self, value):
		self._AddtlIdInf = value if type(value) != auto else self.make_default("AddtlIdInf")

	@AddtlIdInf.deleter
	def AddtlIdInf(self):
		del self._AddtlIdInf
		self._AddtlIdInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification246Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlIdInf', type=PartyAdditionalIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

