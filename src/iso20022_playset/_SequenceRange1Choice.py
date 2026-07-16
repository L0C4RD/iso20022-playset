# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SequenceRange1

class SequenceRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQSeq", "_FrSeq", "_FrToSeq", "_NEQSeq", "_ToSeq"]
	@property
	def EQSeq(self):
		return self._EQSeq

	@EQSeq.setter
	def EQSeq(self, value):
		self._EQSeq = value if value is not None else base_types.UninitialisedField(self, 'EQSeq', Max35Text, True)

	@EQSeq.deleter
	def EQSeq(self):
		del self._EQSeq
		self._EQSeq = base_types.UninitialisedField(self, 'EQSeq', Max35Text, True)

	@property
	def FrSeq(self):
		return self._FrSeq

	@FrSeq.setter
	def FrSeq(self, value):
		self._FrSeq = value if value is not None else base_types.UninitialisedField(self, 'FrSeq', Max35Text, False)

	@FrSeq.deleter
	def FrSeq(self):
		del self._FrSeq
		self._FrSeq = base_types.UninitialisedField(self, 'FrSeq', Max35Text, False)

	@property
	def FrToSeq(self):
		return self._FrToSeq

	@FrToSeq.setter
	def FrToSeq(self, value):
		self._FrToSeq = value if value is not None else base_types.UninitialisedField(self, 'FrToSeq', SequenceRange1, True)

	@FrToSeq.deleter
	def FrToSeq(self):
		del self._FrToSeq
		self._FrToSeq = base_types.UninitialisedField(self, 'FrToSeq', SequenceRange1, True)

	@property
	def NEQSeq(self):
		return self._NEQSeq

	@NEQSeq.setter
	def NEQSeq(self, value):
		self._NEQSeq = value if value is not None else base_types.UninitialisedField(self, 'NEQSeq', Max35Text, True)

	@NEQSeq.deleter
	def NEQSeq(self):
		del self._NEQSeq
		self._NEQSeq = base_types.UninitialisedField(self, 'NEQSeq', Max35Text, True)

	@property
	def ToSeq(self):
		return self._ToSeq

	@ToSeq.setter
	def ToSeq(self, value):
		self._ToSeq = value if value is not None else base_types.UninitialisedField(self, 'ToSeq', Max35Text, False)

	@ToSeq.deleter
	def ToSeq(self):
		del self._ToSeq
		self._ToSeq = base_types.UninitialisedField(self, 'ToSeq', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EQSeq', type=Max35Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='FrSeq', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToSeq', type=SequenceRange1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='NEQSeq', type=Max35Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ToSeq', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))