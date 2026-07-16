# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ElementIdentification1
from . import Max350Text
from . import Max35Text
from . import Number

class ValidationResult5(base_types._BaseFieldType):

	__slots__ = ["_MisMtchdElmt", "_RuleDesc", "_RuleId", "_SeqNb"]
	@property
	def MisMtchdElmt(self):
		return self._MisMtchdElmt

	@MisMtchdElmt.setter
	def MisMtchdElmt(self, value):
		self._MisMtchdElmt = value if value is not None else base_types.UninitialisedField(self, 'MisMtchdElmt', ElementIdentification1, True)

	@MisMtchdElmt.deleter
	def MisMtchdElmt(self):
		del self._MisMtchdElmt
		self._MisMtchdElmt = base_types.UninitialisedField(self, 'MisMtchdElmt', ElementIdentification1, True)

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
		base_types.FieldEntry(name='MisMtchdElmt', type=ElementIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RuleDesc', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RuleId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))