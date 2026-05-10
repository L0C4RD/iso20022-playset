from . import base_types
from ._FreightCommodityWet2 import FreightCommodityWet2
from ._FreightCommodityOther1 import FreightCommodityOther1
from ._FreightCommodityContainerShip1 import FreightCommodityContainerShip1
from ._FreightCommodityDry2 import FreightCommodityDry2

class AssetClassCommodityFreight3Choice(base_types._BaseFieldType):

	__slots__ = ["_CntnrShip", "_Dry", "_Wet", "_Othr"]
	@property
	def CntnrShip(self):
		return self._CntnrShip

	@CntnrShip.setter
	def CntnrShip(self, value):
		self._CntnrShip = value if type(value) != base_types.auto else self.make_default("CntnrShip")

	@CntnrShip.deleter
	def CntnrShip(self):
		del self._CntnrShip
		self._CntnrShip = None

	@property
	def Dry(self):
		return self._Dry

	@Dry.setter
	def Dry(self, value):
		self._Dry = value if type(value) != base_types.auto else self.make_default("Dry")

	@Dry.deleter
	def Dry(self):
		del self._Dry
		self._Dry = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Wet(self):
		return self._Wet

	@Wet.setter
	def Wet(self, value):
		self._Wet = value if type(value) != base_types.auto else self.make_default("Wet")

	@Wet.deleter
	def Wet(self):
		del self._Wet
		self._Wet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntnrShip', type=FreightCommodityContainerShip1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dry', type=FreightCommodityDry2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=FreightCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wet', type=FreightCommodityWet2, min=0, max=1, mutex_group=1, array=False),
	))

