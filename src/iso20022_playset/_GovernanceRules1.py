# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GovernanceIdentification1Choice
from . import Location1

class GovernanceRules1(base_types._BaseFieldType):

	__slots__ = ["_AplblLaw", "_Jursdctn", "_RuleId"]
	@property
	def AplblLaw(self):
		return self._AplblLaw

	@AplblLaw.setter
	def AplblLaw(self, value):
		self._AplblLaw = value if value is not None else base_types.UninitialisedField(self, 'AplblLaw', Location1, False)

	@AplblLaw.deleter
	def AplblLaw(self):
		del self._AplblLaw
		self._AplblLaw = base_types.UninitialisedField(self, 'AplblLaw', Location1, False)

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if value is not None else base_types.UninitialisedField(self, 'Jursdctn', Location1, True)

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = base_types.UninitialisedField(self, 'Jursdctn', Location1, True)

	@property
	def RuleId(self):
		return self._RuleId

	@RuleId.setter
	def RuleId(self, value):
		self._RuleId = value if value is not None else base_types.UninitialisedField(self, 'RuleId', GovernanceIdentification1Choice, False)

	@RuleId.deleter
	def RuleId(self):
		del self._RuleId
		self._RuleId = base_types.UninitialisedField(self, 'RuleId', GovernanceIdentification1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AplblLaw', type=Location1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Location1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RuleId', type=GovernanceIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))