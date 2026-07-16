# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AggregateBalanceInformation3
from . import Extension1
from . import SafekeepingAccount2
from . import Statement6
from . import SubAccountIdentification3
from . import TotalValueInPageAndStatement

class AccountingStatementOfHoldings2(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_BalForAcct", "_StmtGnlDtls", "_SubAcctDtls", "_TtlVals", "_Xtnsn"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SafekeepingAccount2, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SafekeepingAccount2, False)

	@property
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if value is not None else base_types.UninitialisedField(self, 'BalForAcct', AggregateBalanceInformation3, True)

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = base_types.UninitialisedField(self, 'BalForAcct', AggregateBalanceInformation3, True)

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement6, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement6, False)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification3, True)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification3, True)

	@property
	def TtlVals(self):
		return self._TtlVals

	@TtlVals.setter
	def TtlVals(self, value):
		self._TtlVals = value if value is not None else base_types.UninitialisedField(self, 'TtlVals', TotalValueInPageAndStatement, False)

	@TtlVals.deleter
	def TtlVals(self):
		del self._TtlVals
		self._TtlVals = base_types.UninitialisedField(self, 'TtlVals', TotalValueInPageAndStatement, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlVals', type=TotalValueInPageAndStatement, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))