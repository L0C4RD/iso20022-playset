from . import base_types
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text
from ._PartyIdentification147Choice import PartyIdentification147Choice
from ._AlternatePartyIdentification9 import AlternatePartyIdentification9
from ._CashAccountIdentification12Choice import CashAccountIdentification12Choice

class PartyIdentificationAndAccount232(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_AltrnId", "_PrcgId", "_Id"]
	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification12Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification147Choice, min=1, max=1, mutex_group=None, array=False),
	))

