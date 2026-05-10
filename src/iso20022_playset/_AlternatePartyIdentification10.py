from . import base_types
from ._IdentificationType42Choice import IdentificationType42Choice
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text

class AlternatePartyIdentification10(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_TpOfId", "_AltrnId"]
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
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def TpOfId(self):
		return self._TpOfId

	@TpOfId.setter
	def TpOfId(self, value):
		self._TpOfId = value if type(value) != base_types.auto else self.make_default("TpOfId")

	@TpOfId.deleter
	def TpOfId(self):
		del self._TpOfId
		self._TpOfId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfId', type=IdentificationType42Choice, min=1, max=1, mutex_group=None, array=False),
	))

