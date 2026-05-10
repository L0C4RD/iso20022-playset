from . import base_types
from ._Max35Text import Max35Text
from ._Max140Text import Max140Text
from ._AlternatePartyIdentification7 import AlternatePartyIdentification7
from ._PartyIdentification120Choice import PartyIdentification120Choice

class PartyIdentificationAndAccount204(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PrcgId", "_AltrnId", "_BlckChainAdrOrWllt", "_SfkpgAcct"]
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
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if type(value) != base_types.auto else self.make_default("PrcgId")

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification120Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

