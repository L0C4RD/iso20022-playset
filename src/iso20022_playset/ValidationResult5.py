import base_types
import Max350Text
import ElementIdentification1
import Number
import Max35Text

class ValidationResult5(base_types._BaseFieldType):

	__slots__ = ["_RuleId", "_RuleDesc", "_SeqNb", "_MisMtchdElmt"]
	@property
	def RuleId(self):
		return self._RuleId

	@RuleId.setter
	def RuleId(self, value):
		self._RuleId = value if type(value) != auto else self.make_default("RuleId")

	@RuleId.deleter
	def RuleId(self):
		del self._RuleId
		self._RuleId = None

	@property
	def RuleDesc(self):
		return self._RuleDesc

	@RuleDesc.setter
	def RuleDesc(self, value):
		self._RuleDesc = value if type(value) != auto else self.make_default("RuleDesc")

	@RuleDesc.deleter
	def RuleDesc(self):
		del self._RuleDesc
		self._RuleDesc = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def MisMtchdElmt(self):
		return self._MisMtchdElmt

	@MisMtchdElmt.setter
	def MisMtchdElmt(self, value):
		self._MisMtchdElmt = value if type(value) != auto else self.make_default("MisMtchdElmt")

	@MisMtchdElmt.deleter
	def MisMtchdElmt(self):
		del self._MisMtchdElmt
		self._MisMtchdElmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RuleId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleDesc', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MisMtchdElmt', type=ElementIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

