# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import DocumentIdentification3
from . import DocumentIdentification4
from . import DocumentIdentification5
from . import Limit1
from . import MessageIdentification1
from . import MisMatchReport3
from . import PartyIdentification26
from . import PendingActivity2
from . import SimpleIdentificationInformation
from . import TransactionStatus4

class BaselineMatchReportV03(base_types._BaseFieldType):

	__slots__ = ["_BaselnEstblishmtTrils", "_Buyr", "_BuyrBk", "_CmpardDocRef", "_EstblishdBaselnId", "_ReqForActn", "_Rpt", "_RptId", "_Sellr", "_SellrBk", "_TxId", "_TxSts", "_UsrTxRef"]
	@property
	def BaselnEstblishmtTrils(self):
		return self._BaselnEstblishmtTrils

	@BaselnEstblishmtTrils.setter
	def BaselnEstblishmtTrils(self, value):
		self._BaselnEstblishmtTrils = value if value is not None else base_types.UninitialisedField(self, 'BaselnEstblishmtTrils', Limit1, False)

	@BaselnEstblishmtTrils.deleter
	def BaselnEstblishmtTrils(self):
		del self._BaselnEstblishmtTrils
		self._BaselnEstblishmtTrils = base_types.UninitialisedField(self, 'BaselnEstblishmtTrils', Limit1, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentification26, False)

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
	def CmpardDocRef(self):
		return self._CmpardDocRef

	@CmpardDocRef.setter
	def CmpardDocRef(self, value):
		self._CmpardDocRef = value if value is not None else base_types.UninitialisedField(self, 'CmpardDocRef', DocumentIdentification4, False)

	@CmpardDocRef.deleter
	def CmpardDocRef(self):
		del self._CmpardDocRef
		self._CmpardDocRef = base_types.UninitialisedField(self, 'CmpardDocRef', DocumentIdentification4, False)

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
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if value is not None else base_types.UninitialisedField(self, 'Rpt', MisMatchReport3, False)

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = base_types.UninitialisedField(self, 'Rpt', MisMatchReport3, False)

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
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PartyIdentification26, False)

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
		base_types.FieldEntry(name='BaselnEstblishmtTrils', type=Limit1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpardDocRef', type=DocumentIdentification4, min=2, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=MisMatchReport3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))