from . import base_types
import PartyIdentification144
import BlockChainAddressWallet3
import DocumentIdentification54
import ProcessingStatus89Choice
import SupplementaryData1
import StatusOrStatement13Choice
import SecuritiesAccount19

class SecuritiesStatusOrStatementQueryStatusAdviceV07(base_types._BaseFieldType):

	__slots__ = ["_QryDtls", "_BlckChainAdrOrWllt", "_StsOrStmtReqd", "_AcctOwnr", "_PrcgSts", "_SfkpgAcct", "_SplmtryData"]
	@property
	def QryDtls(self):
		return self._QryDtls

	@QryDtls.setter
	def QryDtls(self, value):
		self._QryDtls = value if type(value) != auto else self.make_default("QryDtls")

	@QryDtls.deleter
	def QryDtls(self):
		del self._QryDtls
		self._QryDtls = None

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
	def StsOrStmtReqd(self):
		return self._StsOrStmtReqd

	@StsOrStmtReqd.setter
	def StsOrStmtReqd(self, value):
		self._StsOrStmtReqd = value if type(value) != auto else self.make_default("StsOrStmtReqd")

	@StsOrStmtReqd.deleter
	def StsOrStmtReqd(self):
		del self._StsOrStmtReqd
		self._StsOrStmtReqd = None

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

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryDtls', type=DocumentIdentification54, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrStmtReqd', type=StatusOrStatement13Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus89Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

