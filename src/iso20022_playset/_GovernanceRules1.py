from . import base_types
from .Location1 import Location1
from .GovernanceIdentification1Choice import GovernanceIdentification1Choice

class GovernanceRules1(base_types._BaseFieldType):

	__slots__ = ["_RuleId", "_Jursdctn", "_AplblLaw"]
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
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if type(value) != base_types.auto else self.make_default("Jursdctn")

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = None

	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if type(value) != base_types.auto else self.make_default("AplblLaw")

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RuleId', type=GovernanceIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Location1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AplblLaw', type=Location1, min=0, max=1, mutex_group=None, array=False),
	))

