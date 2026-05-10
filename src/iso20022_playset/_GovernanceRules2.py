from . import base_types
from ._GovernanceIdentification1Choice import GovernanceIdentification1Choice
from ._Location1 import Location1
from ._xs:ID import xs:ID

class GovernanceRules2(base_types._BaseFieldType):

	__slots__ = ["_AplblLaw", "_Id", "_Jursdctn", "_RuleId"]
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

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
	def RuleId(self):
		return self._RuleId

	@RuleId.setter
	def RuleId(self, value):
		self._RuleId = value if type(value) != base_types.auto else self.make_default("RuleId")

	@RuleId.deleter
	def RuleId(self):
		del self._RuleId
		self._RuleId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblLaw', type=Location1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Location1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RuleId', type=GovernanceIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))

