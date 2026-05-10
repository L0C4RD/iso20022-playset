from . import base_types
from ._CountryCode import CountryCode
from ._ExternalTypeOfParty1Code import ExternalTypeOfParty1Code

class PlaceOfPresentation1(base_types._BaseFieldType):

	__slots__ = ["_Plc", "_Ctry"]
	@property
	def Plc(self):
		return self._Plc

	@Plc.setter
	def Plc(self, value):
		self._Plc = value if type(value) != base_types.auto else self.make_default("Plc")

	@Plc.deleter
	def Plc(self):
		del self._Plc
		self._Plc = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plc', type=ExternalTypeOfParty1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

