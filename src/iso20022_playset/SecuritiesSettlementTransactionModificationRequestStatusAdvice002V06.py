import base_types
import SecuritiesAccount30
import SupplementaryData1
import PartyIdentification156
import TransactionDetails158
import ModificationProcessingStatus11Choice
import TransactionIdentifications37
import BlockChainAddressWallet7
import RestrictedFINXMax16Text

class SecuritiesSettlementTransactionModificationRequestStatusAdvice002V06(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_ModReqRef", "_BlckChainAdrOrWllt", "_TxDtls", "_ModPrcgSts", "_AcctOwnr", "_SfkpgAcct", "_SplmtryData"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def ModReqRef(self):
		return self._ModReqRef

	@ModReqRef.setter
	def ModReqRef(self, value):
		self._ModReqRef = value if type(value) != auto else self.make_default("ModReqRef")

	@ModReqRef.deleter
	def ModReqRef(self):
		del self._ModReqRef
		self._ModReqRef = None

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
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def ModPrcgSts(self):
		return self._ModPrcgSts

	@ModPrcgSts.setter
	def ModPrcgSts(self, value):
		self._ModPrcgSts = value if type(value) != auto else self.make_default("ModPrcgSts")

	@ModPrcgSts.deleter
	def ModPrcgSts(self):
		del self._ModPrcgSts
		self._ModPrcgSts = None

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
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModReqRef', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails158, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModPrcgSts', type=ModificationProcessingStatus11Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

