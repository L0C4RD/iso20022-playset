from . import base_types
from ._Max35Text import Max35Text
from ._Number import Number
from ._Max350Text import Max350Text
from ._ElementIdentification1 import ElementIdentification1

class ValidationResult5(base_types._BaseFieldType):

	__slots__ = ["_RuleDesc", "_SeqNb", "_RuleId", "_MisMtchdElmt"]
	@property
	def RuleDesc(self):
		return self._RuleDesc

	@RuleDesc.setter
	def RuleDesc(self, value):
		self._RuleDesc = value if type(value) != base_types.auto else self.make_default("RuleDesc")

	@RuleDesc.deleter
	def RuleDesc(self):
		del self._RuleDesc
		self._RuleDesc = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def RuleId(self):
		return self._RuleId

	@RuleId.setter
	def RuleId(self, value):
		self._RuleId = value if type(value) != base_types.auto else self.make_default("RuleId")

	@RuleId.deleter
	def RuleId(self):
		del self._RuleId
		self._RuleId = None

	@property
	def MisMtchdElmt(self):
		return self._MisMtchdElmt

	@MisMtchdElmt.setter
	def MisMtchdElmt(self, value):
		self._MisMtchdElmt = value if type(value) != base_types.auto else self.make_default("MisMtchdElmt")

	@MisMtchdElmt.deleter
	def MisMtchdElmt(self):
		del self._MisMtchdElmt
		self._MisMtchdElmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RuleDesc', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MisMtchdElmt', type=ElementIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

