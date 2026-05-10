from . import base_types
import Party50Choice
import Max35Text
import ISODateTime

class OriginalMessage6(base_types._BaseFieldType):

	__slots__ = ["_OrgnlMsgNmId", "_OrgnlMsgId", "_OrgnlSndr", "_OrgnlCreDtTm", "_OrgnlPackgId", "_OrgnlRcrdId"]
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
	def OrgnlPackgId(self):
		return self._OrgnlPackgId

	@OrgnlPackgId.setter
	def OrgnlPackgId(self, value):
		self._OrgnlPackgId = value if type(value) != auto else self.make_default("OrgnlPackgId")

	@OrgnlPackgId.deleter
	def OrgnlPackgId(self):
		del self._OrgnlPackgId
		self._OrgnlPackgId = None

	@property
	def OrgnlRcrdId(self):
		return self._OrgnlRcrdId

	@OrgnlRcrdId.setter
	def OrgnlRcrdId(self, value):
		self._OrgnlRcrdId = value if type(value) != auto else self.make_default("OrgnlRcrdId")

	@OrgnlRcrdId.deleter
	def OrgnlRcrdId(self):
		del self._OrgnlRcrdId
		self._OrgnlRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPackgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRcrdId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

