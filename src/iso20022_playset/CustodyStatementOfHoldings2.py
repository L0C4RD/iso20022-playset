from . import base_types
from .SubAccountIdentification5 import SubAccountIdentification5
from .SafekeepingAccount2 import SafekeepingAccount2
from .Statement7 import Statement7
from .AggregateBalanceInformation4 import AggregateBalanceInformation4
from .TotalValueInPageAndStatement import TotalValueInPageAndStatement
from .Extension1 import Extension1

class CustodyStatementOfHoldings2(base_types._BaseFieldType):

	__slots__ = ["_StmtGnlDtls", "_Xtnsn", "_SubAcctDtls", "_BalForAcct", "_AcctDtls", "_TtlVals"]
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
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVals', type=TotalValueInPageAndStatement, min=0, max=1, mutex_group=None, array=False),
	))

