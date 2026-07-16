# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FreightCommodityContainerShip2
from . import FreightCommodityDry3
from . import FreightCommodityOther2
from . import FreightCommodityWet3

class AssetClassCommodityFreight4Choice(base_types._BaseFieldType):

	__slots__ = ["_CntnrShip", "_Dry", "_Othr", "_Wet"]
	@property
	def CntnrShip(self):
		return self._CntnrShip

	@CntnrShip.setter
	def CntnrShip(self, value):
		self._CntnrShip = value if value is not None else base_types.UninitialisedField(self, 'CntnrShip', FreightCommodityContainerShip2, False)

	@CntnrShip.deleter
	def CntnrShip(self):
		del self._CntnrShip
		self._CntnrShip = base_types.UninitialisedField(self, 'CntnrShip', FreightCommodityContainerShip2, False)

	@property
	def Dry(self):
		return self._Dry

	@Dry.setter
	def Dry(self, value):
		self._Dry = value if value is not None else base_types.UninitialisedField(self, 'Dry', FreightCommodityDry3, False)

	@Dry.deleter
	def Dry(self):
		del self._Dry
		self._Dry = base_types.UninitialisedField(self, 'Dry', FreightCommodityDry3, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', FreightCommodityOther2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', FreightCommodityOther2, False)

	@property
	def Wet(self):
		return self._Wet

	@Wet.setter
	def Wet(self, value):
		self._Wet = value if value is not None else base_types.UninitialisedField(self, 'Wet', FreightCommodityWet3, False)

	@Wet.deleter
	def Wet(self):
		del self._Wet
		self._Wet = base_types.UninitialisedField(self, 'Wet', FreightCommodityWet3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntnrShip', type=FreightCommodityContainerShip2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dry', type=FreightCommodityDry3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=FreightCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wet', type=FreightCommodityWet3, min=0, max=1, mutex_group=1, array=False),
	))