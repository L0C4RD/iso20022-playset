from . import base_types
import VoteInstructionType1Choice
import Number

class VoteTypeAndQuantity1(base_types._BaseFieldType):

	__slots__ = ["_VoteInstrTp", "_VoteQty"]
	@property
	def VoteInstrTp(self):
		return self._VoteInstrTp

	@VoteInstrTp.setter
	def VoteInstrTp(self, value):
		self._VoteInstrTp = value if type(value) != auto else self.make_default("VoteInstrTp")

	@VoteInstrTp.deleter
	def VoteInstrTp(self):
		del self._VoteInstrTp
		self._VoteInstrTp = None

	@property
	def VoteQty(self):
		return self._VoteQty

	@VoteQty.setter
	def VoteQty(self, value):
		self._VoteQty = value if type(value) != auto else self.make_default("VoteQty")

	@VoteQty.deleter
	def VoteQty(self):
		del self._VoteQty
		self._VoteQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VoteInstrTp', type=VoteInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteQty', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

