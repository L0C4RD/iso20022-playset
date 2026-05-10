from . import base_types
from .Max35Text import Max35Text
from .ElementIdentification3 import ElementIdentification3
from .Max350Text import Max350Text
from .Number import Number

class ValidationResult3(base_types._BaseFieldType):

	__slots__ = ["_RuleDesc", "_SeqNb", "_RuleId", "_Elmt"]
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
	def Elmt(self):
		return self._Elmt

	@Elmt.setter
	def Elmt(self, value):
		self._Elmt = value if type(value) != auto else self.make_default("Elmt")

	@Elmt.deleter
	def Elmt(self):
		del self._Elmt
		self._Elmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RuleDesc', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Elmt', type=ElementIdentification3, min=0, max=None, mutex_group=None, array=True),
	))

