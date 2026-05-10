from . import base_types
from .Max256Text import Max256Text
from .POIComponentStatus1Code import POIComponentStatus1Code
from .ISODate import ISODate

class PointOfInteractionComponentStatus3(base_types._BaseFieldType):

	__slots__ = ["_XpryDt", "_Sts", "_VrsnNb"]
	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if type(value) != base_types.auto else self.make_default("VrsnNb")

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=POIComponentStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

