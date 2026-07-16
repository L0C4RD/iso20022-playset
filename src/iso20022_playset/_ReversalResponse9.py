# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max140Text
from . import Max35Text
from . import PaymentReceipt6
from . import RetailerReversalResult7
from . import TransactionIdentifier1

class ReversalResponse9(base_types._BaseFieldType):

	__slots__ = ["_IssrRefData", "_POIRcncltnId", "_POITxId", "_Rct", "_RvsdAmt", "_RvslTxRslt", "_SaleRefId", "_SaleTxId"]
	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if value is not None else base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = base_types.UninitialisedField(self, 'IssrRefData', Max140Text, False)

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
	def RvslTxRslt(self):
		return self._RvslTxRslt

	@RvslTxRslt.setter
	def RvslTxRslt(self, value):
		self._RvslTxRslt = value if value is not None else base_types.UninitialisedField(self, 'RvslTxRslt', RetailerReversalResult7, False)

	@RvslTxRslt.deleter
	def RvslTxRslt(self):
		del self._RvslTxRslt
		self._RvslTxRslt = base_types.UninitialisedField(self, 'RvslTxRslt', RetailerReversalResult7, False)

	@property
	def SaleRefId(self):
		return self._SaleRefId

	@SaleRefId.setter
	def SaleRefId(self, value):
		self._SaleRefId = value if value is not None else base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

	@SaleRefId.deleter
	def SaleRefId(self):
		del self._SaleRefId
		self._SaleRefId = base_types.UninitialisedField(self, 'SaleRefId', Max35Text, False)

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
		base_types.FieldEntry(name='IssrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rct', type=PaymentReceipt6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslTxRslt', type=RetailerReversalResult7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
	))