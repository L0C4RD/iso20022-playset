from . import base_types
from ._SecuritiesAccount26 import SecuritiesAccount26
from ._Intermediary44 import Intermediary44
from ._TotalValueInPageAndStatement1 import TotalValueInPageAndStatement1
from ._BlockChainAddressWallet1 import BlockChainAddressWallet1
from ._Statement73 import Statement73
from ._PartyIdentification136 import PartyIdentification136
from ._AggregateBalanceInformation46 import AggregateBalanceInformation46
from ._Pagination1 import Pagination1
from ._SubAccountIdentification71 import SubAccountIdentification71
from ._PartyIdentification144 import PartyIdentification144

class SecuritiesBalanceCustodyReportV12(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_AcctBaseCcyTtlAmts", "_SfkpgAcct", "_SubAcctDtls", "_AcctOwnr", "_StmtGnlDtls", "_AcctSvcr", "_Pgntn", "_IntrmyInf", "_BalForAcct"]
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
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

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
	def BalForAcct(self):
		return self._BalForAcct

	@BalForAcct.setter
	def BalForAcct(self, value):
		self._BalForAcct = value if type(value) != base_types.auto else self.make_default("BalForAcct")

	@BalForAcct.deleter
	def BalForAcct(self):
		del self._BalForAcct
		self._BalForAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccountIdentification71, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement73, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInf', type=Intermediary44, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalForAcct', type=AggregateBalanceInformation46, min=0, max=None, mutex_group=None, array=True),
	))

