# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Baseline5
from . import ContactIdentification1
from . import ContactIdentification3
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import MessageIdentification1
from . import PendingActivity2
from . import ReportType1
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class FullPushThroughReportV05(base_types._BaseFieldType):

	__slots__ = ["_BuyrBkCtctPrsn", "_BuyrCtctPrsn", "_EstblishdBaselnId", "_OthrBkCtctPrsn", "_PushdThrghBaseln", "_ReqForActn", "_RptId", "_RptPurp", "_SellrBkCtctPrsn", "_SellrCtctPrsn", "_TxId", "_TxSts", "_UsrTxRef"]
	@property
	def BuyrBkCtctPrsn(self):
		return self._BuyrBkCtctPrsn

	@BuyrBkCtctPrsn.setter
	def BuyrBkCtctPrsn(self, value):
		self._BuyrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'BuyrBkCtctPrsn', ContactIdentification1, True)

	@BuyrBkCtctPrsn.deleter
	def BuyrBkCtctPrsn(self):
		del self._BuyrBkCtctPrsn
		self._BuyrBkCtctPrsn = base_types.UninitialisedField(self, 'BuyrBkCtctPrsn', ContactIdentification1, True)

	@property
	def BuyrCtctPrsn(self):
		return self._BuyrCtctPrsn

	@BuyrCtctPrsn.setter
	def BuyrCtctPrsn(self, value):
		self._BuyrCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'BuyrCtctPrsn', ContactIdentification1, True)

	@BuyrCtctPrsn.deleter
	def BuyrCtctPrsn(self):
		del self._BuyrCtctPrsn
		self._BuyrCtctPrsn = base_types.UninitialisedField(self, 'BuyrCtctPrsn', ContactIdentification1, True)

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
	def OthrBkCtctPrsn(self):
		return self._OthrBkCtctPrsn

	@OthrBkCtctPrsn.setter
	def OthrBkCtctPrsn(self, value):
		self._OthrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'OthrBkCtctPrsn', ContactIdentification3, True)

	@OthrBkCtctPrsn.deleter
	def OthrBkCtctPrsn(self):
		del self._OthrBkCtctPrsn
		self._OthrBkCtctPrsn = base_types.UninitialisedField(self, 'OthrBkCtctPrsn', ContactIdentification3, True)

	@property
	def PushdThrghBaseln(self):
		return self._PushdThrghBaseln

	@PushdThrghBaseln.setter
	def PushdThrghBaseln(self, value):
		self._PushdThrghBaseln = value if value is not None else base_types.UninitialisedField(self, 'PushdThrghBaseln', Baseline5, False)

	@PushdThrghBaseln.deleter
	def PushdThrghBaseln(self):
		del self._PushdThrghBaseln
		self._PushdThrghBaseln = base_types.UninitialisedField(self, 'PushdThrghBaseln', Baseline5, False)

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
	def RptPurp(self):
		return self._RptPurp

	@RptPurp.setter
	def RptPurp(self, value):
		self._RptPurp = value if value is not None else base_types.UninitialisedField(self, 'RptPurp', ReportType1, False)

	@RptPurp.deleter
	def RptPurp(self):
		del self._RptPurp
		self._RptPurp = base_types.UninitialisedField(self, 'RptPurp', ReportType1, False)

	@property
	def SellrBkCtctPrsn(self):
		return self._SellrBkCtctPrsn

	@SellrBkCtctPrsn.setter
	def SellrBkCtctPrsn(self, value):
		self._SellrBkCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'SellrBkCtctPrsn', ContactIdentification1, True)

	@SellrBkCtctPrsn.deleter
	def SellrBkCtctPrsn(self):
		del self._SellrBkCtctPrsn
		self._SellrBkCtctPrsn = base_types.UninitialisedField(self, 'SellrBkCtctPrsn', ContactIdentification1, True)

	@property
	def SellrCtctPrsn(self):
		return self._SellrCtctPrsn

	@SellrCtctPrsn.setter
	def SellrCtctPrsn(self, value):
		self._SellrCtctPrsn = value if value is not None else base_types.UninitialisedField(self, 'SellrCtctPrsn', ContactIdentification1, True)

	@SellrCtctPrsn.deleter
	def SellrCtctPrsn(self):
		del self._SellrCtctPrsn
		self._SellrCtctPrsn = base_types.UninitialisedField(self, 'SellrCtctPrsn', ContactIdentification1, True)

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
		base_types.FieldEntry(name='BuyrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PushdThrghBaseln', type=Baseline5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPurp', type=ReportType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))