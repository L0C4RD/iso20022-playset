# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingExceptionOrExemption3Choice
from . import ClearingPartyAndTime21Choice
from . import ClearingPartyAndTime22Choice

class Cleared23Choice(base_types._BaseFieldType):

	__slots__ = ["_Clrd", "_IntndToClear", "_NonClrd"]
	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if value is not None else base_types.UninitialisedField(self, 'Clrd', ClearingPartyAndTime21Choice, False)

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = base_types.UninitialisedField(self, 'Clrd', ClearingPartyAndTime21Choice, False)

	@property
	def IntndToClear(self):
		return self._IntndToClear

	@IntndToClear.setter
	def IntndToClear(self, value):
		self._IntndToClear = value if value is not None else base_types.UninitialisedField(self, 'IntndToClear', ClearingPartyAndTime22Choice, False)

	@IntndToClear.deleter
	def IntndToClear(self):
		del self._IntndToClear
		self._IntndToClear = base_types.UninitialisedField(self, 'IntndToClear', ClearingPartyAndTime22Choice, False)

	@property
	def NonClrd(self):
		return self._NonClrd

	@NonClrd.setter
	def NonClrd(self, value):
		self._NonClrd = value if value is not None else base_types.UninitialisedField(self, 'NonClrd', ClearingExceptionOrExemption3Choice, False)

	@NonClrd.deleter
	def NonClrd(self):
		del self._NonClrd
		self._NonClrd = base_types.UninitialisedField(self, 'NonClrd', ClearingExceptionOrExemption3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clrd', type=ClearingPartyAndTime21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntndToClear', type=ClearingPartyAndTime22Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonClrd', type=ClearingExceptionOrExemption3Choice, min=0, max=1, mutex_group=1, array=False),
	))