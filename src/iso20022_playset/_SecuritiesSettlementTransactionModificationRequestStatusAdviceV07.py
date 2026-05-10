from . import base_types
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SupplementaryData1 import SupplementaryData1
from ._PartyIdentification144 import PartyIdentification144
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._TransactionDetails171 import TransactionDetails171
from ._Max35Text import Max35Text
from ._ModificationProcessingStatus10Choice import ModificationProcessingStatus10Choice
from ._TransactionIdentifications33 import TransactionIdentifications33

class SecuritiesSettlementTransactionModificationRequestStatusAdviceV07(base_types._BaseFieldType):

	__slots__ = ["_TxDtls", "_SfkpgAcct", "_ModReqRef", "_ModPrcgSts", "_BlckChainAdrOrWllt", "_SplmtryData", "_TxId", "_AcctOwnr"]
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
	def ModPrcgSts(self):
		return self._ModPrcgSts

	@ModPrcgSts.setter
	def ModPrcgSts(self, value):
		self._ModPrcgSts = value if type(value) != base_types.auto else self.make_default("ModPrcgSts")

	@ModPrcgSts.deleter
	def ModPrcgSts(self):
		del self._ModPrcgSts
		self._ModPrcgSts = None

	@property
	def ModReqRef(self):
		return self._ModReqRef

	@ModReqRef.setter
	def ModReqRef(self, value):
		self._ModReqRef = value if type(value) != base_types.auto else self.make_default("ModReqRef")

	@ModReqRef.deleter
	def ModReqRef(self):
		del self._ModReqRef
		self._ModReqRef = None

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
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModPrcgSts', type=ModificationProcessingStatus10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModReqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails171, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications33, min=0, max=1, mutex_group=None, array=False),
	))

