# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SafekeepingAccount18

class CancelInstruction5(base_types._BaseFieldType):

	__slots__ = ["_InstdPos", "_SnglInstrId"]
	@property
	def InstdPos(self):
		return self._InstdPos

	@InstdPos.setter
	def InstdPos(self, value):
		self._InstdPos = value if value is not None else base_types.UninitialisedField(self, 'InstdPos', SafekeepingAccount18, False)

	@InstdPos.deleter
	def InstdPos(self):
		del self._InstdPos
		self._InstdPos = base_types.UninitialisedField(self, 'InstdPos', SafekeepingAccount18, False)

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if value is not None else base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdPos', type=SafekeepingAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))