from . import base_types
import FreightCommodityWet1
import FreightCommodityDry1
import FreightCommodityContainerShip1

class AssetClassCommodityFreight1Choice(base_types._BaseFieldType):

	__slots__ = ["_Wet", "_CntnrShip", "_Dry"]
	@property
	def Wet(self):
		return self._Wet

	@Wet.setter
	def Wet(self, value):
		self._Wet = value if type(value) != auto else self.make_default("Wet")

	@Wet.deleter
	def Wet(self):
		del self._Wet
		self._Wet = None

	@property
	def CntnrShip(self):
		return self._CntnrShip

	@CntnrShip.setter
	def CntnrShip(self, value):
		self._CntnrShip = value if type(value) != auto else self.make_default("CntnrShip")

	@CntnrShip.deleter
	def CntnrShip(self):
		del self._CntnrShip
		self._CntnrShip = None

	@property
	def Dry(self):
		return self._Dry

	@Dry.setter
	def Dry(self, value):
		self._Dry = value if type(value) != auto else self.make_default("Dry")

	@Dry.deleter
	def Dry(self):
		del self._Dry
		self._Dry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Wet', type=FreightCommodityWet1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CntnrShip', type=FreightCommodityContainerShip1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dry', type=FreightCommodityDry1, min=0, max=1, mutex_group=1, array=False),
	))

