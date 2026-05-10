from . import base_types
from ._AdditionalQueryParameters14 import AdditionalQueryParameters14
from ._BlockChainAddressWallet7 import BlockChainAddressWallet7
from ._DocumentNumber14 import DocumentNumber14
from ._PartyIdentification156 import PartyIdentification156
from ._SecuritiesAccount30 import SecuritiesAccount30
from ._Statement84 import Statement84
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesStatementQuery002V08(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AddtlQryParams", "_BlckChainAdrOrWllt", "_SfkpgAcct", "_SplmtryData", "_StmtGnlDtls", "_StmtReqd"]
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
	def AddtlQryParams(self):
		return self._AddtlQryParams

	@AddtlQryParams.setter
	def AddtlQryParams(self, value):
		self._AddtlQryParams = value if type(value) != base_types.auto else self.make_default("AddtlQryParams")

	@AddtlQryParams.deleter
	def AddtlQryParams(self):
		del self._AddtlQryParams
		self._AddtlQryParams = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

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
	def StmtReqd(self):
		return self._StmtReqd

	@StmtReqd.setter
	def StmtReqd(self, value):
		self._StmtReqd = value if type(value) != base_types.auto else self.make_default("StmtReqd")

	@StmtReqd.deleter
	def StmtReqd(self):
		del self._StmtReqd
		self._StmtReqd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQryParams', type=AdditionalQueryParameters14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement84, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtReqd', type=DocumentNumber14, min=1, max=1, mutex_group=None, array=False),
	))

