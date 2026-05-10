import base_types
import PartyIdentificationAndAccount206

class Counterparty16Choice(base_types._BaseFieldType):

	__slots__ = ["_Sellr", "_Buyr"]
	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sellr', type=PartyIdentificationAndAccount206, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentificationAndAccount206, min=0, max=1, mutex_group=1, array=False),
	))

