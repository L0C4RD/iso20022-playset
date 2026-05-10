from . import base_types
import Max10000Binary
import ContentInformationType10
import TransactionIdentifier3
import DetailedAmount12
import CardAccount20
import AmountAndCurrency1

class ATMTransaction42(base_types._BaseFieldType):

	__slots__ = ["_TtlReqdAmt", "_TxId", "_PrtctdAcctData", "_ICCRltdData", "_DtldReqdAmt", "_AcctData"]
	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if type(value) != auto else self.make_default("TtlReqdAmt")

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = None

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

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlReqdAmt', type=AmountAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctData', type=CardAccount20, min=0, max=1, mutex_group=None, array=False),
	))

