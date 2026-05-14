# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EnergyCommodityCoal1 import EnergyCommodityCoal1
from ._EnergyCommodityDistillates1 import EnergyCommodityDistillates1
from ._EnergyCommodityElectricity1 import EnergyCommodityElectricity1
from ._EnergyCommodityInterEnergy1 import EnergyCommodityInterEnergy1
from ._EnergyCommodityLightEnd1 import EnergyCommodityLightEnd1
from ._EnergyCommodityNaturalGas2 import EnergyCommodityNaturalGas2
from ._EnergyCommodityOil2 import EnergyCommodityOil2
from ._EnergyCommodityOther1 import EnergyCommodityOther1
from ._EnergyCommodityRenewableEnergy1 import EnergyCommodityRenewableEnergy1

class AssetClassCommodityEnergy2Choice(base_types._BaseFieldType):

	__slots__ = ["_Coal", "_Dstllts", "_Elctrcty", "_IntrNrgy", "_LghtEnd", "_NtrlGas", "_Oil", "_Othr", "_RnwblNrgy"]
	@property
	def Coal(self):
		return self._Coal

	@Coal.setter
	def Coal(self, value):
		self._Coal = value if type(value) != base_types.auto else self.make_default("Coal")

	@Coal.deleter
	def Coal(self):
		del self._Coal
		self._Coal = None

	@property
	def Dstllts(self):
		return self._Dstllts

	@Dstllts.setter
	def Dstllts(self, value):
		self._Dstllts = value if type(value) != base_types.auto else self.make_default("Dstllts")

	@Dstllts.deleter
	def Dstllts(self):
		del self._Dstllts
		self._Dstllts = None

	@property
	def Elctrcty(self):
		return self._Elctrcty

	@Elctrcty.setter
	def Elctrcty(self, value):
		self._Elctrcty = value if type(value) != base_types.auto else self.make_default("Elctrcty")

	@Elctrcty.deleter
	def Elctrcty(self):
		del self._Elctrcty
		self._Elctrcty = None

	@property
	def IntrNrgy(self):
		return self._IntrNrgy

	@IntrNrgy.setter
	def IntrNrgy(self, value):
		self._IntrNrgy = value if type(value) != base_types.auto else self.make_default("IntrNrgy")

	@IntrNrgy.deleter
	def IntrNrgy(self):
		del self._IntrNrgy
		self._IntrNrgy = None

	@property
	def LghtEnd(self):
		return self._LghtEnd

	@LghtEnd.setter
	def LghtEnd(self, value):
		self._LghtEnd = value if type(value) != base_types.auto else self.make_default("LghtEnd")

	@LghtEnd.deleter
	def LghtEnd(self):
		del self._LghtEnd
		self._LghtEnd = None

	@property
	def NtrlGas(self):
		return self._NtrlGas

	@NtrlGas.setter
	def NtrlGas(self, value):
		self._NtrlGas = value if type(value) != base_types.auto else self.make_default("NtrlGas")

	@NtrlGas.deleter
	def NtrlGas(self):
		del self._NtrlGas
		self._NtrlGas = None

	@property
	def Oil(self):
		return self._Oil

	@Oil.setter
	def Oil(self, value):
		self._Oil = value if type(value) != base_types.auto else self.make_default("Oil")

	@Oil.deleter
	def Oil(self):
		del self._Oil
		self._Oil = None

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
	def RnwblNrgy(self):
		return self._RnwblNrgy

	@RnwblNrgy.setter
	def RnwblNrgy(self, value):
		self._RnwblNrgy = value if type(value) != base_types.auto else self.make_default("RnwblNrgy")

	@RnwblNrgy.deleter
	def RnwblNrgy(self):
		del self._RnwblNrgy
		self._RnwblNrgy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coal', type=EnergyCommodityCoal1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dstllts', type=EnergyCommodityDistillates1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Elctrcty', type=EnergyCommodityElectricity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrNrgy', type=EnergyCommodityInterEnergy1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LghtEnd', type=EnergyCommodityLightEnd1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlGas', type=EnergyCommodityNaturalGas2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Oil', type=EnergyCommodityOil2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=EnergyCommodityOther1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RnwblNrgy', type=EnergyCommodityRenewableEnergy1, min=0, max=1, mutex_group=1, array=False),
	))