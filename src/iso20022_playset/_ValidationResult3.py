# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ElementIdentification3
from . import Max350Text
from . import Max35Text
from . import Number

class ValidationResult3(base_types._BaseFieldType):

	__slots__ = ["_Elmt", "_RuleDesc", "_RuleId", "_SeqNb"]
	@property
	def Elmt(self):
		return self._Elmt

	@Elmt.setter
	def Elmt(self, value):
		self._Elmt = value if value is not None else base_types.UninitialisedField(self, 'Elmt', ElementIdentification3, True)

	@Elmt.deleter
	def Elmt(self):
		del self._Elmt
		self._Elmt = base_types.UninitialisedField(self, 'Elmt', ElementIdentification3, True)

	@property
	def RuleDesc(self):
		return self._RuleDesc

	@RuleDesc.setter
	def RuleDesc(self, value):
		self._RuleDesc = value if value is not None else base_types.UninitialisedField(self, 'RuleDesc', Max350Text, False)

	@RuleDesc.deleter
	def RuleDesc(self):
		del self._RuleDesc
		self._RuleDesc = base_types.UninitialisedField(self, 'RuleDesc', Max350Text, False)

	@property
	def RuleId(self):
		return self._RuleId

	@RuleId.setter
	def RuleId(self, value):
		self._RuleId = value if value is not None else base_types.UninitialisedField(self, 'RuleId', Max35Text, False)

	@RuleId.deleter
	def RuleId(self):
		del self._RuleId
		self._RuleId = base_types.UninitialisedField(self, 'RuleId', Max35Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Elmt', type=ElementIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RuleDesc', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))