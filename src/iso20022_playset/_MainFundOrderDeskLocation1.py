from . import base_types
from ._CountryCode import CountryCode
from ._UTCOffset1 import UTCOffset1

class MainFundOrderDeskLocation1(base_types._BaseFieldType):

	__slots__ = ["_TmZoneOffSet", "_Ctry"]
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
	def TmZoneOffSet(self):
		return self._TmZoneOffSet

	@TmZoneOffSet.setter
	def TmZoneOffSet(self, value):
		self._TmZoneOffSet = value if type(value) != base_types.auto else self.make_default("TmZoneOffSet")

	@TmZoneOffSet.deleter
	def TmZoneOffSet(self):
		del self._TmZoneOffSet
		self._TmZoneOffSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZoneOffSet', type=UTCOffset1, min=1, max=1, mutex_group=None, array=False),
	))

