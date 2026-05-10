from . import base_types
from ._TotalValueInPageAndStatement3 import TotalValueInPageAndStatement3
from ._PartyIdentification157 import PartyIdentification157
from ._Intermediary45 import Intermediary45
from ._SubAccountIdentification69 import SubAccountIdentification69
from ._Pagination1 import Pagination1
from ._AggregateBalanceInformation44 import AggregateBalanceInformation44
from ._PartyIdentification156 import PartyIdentification156
from ._BlockChainAddressWallet10 import BlockChainAddressWallet10
from ._SecuritiesAccount42 import SecuritiesAccount42
from ._Statement77 import Statement77

class SecuritiesBalanceCustodyReport002V11(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_IntrmyInf", "_AcctOwnr", "_StmtGnlDtls", "_SfkpgAcct", "_Pgntn", "_AcctBaseCcyTtlAmts", "_SubAcctDtls", "_BalForAcct", "_AcctSvcr"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def IntrmyInf(self):
		return self._IntrmyInf

	@IntrmyInf.setter
	def IntrmyInf(self, value):
		self._IntrmyInf = value if type(value) != base_types.auto else self.make_default("IntrmyInf")

	@IntrmyInf.deleter
	def IntrmyInf(self):
		del self._IntrmyInf
		self._IntrmyInf = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

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
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def AcctBaseCcyTtlAmts(self):
		return self._AcctBaseCcyTtlAmts

	@AcctBaseCcyTtlAmts.setter
	def AcctBaseCcyTtlAmts(self, value):
		self._AcctBaseCcyTtlAmts = value if type(value) != base_types.auto else self.make_default("AcctBaseCcyTtlAmts")

	@AcctBaseCcyTtlAmts.deleter
	def AcctBaseCcyTtlAmts(self):
		del self._AcctBaseCcyTtlAmts
		self._AcctBaseCcyTtlAmts = None

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
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary45, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement77, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification69, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
	))

