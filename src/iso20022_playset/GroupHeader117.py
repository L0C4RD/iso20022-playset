from . import base_types
import Party50Choice
import Max35Text
import ISODateTime

class GroupHeader117(base_types._BaseFieldType):

	__slots__ = ["_MsgSndr", "_MsgId", "_CreDtTm"]
	@property
	def MsgSndr(self):
		return self._MsgSndr

	@MsgSndr.setter
	def MsgSndr(self, value):
		self._MsgSndr = value if type(value) != auto else self.make_default("MsgSndr")

	@MsgSndr.deleter
	def MsgSndr(self):
		del self._MsgSndr
		self._MsgSndr = None

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
		base_types.FieldEntry(name='MsgSndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

