import base_types
import Statement83
import DocumentNumber13
import AdditionalQueryParameters13
import PartyIdentification144
import BlockChainAddressWallet3
import SupplementaryData1
import SecuritiesAccount19

class SecuritiesStatementQueryV08(base_types._BaseFieldType):

	__slots__ = ["_StmtReqd", "_SplmtryData", "_BlckChainAdrOrWllt", "_AddtlQryParams", "_StmtGnlDtls", "_SfkpgAcct", "_AcctOwnr"]
	@property
	def StmtReqd(self):
		return self._StmtReqd

	@StmtReqd.setter
	def StmtReqd(self, value):
		self._StmtReqd = value if type(value) != auto else self.make_default("StmtReqd")

	@StmtReqd.deleter
	def StmtReqd(self):
		del self._StmtReqd
		self._StmtReqd = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def AddtlQryParams(self):
		return self._AddtlQryParams

	@AddtlQryParams.setter
	def AddtlQryParams(self, value):
		self._AddtlQryParams = value if type(value) != auto else self.make_default("AddtlQryParams")

	@AddtlQryParams.deleter
	def AddtlQryParams(self):
		del self._AddtlQryParams
		self._AddtlQryParams = None

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtReqd', type=DocumentNumber13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlQryParams', type=AdditionalQueryParameters13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement83, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
	))

