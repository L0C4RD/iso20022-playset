from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator

class ContractRegistrationStatementCriteria1(base_types._BaseFieldType):

	__slots__ = ["_RgltryRuleVldtn", "_SpprtgDocJrnl", "_AddtlSpprtgDocJrnl", "_TxJrnl"]
	@property
	def RgltryRuleVldtn(self):
		return self._RgltryRuleVldtn

	@RgltryRuleVldtn.setter
	def RgltryRuleVldtn(self, value):
		self._RgltryRuleVldtn = value if type(value) != base_types.auto else self.make_default("RgltryRuleVldtn")

	@RgltryRuleVldtn.deleter
	def RgltryRuleVldtn(self):
		del self._RgltryRuleVldtn
		self._RgltryRuleVldtn = None

	@property
	def SpprtgDocJrnl(self):
		return self._SpprtgDocJrnl

	@SpprtgDocJrnl.setter
	def SpprtgDocJrnl(self, value):
		self._SpprtgDocJrnl = value if type(value) != base_types.auto else self.make_default("SpprtgDocJrnl")

	@SpprtgDocJrnl.deleter
	def SpprtgDocJrnl(self):
		del self._SpprtgDocJrnl
		self._SpprtgDocJrnl = None

	@property
	def AddtlSpprtgDocJrnl(self):
		return self._AddtlSpprtgDocJrnl

	@AddtlSpprtgDocJrnl.setter
	def AddtlSpprtgDocJrnl(self, value):
		self._AddtlSpprtgDocJrnl = value if type(value) != base_types.auto else self.make_default("AddtlSpprtgDocJrnl")

	@AddtlSpprtgDocJrnl.deleter
	def AddtlSpprtgDocJrnl(self):
		del self._AddtlSpprtgDocJrnl
		self._AddtlSpprtgDocJrnl = None

	@property
	def TxJrnl(self):
		return self._TxJrnl

	@TxJrnl.setter
	def TxJrnl(self, value):
		self._TxJrnl = value if type(value) != base_types.auto else self.make_default("TxJrnl")

	@TxJrnl.deleter
	def TxJrnl(self):
		del self._TxJrnl
		self._TxJrnl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RgltryRuleVldtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpprtgDocJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSpprtgDocJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxJrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

