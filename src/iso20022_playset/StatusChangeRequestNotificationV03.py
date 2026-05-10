from . import base_types
import TransactionStatus3
import MessageIdentification1
import DocumentIdentification3
import PendingActivity2
import TransactionStatus4
import SimpleIdentificationInformation
import Reason2
import BICIdentification1
import DocumentIdentification5

class StatusChangeRequestNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_TxSts", "_Initr", "_NtfctnId", "_ReqForActn", "_ReqRsn", "_EstblishdBaselnId", "_UsrTxRef", "_TxId", "_PropsdStsChng"]
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
	def Initr(self):
		return self._Initr

	@Initr.setter
	def Initr(self, value):
		self._Initr = value if type(value) != auto else self.make_default("Initr")

	@Initr.deleter
	def Initr(self):
		del self._Initr
		self._Initr = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	@property
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if type(value) != auto else self.make_default("ReqForActn")

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = None

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
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

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
	def PropsdStsChng(self):
		return self._PropsdStsChng

	@PropsdStsChng.setter
	def PropsdStsChng(self, value):
		self._PropsdStsChng = value if type(value) != auto else self.make_default("PropsdStsChng")

	@PropsdStsChng.deleter
	def PropsdStsChng(self):
		del self._PropsdStsChng
		self._PropsdStsChng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Initr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRsn', type=Reason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdStsChng', type=TransactionStatus3, min=1, max=1, mutex_group=None, array=False),
	))

