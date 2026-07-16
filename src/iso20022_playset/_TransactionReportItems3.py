# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import CountryCode
from . import CurrencyAndAmount
from . import DocumentIdentification3
from . import DocumentIdentification5
from . import DocumentIdentification7
from . import Max35Text
from . import PartyIdentification26
from . import PendingActivity2
from . import TransactionStatus4

class TransactionReportItems3(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_BuyrBk", "_BuyrBkCtry", "_EstblishdBaselnId", "_OblgrBk", "_OutsdngAmt", "_PdgReqForActn", "_PurchsOrdrRef", "_Sellr", "_SellrBk", "_SellrBkCtry", "_SubmitgBk", "_TtlNetAmt", "_TxId", "_TxSts", "_UsrTxRef"]
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
	def BuyrBkCtry(self):
		return self._BuyrBkCtry

	@BuyrBkCtry.setter
	def BuyrBkCtry(self, value):
		self._BuyrBkCtry = value if value is not None else base_types.UninitialisedField(self, 'BuyrBkCtry', CountryCode, False)

	@BuyrBkCtry.deleter
	def BuyrBkCtry(self):
		del self._BuyrBkCtry
		self._BuyrBkCtry = base_types.UninitialisedField(self, 'BuyrBkCtry', CountryCode, False)

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
	def OblgrBk(self):
		return self._OblgrBk

	@OblgrBk.setter
	def OblgrBk(self, value):
		self._OblgrBk = value if value is not None else base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, True)

	@OblgrBk.deleter
	def OblgrBk(self):
		del self._OblgrBk
		self._OblgrBk = base_types.UninitialisedField(self, 'OblgrBk', BICIdentification1, True)

	@property
	def OutsdngAmt(self):
		return self._OutsdngAmt

	@OutsdngAmt.setter
	def OutsdngAmt(self, value):
		self._OutsdngAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngAmt', CurrencyAndAmount, False)

	@OutsdngAmt.deleter
	def OutsdngAmt(self):
		del self._OutsdngAmt
		self._OutsdngAmt = base_types.UninitialisedField(self, 'OutsdngAmt', CurrencyAndAmount, False)

	@property
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if value is not None else base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, True)

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = base_types.UninitialisedField(self, 'PdgReqForActn', PendingActivity2, True)

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

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
	def SellrBkCtry(self):
		return self._SellrBkCtry

	@SellrBkCtry.setter
	def SellrBkCtry(self, value):
		self._SellrBkCtry = value if value is not None else base_types.UninitialisedField(self, 'SellrBkCtry', CountryCode, False)

	@SellrBkCtry.deleter
	def SellrBkCtry(self):
		del self._SellrBkCtry
		self._SellrBkCtry = base_types.UninitialisedField(self, 'SellrBkCtry', CountryCode, False)

	@property
	def SubmitgBk(self):
		return self._SubmitgBk

	@SubmitgBk.setter
	def SubmitgBk(self, value):
		self._SubmitgBk = value if value is not None else base_types.UninitialisedField(self, 'SubmitgBk', BICIdentification1, True)

	@SubmitgBk.deleter
	def SubmitgBk(self):
		del self._SubmitgBk
		self._SubmitgBk = base_types.UninitialisedField(self, 'SubmitgBk', BICIdentification1, True)

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

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
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBkCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OutsdngAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBkCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgBk', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
	))