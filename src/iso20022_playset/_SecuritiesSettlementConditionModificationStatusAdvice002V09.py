from . import base_types
from ._BlockChainAddressWallet7 import BlockChainAddressWallet7
from ._PartyIdentification156 import PartyIdentification156
from ._ProcessingStatus91Choice import ProcessingStatus91Choice
from ._RequestDetails29 import RequestDetails29
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text
from ._SecuritiesAccount30 import SecuritiesAccount30
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesSettlementConditionModificationStatusAdvice002V09(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_BlckChainAdrOrWllt", "_PrcgSts", "_ReqDtls", "_ReqRef", "_SfkpgAcct", "_SplmtryData"]
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
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def ReqDtls(self):
		return self._ReqDtls

	@ReqDtls.setter
	def ReqDtls(self, value):
		self._ReqDtls = value if type(value) != base_types.auto else self.make_default("ReqDtls")

	@ReqDtls.deleter
	def ReqDtls(self):
		del self._ReqDtls
		self._ReqDtls = None

	@property
	def ReqRef(self):
		return self._ReqRef

	@ReqRef.setter
	def ReqRef(self, value):
		self._ReqRef = value if type(value) != base_types.auto else self.make_default("ReqRef")

	@ReqRef.deleter
	def ReqRef(self):
		del self._ReqRef
		self._ReqRef = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus91Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqDtls', type=RequestDetails29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRef', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

