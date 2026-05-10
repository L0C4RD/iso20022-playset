import base_types
import ISOTime
import EventType1Choice

class ExecutionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Evt", "_Tm"]
	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if type(value) != auto else self.make_default("Evt")

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Evt', type=EventType1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=1, array=False),
	))

