import base_types
import Max35Text
import PaymentIdentification15
import ISODateTime

class OriginalTransactionReference43(base_types._BaseFieldType):

	__slots__ = ["_MsgNmId", "_CreDtTm", "_OrgnlTx", "_MsgId"]
	@property
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if type(value) != auto else self.make_default("MsgNmId")

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = None

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

	@property
	def OrgnlTx(self):
		return self._OrgnlTx

	@OrgnlTx.setter
	def OrgnlTx(self, value):
		self._OrgnlTx = value if type(value) != auto else self.make_default("OrgnlTx")

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTx', type=PaymentIdentification15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

