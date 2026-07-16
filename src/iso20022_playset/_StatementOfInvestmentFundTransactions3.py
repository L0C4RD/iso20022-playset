# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extension1
from . import InvestmentAccount43
from . import InvestmentFundTransactionsByFund3
from . import Statement8
from . import SubAccountIdentification36

class StatementOfInvestmentFundTransactions3(base_types._BaseFieldType):

	__slots__ = ["_InvstmtAcctDtls", "_StmtGnlDtls", "_SubAcctDtls", "_TxOnAcct", "_Xtnsn"]
	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount43, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount43, False)

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement8, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement8, False)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification36, True)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccountIdentification36, True)

	@property
	def TxOnAcct(self):
		return self._TxOnAcct

	@TxOnAcct.setter
	def TxOnAcct(self, value):
		self._TxOnAcct = value if value is not None else base_types.UninitialisedField(self, 'TxOnAcct', InvestmentFundTransactionsByFund3, True)

	@TxOnAcct.deleter
	def TxOnAcct(self):
		del self._TxOnAcct
		self._TxOnAcct = base_types.UninitialisedField(self, 'TxOnAcct', InvestmentFundTransactionsByFund3, True)

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
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxOnAcct', type=InvestmentFundTransactionsByFund3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))