from . import base_types
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text
from ._PartyIdentification258Choice import PartyIdentification258Choice
from ._AlternatePartyIdentification9 import AlternatePartyIdentification9

class PartyIdentification318(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_PrcgId", "_Id"]
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
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification258Choice, min=1, max=1, mutex_group=None, array=False),
	))

