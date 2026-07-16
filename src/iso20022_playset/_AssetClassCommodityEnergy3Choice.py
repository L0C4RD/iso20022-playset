# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EnergyCommodityCoal2
from . import EnergyCommodityDistillates2
from . import EnergyCommodityElectricity2
from . import EnergyCommodityInterEnergy2
from . import EnergyCommodityLightEnd2
from . import EnergyCommodityNaturalGas3
from . import EnergyCommodityOil3
from . import EnergyCommodityOther2
from . import EnergyCommodityRenewableEnergy2

class AssetClassCommodityEnergy3Choice(base_types._BaseFieldType):

	__slots__ = ["_Coal", "_Dstllts", "_Elctrcty", "_IntrNrgy", "_LghtEnd", "_NtrlGas", "_Oil", "_Othr", "_RnwblNrgy"]
	@property
	def Coal(self):
		return self._Coal

	@Coal.setter
	def Coal(self, value):
		self._Coal = value if value is not None else base_types.UninitialisedField(self, 'Coal', EnergyCommodityCoal2, False)

	@Coal.deleter
	def Coal(self):
		del self._Coal
		self._Coal = base_types.UninitialisedField(self, 'Coal', EnergyCommodityCoal2, False)

	@property
	def Dstllts(self):
		return self._Dstllts

	@Dstllts.setter
	def Dstllts(self, value):
		self._Dstllts = value if value is not None else base_types.UninitialisedField(self, 'Dstllts', EnergyCommodityDistillates2, False)

	@Dstllts.deleter
	def Dstllts(self):
		del self._Dstllts
		self._Dstllts = base_types.UninitialisedField(self, 'Dstllts', EnergyCommodityDistillates2, False)

	@property
	def Elctrcty(self):
		return self._Elctrcty

	@Elctrcty.setter
	def Elctrcty(self, value):
		self._Elctrcty = value if value is not None else base_types.UninitialisedField(self, 'Elctrcty', EnergyCommodityElectricity2, False)

	@Elctrcty.deleter
	def Elctrcty(self):
		del self._Elctrcty
		self._Elctrcty = base_types.UninitialisedField(self, 'Elctrcty', EnergyCommodityElectricity2, False)

	@property
	def IntrNrgy(self):
		return self._IntrNrgy

	@IntrNrgy.setter
	def IntrNrgy(self, value):
		self._IntrNrgy = value if value is not None else base_types.UninitialisedField(self, 'IntrNrgy', EnergyCommodityInterEnergy2, False)

	@IntrNrgy.deleter
	def IntrNrgy(self):
		del self._IntrNrgy
		self._IntrNrgy = base_types.UninitialisedField(self, 'IntrNrgy', EnergyCommodityInterEnergy2, False)

	@property
	def LghtEnd(self):
		return self._LghtEnd

	@LghtEnd.setter
	def LghtEnd(self, value):
		self._LghtEnd = value if value is not None else base_types.UninitialisedField(self, 'LghtEnd', EnergyCommodityLightEnd2, False)

	@LghtEnd.deleter
	def LghtEnd(self):
		del self._LghtEnd
		self._LghtEnd = base_types.UninitialisedField(self, 'LghtEnd', EnergyCommodityLightEnd2, False)

	@property
	def NtrlGas(self):
		return self._NtrlGas

	@NtrlGas.setter
	def NtrlGas(self, value):
		self._NtrlGas = value if value is not None else base_types.UninitialisedField(self, 'NtrlGas', EnergyCommodityNaturalGas3, False)

	@NtrlGas.deleter
	def NtrlGas(self):
		del self._NtrlGas
		self._NtrlGas = base_types.UninitialisedField(self, 'NtrlGas', EnergyCommodityNaturalGas3, False)

	@property
	def Oil(self):
		return self._Oil

	@Oil.setter
	def Oil(self, value):
		self._Oil = value if value is not None else base_types.UninitialisedField(self, 'Oil', EnergyCommodityOil3, False)

	@Oil.deleter
	def Oil(self):
		del self._Oil
		self._Oil = base_types.UninitialisedField(self, 'Oil', EnergyCommodityOil3, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', EnergyCommodityOther2, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', EnergyCommodityOther2, False)

	@property
	def RnwblNrgy(self):
		return self._RnwblNrgy

	@RnwblNrgy.setter
	def RnwblNrgy(self, value):
		self._RnwblNrgy = value if value is not None else base_types.UninitialisedField(self, 'RnwblNrgy', EnergyCommodityRenewableEnergy2, False)

	@RnwblNrgy.deleter
	def RnwblNrgy(self):
		del self._RnwblNrgy
		self._RnwblNrgy = base_types.UninitialisedField(self, 'RnwblNrgy', EnergyCommodityRenewableEnergy2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coal', type=EnergyCommodityCoal2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dstllts', type=EnergyCommodityDistillates2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Elctrcty', type=EnergyCommodityElectricity2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrNrgy', type=EnergyCommodityInterEnergy2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LghtEnd', type=EnergyCommodityLightEnd2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlGas', type=EnergyCommodityNaturalGas3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Oil', type=EnergyCommodityOil3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=EnergyCommodityOther2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RnwblNrgy', type=EnergyCommodityRenewableEnergy2, min=0, max=1, mutex_group=1, array=False),
	))