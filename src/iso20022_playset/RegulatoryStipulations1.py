from . import base_types
from .CountryCode import CountryCode
from .Max350Text import Max350Text

class RegulatoryStipulations1(base_types._BaseFieldType):

	__slots__ = ["_Stiptns", "_Ctry"]
	@property
	def Stiptns(self):
		return self._Stiptns

	@Stiptns.setter
	def Stiptns(self, value):
		self._Stiptns = value if type(value) != auto else self.make_default("Stiptns")

	@Stiptns.deleter
	def Stiptns(self):
		del self._Stiptns
		self._Stiptns = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Stiptns', type=Max350Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

