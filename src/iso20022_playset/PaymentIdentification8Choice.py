import base_types
import Max35Text
import QueueTransactionIdentification1
import UUIDv4Identifier
import ShortPaymentIdentification4
import LongPaymentIdentification4
import Max70Text

class PaymentIdentification8Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryId", "_ShrtBizId", "_UETR", "_TxId", "_QId", "_LngBizId"]
	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	@property
	def ShrtBizId(self):
		return self._ShrtBizId

	@ShrtBizId.setter
	def ShrtBizId(self, value):
		self._ShrtBizId = value if type(value) != auto else self.make_default("ShrtBizId")

	@ShrtBizId.deleter
	def ShrtBizId(self):
		del self._ShrtBizId
		self._ShrtBizId = None

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def QId(self):
		return self._QId

	@QId.setter
	def QId(self, value):
		self._QId = value if type(value) != auto else self.make_default("QId")

	@QId.deleter
	def QId(self):
		del self._QId
		self._QId = None

	@property
	def LngBizId(self):
		return self._LngBizId

	@LngBizId.setter
	def LngBizId(self, value):
		self._LngBizId = value if type(value) != auto else self.make_default("LngBizId")

	@LngBizId.deleter
	def LngBizId(self):
		del self._LngBizId
		self._LngBizId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryId', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtBizId', type=ShortPaymentIdentification4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QId', type=QueueTransactionIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LngBizId', type=LongPaymentIdentification4, min=0, max=1, mutex_group=1, array=False),
	))

