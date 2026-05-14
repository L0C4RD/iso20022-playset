# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AggregateBalanceInformation3 import AggregateBalanceInformation3
from ._Extension1 import Extension1
from ._SafekeepingAccount2 import SafekeepingAccount2
from ._Statement6 import Statement6
from ._SubAccountIdentification3 import SubAccountIdentification3
from ._TotalValueInPageAndStatement import TotalValueInPageAndStatement

class AccountingStatementOfHoldings2(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_BalForAcct", "_StmtGnlDtls", "_SubAcctDtls", "_TtlVals", "_Xtnsn"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlVals', type=TotalValueInPageAndStatement, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))