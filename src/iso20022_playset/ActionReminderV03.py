import base_types
import DocumentIdentification5
import PendingActivity2
import TransactionStatus4
import SimpleIdentificationInformation
import MessageIdentification1
import DocumentIdentification3

class ActionReminderV03(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_RmndrId", "_PdgReqForActn", "_MsgReqrngActn", "_UsrTxRef", "_TxSts", "_EstblishdBaselnId"]
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
	def RmndrId(self):
		return self._RmndrId

	@RmndrId.setter
	def RmndrId(self, value):
		self._RmndrId = value if type(value) != auto else self.make_default("RmndrId")

	@RmndrId.deleter
	def RmndrId(self):
		del self._RmndrId
		self._RmndrId = None

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if type(value) != auto else self.make_default("PdgReqForActn")

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = None

	@property
	def MsgReqrngActn(self):
		return self._MsgReqrngActn

	@MsgReqrngActn.setter
	def MsgReqrngActn(self, value):
		self._MsgReqrngActn = value if type(value) != auto else self.make_default("MsgReqrngActn")

	@MsgReqrngActn.deleter
	def MsgReqrngActn(self):
		del self._MsgReqrngActn
		self._MsgReqrngActn = None

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if type(value) != auto else self.make_default("UsrTxRef")

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmndrId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgReqrngActn', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
	))

