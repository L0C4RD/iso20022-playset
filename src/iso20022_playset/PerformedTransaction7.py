import base_types
import ImpliedCurrencyAndAmount
import LoyaltyResult3
import TransactionIdentifier1
import Max35Text
import RetailerPaymentResult7
import ResponseType11

class PerformedTransaction7(base_types._BaseFieldType):

	__slots__ = ["_Rspn", "_LltyRslt", "_RvsdAmt", "_SaleTxId", "_POIRcncltnId", "_POITxId", "_PmtRslt"]
	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def LltyRslt(self):
		return self._LltyRslt

	@LltyRslt.setter
	def LltyRslt(self, value):
		self._LltyRslt = value if type(value) != auto else self.make_default("LltyRslt")

	@LltyRslt.deleter
	def LltyRslt(self):
		del self._LltyRslt
		self._LltyRslt = None

	@property
	def RvsdAmt(self):
		return self._RvsdAmt

	@RvsdAmt.setter
	def RvsdAmt(self, value):
		self._RvsdAmt = value if type(value) != auto else self.make_default("RvsdAmt")

	@RvsdAmt.deleter
	def RvsdAmt(self):
		del self._RvsdAmt
		self._RvsdAmt = None

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def POITxId(self):
		return self._POITxId

	@POITxId.setter
	def POITxId(self, value):
		self._POITxId = value if type(value) != auto else self.make_default("POITxId")

	@POITxId.deleter
	def POITxId(self):
		del self._POITxId
		self._POITxId = None

	@property
	def PmtRslt(self):
		return self._PmtRslt

	@PmtRslt.setter
	def PmtRslt(self, value):
		self._PmtRslt = value if type(value) != auto else self.make_default("PmtRslt")

	@PmtRslt.deleter
	def PmtRslt(self):
		del self._PmtRslt
		self._PmtRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyRslt', type=LoyaltyResult3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POITxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRslt', type=RetailerPaymentResult7, min=0, max=1, mutex_group=None, array=False),
	))

