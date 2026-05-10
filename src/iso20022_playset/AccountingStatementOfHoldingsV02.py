from . import base_types
from .SafekeepingAccount2 import SafekeepingAccount2
from .MessageIdentification1 import MessageIdentification1
from .SubAccountIdentification3 import SubAccountIdentification3
from .Pagination import Pagination
from .AggregateBalanceInformation3 import AggregateBalanceInformation3
from .TotalValueInPageAndStatement import TotalValueInPageAndStatement
from .AdditionalReference2 import AdditionalReference2
from .Statement6 import Statement6
from .Extension1 import Extension1

class AccountingStatementOfHoldingsV02(base_types._BaseFieldType):

	__slots__ = ["_MsgPgntn", "_RltdRef", "_StmtGnlDtls", "_AcctDtls", "_Xtnsn", "_MsgId", "_PrvsRef", "_BalForAcct", "_SubAcctDtls", "_TtlVals"]
	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != base_types.auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != base_types.auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if type(value) != base_types.auto else self.make_default("BalForAcct")

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = None

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if type(value) != base_types.auto else self.make_default("SubAcctDtls")

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = None

	@property
	def TtlVals(self):
		return self._TtlVals

	@TtlVals.setter
	def TtlVals(self, value):
		self._TtlVals = value if type(value) != base_types.auto else self.make_default("TtlVals")

	@TtlVals.deleter
	def TtlVals(self):
		del self._TtlVals
		self._TtlVals = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlVals', type=TotalValueInPageAndStatement, min=0, max=1, mutex_group=None, array=False),
	))

