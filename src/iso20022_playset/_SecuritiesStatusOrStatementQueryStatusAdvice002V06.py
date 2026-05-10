from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .StatusOrStatement12Choice import StatusOrStatement12Choice
from .ProcessingStatus95Choice import ProcessingStatus95Choice
from .DocumentIdentification55 import DocumentIdentification55
from .BlockChainAddressWallet7 import BlockChainAddressWallet7
from .PartyIdentification156 import PartyIdentification156
from .SecuritiesAccount30 import SecuritiesAccount30

class SecuritiesStatusOrStatementQueryStatusAdvice002V06(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_AcctOwnr", "_StsOrStmtReqd", "_SfkpgAcct", "_BlckChainAdrOrWllt", "_QryDtls", "_PrcgSts"]
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
	def StsOrStmtReqd(self):
		return self._StsOrStmtReqd

	@StsOrStmtReqd.setter
	def StsOrStmtReqd(self, value):
		self._StsOrStmtReqd = value if type(value) != base_types.auto else self.make_default("StsOrStmtReqd")

	@StsOrStmtReqd.deleter
	def StsOrStmtReqd(self):
		del self._StsOrStmtReqd
		self._StsOrStmtReqd = None

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
	def QryDtls(self):
		return self._QryDtls

	@QryDtls.setter
	def QryDtls(self, value):
		self._QryDtls = value if type(value) != base_types.auto else self.make_default("QryDtls")

	@QryDtls.deleter
	def QryDtls(self):
		del self._QryDtls
		self._QryDtls = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrStmtReqd', type=StatusOrStatement12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryDtls', type=DocumentIdentification55, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus95Choice, min=1, max=1, mutex_group=None, array=False),
	))

