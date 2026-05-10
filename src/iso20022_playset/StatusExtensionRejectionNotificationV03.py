from . import base_types
from .PendingActivity2 import PendingActivity2
from .Reason2 import Reason2
from .MessageIdentification1 import MessageIdentification1
from .TransactionStatus4 import TransactionStatus4
from .DocumentIdentification5 import DocumentIdentification5
from .DocumentIdentification3 import DocumentIdentification3
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class StatusExtensionRejectionNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_RjctnRsn", "_NtfctnId", "_TxId", "_ReqForActn", "_EstblishdBaselnId", "_UsrTxRef", "_NonXtndedSts"]
	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != base_types.auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if type(value) != base_types.auto else self.make_default("ReqForActn")

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = None

	@property
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != base_types.auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if type(value) != base_types.auto else self.make_default("UsrTxRef")

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = None

	@property
	def NonXtndedSts(self):
		return self._NonXtndedSts

	@NonXtndedSts.setter
	def NonXtndedSts(self, value):
		self._NonXtndedSts = value if type(value) != base_types.auto else self.make_default("NonXtndedSts")

	@NonXtndedSts.deleter
	def NonXtndedSts(self):
		del self._NonXtndedSts
		self._NonXtndedSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonXtndedSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
	))

