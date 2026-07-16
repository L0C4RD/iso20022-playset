# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import IntentToPay2
from . import MessageIdentification1
from . import PendingActivity2
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class ForwardIntentToPayNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_BuyrBk", "_EstblishdBaselnId", "_InttToPay", "_NtfctnId", "_ReqForActn", "_SellrBk", "_TxId", "_TxSts", "_UsrTxRef"]
	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if value is not None else base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

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
	def InttToPay(self):
		return self._InttToPay

	@InttToPay.setter
	def InttToPay(self, value):
		self._InttToPay = value if value is not None else base_types.UninitialisedField(self, 'InttToPay', IntentToPay2, False)

	@InttToPay.deleter
	def InttToPay(self):
		del self._InttToPay
		self._InttToPay = base_types.UninitialisedField(self, 'InttToPay', IntentToPay2, False)

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
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if value is not None else base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

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
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InttToPay', type=IntentToPay2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))