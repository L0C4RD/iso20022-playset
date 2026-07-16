# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyAccount3
from . import PaymentAccount3
from . import PaymentReceipt6
from . import StoredValueAccount2
from . import TransactionIdentifier1

class BalanceInquiryResponse6(base_types._BaseFieldType):

	__slots__ = ["_LltyAcct", "_POITxId", "_PmtAcct", "_Rct", "_SaleTxId", "_StordValAcct"]
	@property
	def LltyAcct(self):
		return self._LltyAcct

	@LltyAcct.setter
	def LltyAcct(self, value):
		self._LltyAcct = value if value is not None else base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, False)

	@LltyAcct.deleter
	def LltyAcct(self):
		del self._LltyAcct
		self._LltyAcct = base_types.UninitialisedField(self, 'LltyAcct', LoyaltyAccount3, False)

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if value is not None else base_types.UninitialisedField(self, 'POITxId', TransactionIdentifier1, False)

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = base_types.UninitialisedField(self, 'POITxId', TransactionIdentifier1, False)

	@property
	def PmtAcct(self):
		return self._PmtAcct

	@PmtAcct.setter
	def PmtAcct(self, value):
		self._PmtAcct = value if value is not None else base_types.UninitialisedField(self, 'PmtAcct', PaymentAccount3, False)

	@PmtAcct.deleter
	def PmtAcct(self):
		del self._PmtAcct
		self._PmtAcct = base_types.UninitialisedField(self, 'PmtAcct', PaymentAccount3, False)

	@property
	def Rct(self):
		return self._Rct

	@Rct.setter
	def Rct(self, value):
		self._Rct = value if value is not None else base_types.UninitialisedField(self, 'Rct', PaymentReceipt6, True)

	@Rct.deleter
	def Rct(self):
		del self._Rct
		self._Rct = base_types.UninitialisedField(self, 'Rct', PaymentReceipt6, True)

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if value is not None else base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@property
	def StordValAcct(self):
		return self._StordValAcct

	@StordValAcct.setter
	def StordValAcct(self, value):
		self._StordValAcct = value if value is not None else base_types.UninitialisedField(self, 'StordValAcct', StoredValueAccount2, True)

	@StordValAcct.deleter
	def StordValAcct(self):
		del self._StordValAcct
		self._StordValAcct = base_types.UninitialisedField(self, 'StordValAcct', StoredValueAccount2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyAcct', type=LoyaltyAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcct', type=PaymentAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rct', type=PaymentReceipt6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcct', type=StoredValueAccount2, min=0, max=None, mutex_group=None, array=True),
	))