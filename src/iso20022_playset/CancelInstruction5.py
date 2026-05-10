from . import base_types
import SafekeepingAccount18
import Max35Text

class CancelInstruction5(base_types._BaseFieldType):

	__slots__ = ["_SnglInstrId", "_InstdPos"]
	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if type(value) != auto else self.make_default("SnglInstrId")

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = None

	@property
	def InstdPos(self):
		return self._InstdPos

	@InstdPos.setter
	def InstdPos(self, value):
		self._InstdPos = value if type(value) != auto else self.make_default("InstdPos")

	@InstdPos.deleter
	def InstdPos(self):
		del self._InstdPos
		self._InstdPos = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdPos', type=SafekeepingAccount18, min=0, max=1, mutex_group=None, array=False),
	))

