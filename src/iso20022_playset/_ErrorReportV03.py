# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Count1
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import MessageIdentification1
from . import PendingActivity2
from . import SimpleIdentificationInformation
from . import TransactionStatus4
from . import ValidationResult3

class ErrorReportV03(base_types._BaseFieldType):

	__slots__ = ["_ErrDesc", "_EstblishdBaselnId", "_NbOfErrs", "_ReqForActn", "_RjctdMsgRef", "_RptId", "_TxId", "_TxSts", "_UsrTxRef"]
	@property
	def ErrDesc(self):
		return self._ErrDesc

	@ErrDesc.setter
	def ErrDesc(self, value):
		self._ErrDesc = value if value is not None else base_types.UninitialisedField(self, 'ErrDesc', ValidationResult3, True)

	@ErrDesc.deleter
	def ErrDesc(self):
		del self._ErrDesc
		self._ErrDesc = base_types.UninitialisedField(self, 'ErrDesc', ValidationResult3, True)

	@property
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if value is not None else base_types.UninitialisedField(self, 'EstblishdBaselnId', DocumentIdentification3, False)

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = base_types.UninitialisedField(self, 'EstblishdBaselnId', DocumentIdentification3, False)

	@property
	def NbOfErrs(self):
		return self._NbOfErrs

	@NbOfErrs.setter
	def NbOfErrs(self, value):
		self._NbOfErrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfErrs', Count1, False)

	@NbOfErrs.deleter
	def NbOfErrs(self):
		del self._NbOfErrs
		self._NbOfErrs = base_types.UninitialisedField(self, 'NbOfErrs', Count1, False)

	@property
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if value is not None else base_types.UninitialisedField(self, 'ReqForActn', PendingActivity2, False)

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = base_types.UninitialisedField(self, 'ReqForActn', PendingActivity2, False)

	@property
	def RjctdMsgRef(self):
		return self._RjctdMsgRef

	@RjctdMsgRef.setter
	def RjctdMsgRef(self, value):
		self._RjctdMsgRef = value if value is not None else base_types.UninitialisedField(self, 'RjctdMsgRef', MessageIdentification1, False)

	@RjctdMsgRef.deleter
	def RjctdMsgRef(self):
		del self._RjctdMsgRef
		self._RjctdMsgRef = base_types.UninitialisedField(self, 'RjctdMsgRef', MessageIdentification1, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', TransactionStatus4, False)

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if value is not None else base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, False)

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ErrDesc', type=ValidationResult3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfErrs', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdMsgRef', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=1, mutex_group=None, array=False),
	))