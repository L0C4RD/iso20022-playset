from . import base_types
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._PaymentReturnReason7 import PaymentReturnReason7

class OriginalGroupHeader19(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlMsgNmId", "_RtrRsnInf"]
	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if type(value) != base_types.auto else self.make_default("OrgnlCreDtTm")

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = None

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgId")

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = None

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgNmId")

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = None

	@property
	def RtrRsnInf(self):
		return self._RtrRsnInf

	@RtrRsnInf.setter
	def RtrRsnInf(self, value):
		self._RtrRsnInf = value if type(value) != base_types.auto else self.make_default("RtrRsnInf")

	@RtrRsnInf.deleter
	def RtrRsnInf(self):
		del self._RtrRsnInf
		self._RtrRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrRsnInf', type=PaymentReturnReason7, min=0, max=None, mutex_group=None, array=True),
	))

