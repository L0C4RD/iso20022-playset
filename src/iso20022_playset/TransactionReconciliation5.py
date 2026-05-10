import base_types
import Max35Text
import TransactionTotals12
import Max70Text
import TransactionIdentifier1
import TrueFalseIndicator

class TransactionReconciliation5(base_types._BaseFieldType):

	__slots__ = ["_ClsPrd", "_RcncltnTxId", "_TxTtls", "_AddtlTxData", "_RcncltnId"]
	@property
	def ClsPrd(self):
		return self._ClsPrd

	@ClsPrd.setter
	def ClsPrd(self, value):
		self._ClsPrd = value if type(value) != auto else self.make_default("ClsPrd")

	@ClsPrd.deleter
	def ClsPrd(self):
		del self._ClsPrd
		self._ClsPrd = None

	@property
	def RcncltnTxId(self):
		return self._RcncltnTxId

	@RcncltnTxId.setter
	def RcncltnTxId(self, value):
		self._RcncltnTxId = value if type(value) != auto else self.make_default("RcncltnTxId")

	@RcncltnTxId.deleter
	def RcncltnTxId(self):
		del self._RcncltnTxId
		self._RcncltnTxId = None

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	@property
	def AddtlTxData(self):
		return self._AddtlTxData

	@AddtlTxData.setter
	def AddtlTxData(self, value):
		self._AddtlTxData = value if type(value) != auto else self.make_default("AddtlTxData")

	@AddtlTxData.deleter
	def AddtlTxData(self):
		del self._AddtlTxData
		self._AddtlTxData = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsPrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnTxId', type=TransactionIdentifier1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

