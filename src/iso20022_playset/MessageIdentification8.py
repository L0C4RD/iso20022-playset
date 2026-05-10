from . import base_types
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .ISODateTime import ISODateTime
from .Max35Text import Max35Text

class MessageIdentification8(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_FrstAgt"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if type(value) != base_types.auto else self.make_default("FrstAgt")

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

