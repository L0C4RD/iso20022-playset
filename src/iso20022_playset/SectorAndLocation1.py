from . import base_types
from .CountryCode import CountryCode
from .SNA2008SectorIdentifier import SNA2008SectorIdentifier

class SectorAndLocation1(base_types._BaseFieldType):

	__slots__ = ["_Sctr", "_Lctn"]
	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != base_types.auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sctr', type=SNA2008SectorIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))

