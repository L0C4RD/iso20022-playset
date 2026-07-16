# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode

class Cleared4Choice(base_types._BaseFieldType):

	__slots__ = ["_Clrd", "_NonClrd"]
	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if value is not None else base_types.UninitialisedField(self, 'Clrd', NoReasonCode, False)

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = base_types.UninitialisedField(self, 'Clrd', NoReasonCode, False)

	@property
	def NonClrd(self):
		return self._NonClrd

	@NonClrd.setter
	def NonClrd(self, value):
		self._NonClrd = value if value is not None else base_types.UninitialisedField(self, 'NonClrd', NoReasonCode, False)

	@NonClrd.deleter
	def NonClrd(self):
		del self._NonClrd
		self._NonClrd = base_types.UninitialisedField(self, 'NonClrd', NoReasonCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonClrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))