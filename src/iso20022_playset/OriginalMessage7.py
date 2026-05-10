from . import base_types
import Party50Choice
import Max35Text
import ISODateTime

class OriginalMessage7(base_types._BaseFieldType):

	__slots__ = ["_OrgnlSndr", "_OrgnlCreDtTm", "_OrgnlMsgNmId", "_OrgnlMsgId"]
	@property
	def OrgnlSndr(self):
		return self._OrgnlSndr

	@OrgnlSndr.setter
	def OrgnlSndr(self, value):
		self._OrgnlSndr = value if type(value) != auto else self.make_default("OrgnlSndr")

	@OrgnlSndr.deleter
	def OrgnlSndr(self):
		del self._OrgnlSndr
		self._OrgnlSndr = None

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if type(value) != auto else self.make_default("OrgnlCreDtTm")

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = None

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if type(value) != auto else self.make_default("OrgnlMsgNmId")

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlSndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

