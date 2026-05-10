from . import base_types
from .AlternatePartyIdentification7 import AlternatePartyIdentification7
from .SecuritiesAccount19 import SecuritiesAccount19
from .BlockChainAddressWallet3 import BlockChainAddressWallet3
from .TradingPartyCapacity5Choice import TradingPartyCapacity5Choice
from .PartyIdentification120Choice import PartyIdentification120Choice
from .LEIIdentifier import LEIIdentifier

class PartyIdentificationAndAccount203(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AltrnId", "_SfkpgAcct", "_LEI", "_BlckChainAdrOrWllt", "_PtyCpcty"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

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
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

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
	def PtyCpcty(self):
		return self._PtyCpcty

	@PtyCpcty.setter
	def PtyCpcty(self, value):
		self._PtyCpcty = value if type(value) != base_types.auto else self.make_default("PtyCpcty")

	@PtyCpcty.deleter
	def PtyCpcty(self):
		del self._PtyCpcty
		self._PtyCpcty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification120Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCpcty', type=TradingPartyCapacity5Choice, min=0, max=1, mutex_group=None, array=False),
	))

