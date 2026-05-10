from . import base_types
from .InvestmentFundTransactionsByFund3 import InvestmentFundTransactionsByFund3
from .InvestmentAccount43 import InvestmentAccount43
from .SubAccountIdentification36 import SubAccountIdentification36
from .Extension1 import Extension1
from .Statement8 import Statement8

class StatementOfInvestmentFundTransactions3(base_types._BaseFieldType):

	__slots__ = ["_SubAcctDtls", "_Xtnsn", "_InvstmtAcctDtls", "_TxOnAcct", "_StmtGnlDtls"]
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
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def TxOnAcct(self):
		return self._TxOnAcct

	@TxOnAcct.setter
	def TxOnAcct(self, value):
		self._TxOnAcct = value if type(value) != base_types.auto else self.make_default("TxOnAcct")

	@TxOnAcct.deleter
	def TxOnAcct(self):
		del self._TxOnAcct
		self._TxOnAcct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOnAcct', type=InvestmentFundTransactionsByFund3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement8, min=0, max=1, mutex_group=None, array=False),
	))

