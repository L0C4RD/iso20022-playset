import base_types
import Max350Text
import VoteInstructionType1Choice

class VoteInstructionType1(base_types._BaseFieldType):

	__slots__ = ["_VoteInstrTpCd", "_AddtlInf"]
	@property
	def VoteInstrTpCd(self):
		return self._VoteInstrTpCd

	@VoteInstrTpCd.setter
	def VoteInstrTpCd(self, value):
		self._VoteInstrTpCd = value if type(value) != auto else self.make_default("VoteInstrTpCd")

	@VoteInstrTpCd.deleter
	def VoteInstrTpCd(self):
		del self._VoteInstrTpCd
		self._VoteInstrTpCd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteInstrTpCd', type=VoteInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

