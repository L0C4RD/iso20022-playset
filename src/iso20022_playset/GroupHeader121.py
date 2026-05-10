import base_types
import Max35Text
import ISODateTime
import Party50Choice

class GroupHeader121(base_types._BaseFieldType):

	__slots__ = ["_MsgRcpt", "_MsgId", "_CreDtTm"]
	@property
	def MsgRcpt(self):
		return self._MsgRcpt

	@MsgRcpt.setter
	def MsgRcpt(self, value):
		self._MsgRcpt = value if type(value) != auto else self.make_default("MsgRcpt")

	@MsgRcpt.deleter
	def MsgRcpt(self):
		del self._MsgRcpt
		self._MsgRcpt = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgRcpt', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

