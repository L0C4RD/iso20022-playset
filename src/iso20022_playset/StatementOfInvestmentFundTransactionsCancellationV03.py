import base_types
import StatementOfInvestmentFundTransactions3
import MessageIdentification1
import AdditionalReference2
import Pagination

class StatementOfInvestmentFundTransactionsCancellationV03(base_types._BaseFieldType):

	__slots__ = ["_RltdRef", "_MsgId", "_StmtToBeCanc", "_MsgPgntn", "_PrvsRef"]
	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def StmtToBeCanc(self):
		return self._StmtToBeCanc

	@StmtToBeCanc.setter
	def StmtToBeCanc(self, value):
		self._StmtToBeCanc = value if type(value) != auto else self.make_default("StmtToBeCanc")

	@StmtToBeCanc.deleter
	def StmtToBeCanc(self):
		del self._StmtToBeCanc
		self._StmtToBeCanc = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtToBeCanc', type=StatementOfInvestmentFundTransactions3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference2, min=0, max=1, mutex_group=None, array=False),
	))

