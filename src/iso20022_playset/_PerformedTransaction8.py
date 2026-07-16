# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import LoyaltyResult3
from . import Max35Text
from . import ResponseType11
from . import RetailerPaymentResult8
from . import TransactionIdentifier1

class PerformedTransaction8(base_types._BaseFieldType):

	__slots__ = ["_LltyRslt", "_POIRcncltnId", "_POITxId", "_PmtRslt", "_Rspn", "_RvsdAmt", "_SaleTxId"]
	@property
	def LltyRslt(self):
		return self._LltyRslt

	@LltyRslt.setter
	def LltyRslt(self, value):
		self._LltyRslt = value if value is not None else base_types.UninitialisedField(self, 'LltyRslt', LoyaltyResult3, True)

	@LltyRslt.deleter
	def LltyRslt(self):
		del self._LltyRslt
		self._LltyRslt = base_types.UninitialisedField(self, 'LltyRslt', LoyaltyResult3, True)

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

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
	def PmtRslt(self):
		return self._PmtRslt

	@PmtRslt.setter
	def PmtRslt(self, value):
		self._PmtRslt = value if value is not None else base_types.UninitialisedField(self, 'PmtRslt', RetailerPaymentResult8, False)

	@PmtRslt.deleter
	def PmtRslt(self):
		del self._PmtRslt
		self._PmtRslt = base_types.UninitialisedField(self, 'PmtRslt', RetailerPaymentResult8, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@property
	def RvsdAmt(self):
		return self._RvsdAmt

	@RvsdAmt.setter
	def RvsdAmt(self, value):
		self._RvsdAmt = value if value is not None else base_types.UninitialisedField(self, 'RvsdAmt', ImpliedCurrencyAndAmount, False)

	@RvsdAmt.deleter
	def RvsdAmt(self):
		del self._RvsdAmt
		self._RvsdAmt = base_types.UninitialisedField(self, 'RvsdAmt', ImpliedCurrencyAndAmount, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyRslt', type=LoyaltyResult3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRslt', type=RetailerPaymentResult8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))