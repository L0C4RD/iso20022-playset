from . import base_types
from .Max100KBinary import Max100KBinary

class DeviceTransmitMessageResponse1(base_types._BaseFieldType):

	__slots__ = ["_RcvdMsg"]
	@property
	def RcvdMsg(self):
		return self._RcvdMsg

	@RcvdMsg.setter
	def RcvdMsg(self, value):
		self._RcvdMsg = value if type(value) != base_types.auto else self.make_default("RcvdMsg")

	@RcvdMsg.deleter
	def RcvdMsg(self):
		del self._RcvdMsg
		self._RcvdMsg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvdMsg', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))

