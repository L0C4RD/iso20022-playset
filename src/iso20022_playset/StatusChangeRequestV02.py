import base_types
import MessageIdentification1
import Reason2
import TransactionStatus3
import SimpleIdentificationInformation

class StatusChangeRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ReqRsn", "_SubmitrTxRef", "_ReqId", "_TxId", "_ReqdSts"]
	@property
	def ReqRsn(self):
		return self._ReqRsn

	@ReqRsn.setter
	def ReqRsn(self, value):
		self._ReqRsn = value if type(value) != auto else self.make_default("ReqRsn")

	@ReqRsn.deleter
	def ReqRsn(self):
		del self._ReqRsn
		self._ReqRsn = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

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
	def ReqdSts(self):
		return self._ReqdSts

	@ReqdSts.setter
	def ReqdSts(self, value):
		self._ReqdSts = value if type(value) != auto else self.make_default("ReqdSts")

	@ReqdSts.deleter
	def ReqdSts(self):
		del self._ReqdSts
		self._ReqdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqRsn', type=Reason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSts', type=TransactionStatus3, min=1, max=1, mutex_group=None, array=False),
	))

