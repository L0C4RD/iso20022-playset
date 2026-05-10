from . import base_types
from .TransactionStatus4 import TransactionStatus4
from .DocumentIdentification5 import DocumentIdentification5
from .Count1 import Count1
from .SimpleIdentificationInformation import SimpleIdentificationInformation
from .DocumentIdentification3 import DocumentIdentification3
from .MessageIdentification1 import MessageIdentification1
from .ValidationResult3 import ValidationResult3
from .PendingActivity2 import PendingActivity2

class ErrorReportV03(base_types._BaseFieldType):

	__slots__ = ["_TxSts", "_TxId", "_RptId", "_ErrDesc", "_RjctdMsgRef", "_NbOfErrs", "_ReqForActn", "_UsrTxRef", "_EstblishdBaselnId"]
	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != base_types.auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

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
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def ErrDesc(self):
		return self._ErrDesc

	@ErrDesc.setter
	def ErrDesc(self, value):
		self._ErrDesc = value if type(value) != base_types.auto else self.make_default("ErrDesc")

	@ErrDesc.deleter
	def ErrDesc(self):
		del self._ErrDesc
		self._ErrDesc = None

	@property
	def RjctdMsgRef(self):
		return self._RjctdMsgRef

	@RjctdMsgRef.setter
	def RjctdMsgRef(self, value):
		self._RjctdMsgRef = value if type(value) != base_types.auto else self.make_default("RjctdMsgRef")

	@RjctdMsgRef.deleter
	def RjctdMsgRef(self):
		del self._RjctdMsgRef
		self._RjctdMsgRef = None

	@property
	def NbOfErrs(self):
		return self._NbOfErrs

	@NbOfErrs.setter
	def NbOfErrs(self, value):
		self._NbOfErrs = value if type(value) != base_types.auto else self.make_default("NbOfErrs")

	@NbOfErrs.deleter
	def NbOfErrs(self):
		del self._NbOfErrs
		self._NbOfErrs = None

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
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != base_types.auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrDesc', type=ValidationResult3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RjctdMsgRef', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfErrs', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
	))

