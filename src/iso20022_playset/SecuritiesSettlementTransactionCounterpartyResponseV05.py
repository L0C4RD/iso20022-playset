import base_types
import SupplementaryData1
import ResponseStatus6Choice
import TransactionIdentification6
import TransactionDetails173

class SecuritiesSettlementTransactionCounterpartyResponseV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TxDtls", "_RspnSts", "_TxId"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if type(value) != auto else self.make_default("RspnSts")

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails173, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification6, min=1, max=1, mutex_group=None, array=False),
	))

