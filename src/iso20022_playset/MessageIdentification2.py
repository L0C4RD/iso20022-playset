from . import base_types
from .Max35Text import Max35Text

class MessageIdentification2(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_MsgNmId"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if type(value) != base_types.auto else self.make_default("MsgNmId")

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

