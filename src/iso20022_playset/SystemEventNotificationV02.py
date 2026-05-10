import base_types
import Event2

class SystemEventNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_EvtInf"]
	@property
	def EvtInf(self):
		return self._EvtInf

	@EvtInf.setter
	def EvtInf(self, value):
		self._EvtInf = value if type(value) != auto else self.make_default("EvtInf")

	@EvtInf.deleter
	def EvtInf(self):
		del self._EvtInf
		self._EvtInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtInf', type=Event2, min=1, max=1, mutex_group=None, array=False),
	))

