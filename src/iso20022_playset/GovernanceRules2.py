import base_types
import xs:ID
import GovernanceIdentification1Choice
import Location1

class GovernanceRules2(base_types._BaseFieldType):

	__slots__ = ["_Jursdctn", "_Id", "_AplblLaw", "_RuleId"]
	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if type(value) != auto else self.make_default("Jursdctn")

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if type(value) != auto else self.make_default("AplblLaw")

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Jursdctn', type=Location1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AplblLaw', type=Location1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleId', type=GovernanceIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))

