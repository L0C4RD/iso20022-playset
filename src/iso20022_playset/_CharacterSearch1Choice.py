# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class CharacterSearch1Choice(base_types._BaseFieldType):

	__slots__ = ["_CT", "_EQ", "_NCT", "_NEQ"]
	@property
	def CT(self):
		return self._CT

	@CT.setter
	def CT(self, value):
		self._CT = value if value is not None else base_types.UninitialisedField(self, 'CT', Max35Text, False)

	@CT.deleter
	def CT(self):
		del self._CT
		self._CT = base_types.UninitialisedField(self, 'CT', Max35Text, False)

	@property
	def EQ(self):
		return self._EQ

	@EQ.setter
	def EQ(self, value):
		self._EQ = value if value is not None else base_types.UninitialisedField(self, 'EQ', Max35Text, False)

	@EQ.deleter
	def EQ(self):
		del self._EQ
		self._EQ = base_types.UninitialisedField(self, 'EQ', Max35Text, False)

	@property
	def NCT(self):
		return self._NCT

	@NCT.setter
	def NCT(self, value):
		self._NCT = value if value is not None else base_types.UninitialisedField(self, 'NCT', Max35Text, False)

	@NCT.deleter
	def NCT(self):
		del self._NCT
		self._NCT = base_types.UninitialisedField(self, 'NCT', Max35Text, False)

	@property
	def NEQ(self):
		return self._NEQ

	@NEQ.setter
	def NEQ(self, value):
		self._NEQ = value if value is not None else base_types.UninitialisedField(self, 'NEQ', Max35Text, False)

	@NEQ.deleter
	def NEQ(self):
		del self._NEQ
		self._NEQ = base_types.UninitialisedField(self, 'NEQ', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CT', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EQ', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NCT', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQ', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))