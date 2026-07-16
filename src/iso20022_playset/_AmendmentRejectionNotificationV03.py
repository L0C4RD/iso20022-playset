# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import Count1
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import MessageIdentification1
from . import PendingActivity2
from . import RejectionReason1Choice
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class AmendmentRejectionNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_DltaRptRef", "_EstblishdBaselnId", "_Initr", "_NtfctnId", "_ReqForActn", "_RjctdAmdmntNb", "_RjctnRsn", "_TxId", "_TxSts", "_UsrTxRef"]
	@property
	def DltaRptRef(self):
		return self._DltaRptRef

	@DltaRptRef.setter
	def DltaRptRef(self, value):
		self._DltaRptRef = value if value is not None else base_types.UninitialisedField(self, 'DltaRptRef', MessageIdentification1, False)

	@DltaRptRef.deleter
	def DltaRptRef(self):
		del self._DltaRptRef
		self._DltaRptRef = base_types.UninitialisedField(self, 'DltaRptRef', MessageIdentification1, False)

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
	def Initr(self):
		return self._Initr

	@Initr.setter
	def Initr(self, value):
		self._Initr = value if value is not None else base_types.UninitialisedField(self, 'Initr', BICIdentification1, False)

	@Initr.deleter
	def Initr(self):
		del self._Initr
		self._Initr = base_types.UninitialisedField(self, 'Initr', BICIdentification1, False)

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnId', MessageIdentification1, False)

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = base_types.UninitialisedField(self, 'NtfctnId', MessageIdentification1, False)

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
	def RjctdAmdmntNb(self):
		return self._RjctdAmdmntNb

	@RjctdAmdmntNb.setter
	def RjctdAmdmntNb(self, value):
		self._RjctdAmdmntNb = value if value is not None else base_types.UninitialisedField(self, 'RjctdAmdmntNb', Count1, False)

	@RjctdAmdmntNb.deleter
	def RjctdAmdmntNb(self):
		del self._RjctdAmdmntNb
		self._RjctdAmdmntNb = base_types.UninitialisedField(self, 'RjctdAmdmntNb', Count1, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason1Choice, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason1Choice, False)

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
		self._UsrTxRef = value if value is not None else base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, True)

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = base_types.UninitialisedField(self, 'UsrTxRef', DocumentIdentification5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DltaRptRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Initr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdAmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))