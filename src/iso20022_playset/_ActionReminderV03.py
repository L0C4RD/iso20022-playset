# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import MessageIdentification1
from . import PendingActivity2
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class ActionReminderV03(base_types._BaseFieldType):

	__slots__ = ["_EstblishdBaselnId", "_MsgReqrngActn", "_PdgReqForActn", "_RmndrId", "_TxId", "_TxSts", "_UsrTxRef"]
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
	def MsgReqrngActn(self):
		return self._MsgReqrngActn

	@MsgReqrngActn.setter
	def MsgReqrngActn(self, value):
		self._MsgReqrngActn = value if value is not None else base_types.UninitialisedField(self, 'MsgReqrngActn', MessageIdentification1, False)

	@MsgReqrngActn.deleter
	def MsgReqrngActn(self):
		del self._MsgReqrngActn
		self._MsgReqrngActn = base_types.UninitialisedField(self, 'MsgReqrngActn', MessageIdentification1, False)

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if value is not None else base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, False)

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, False)

	@property
	def RmndrId(self):
		return self._RmndrId

	@RmndrId.setter
	def RmndrId(self, value):
		self._RmndrId = value if value is not None else base_types.UninitialisedField(self, 'RmndrId', MessageIdentification1, False)

	@RmndrId.deleter
	def RmndrId(self):
		del self._RmndrId
		self._RmndrId = base_types.UninitialisedField(self, 'RmndrId', MessageIdentification1, False)

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
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgReqrngActn', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmndrId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))