from . import base_types
from .PaymentInstruction33 import PaymentInstruction33
from .PaymentIdentification8Choice import PaymentIdentification8Choice

class TransactionModification7(base_types._BaseFieldType):

	__slots__ = ["_PmtId", "_NewPmtValSet"]
	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != base_types.auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

	@property
	def NewPmtValSet(self):
		return self._NewPmtValSet

	@NewPmtValSet.setter
	def NewPmtValSet(self, value):
		self._NewPmtValSet = value if type(value) != base_types.auto else self.make_default("NewPmtValSet")

	@NewPmtValSet.deleter
	def NewPmtValSet(self):
		del self._NewPmtValSet
		self._NewPmtValSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPmtValSet', type=PaymentInstruction33, min=1, max=1, mutex_group=None, array=False),
	))

