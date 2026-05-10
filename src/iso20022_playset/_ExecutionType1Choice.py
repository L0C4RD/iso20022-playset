from . import base_types
from ._ISOTime import ISOTime
from ._EventType1Choice import EventType1Choice

class ExecutionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Tm", "_Evt"]
	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if type(value) != base_types.auto else self.make_default("Evt")

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Evt', type=EventType1Choice, min=0, max=1, mutex_group=1, array=False),
	))

