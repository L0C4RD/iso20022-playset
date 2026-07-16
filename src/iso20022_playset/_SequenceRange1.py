# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class SequenceRange1(base_types._BaseFieldType):

	__slots__ = ["_FrSeq", "_ToSeq"]
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
		base_types.FieldEntry(name='FrSeq', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToSeq', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))