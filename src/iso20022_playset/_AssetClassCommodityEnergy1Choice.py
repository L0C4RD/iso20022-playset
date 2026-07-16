# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EnergyCommodityCoal1
from . import EnergyCommodityDistillates1
from . import EnergyCommodityElectricity1
from . import EnergyCommodityInterEnergy1
from . import EnergyCommodityLightEnd1
from . import EnergyCommodityNaturalGas1
from . import EnergyCommodityOil1
from . import EnergyCommodityRenewableEnergy1

class AssetClassCommodityEnergy1Choice(base_types._BaseFieldType):

	__slots__ = ["_Coal", "_Dstllts", "_Elctrcty", "_IntrNrgy", "_LghtEnd", "_NtrlGas", "_Oil", "_RnwblNrgy"]
	@property
	def Coal(self):
		return self._Coal

	@Coal.setter
	def Coal(self, value):
		self._Coal = value if value is not None else base_types.UninitialisedField(self, 'Coal', EnergyCommodityCoal1, False)

	@Coal.deleter
	def Coal(self):
		del self._Coal
		self._Coal = base_types.UninitialisedField(self, 'Coal', EnergyCommodityCoal1, False)

	@property
	def Dstllts(self):
		return self._Dstllts

	@Dstllts.setter
	def Dstllts(self, value):
		self._Dstllts = value if value is not None else base_types.UninitialisedField(self, 'Dstllts', EnergyCommodityDistillates1, False)

	@Dstllts.deleter
	def Dstllts(self):
		del self._Dstllts
		self._Dstllts = base_types.UninitialisedField(self, 'Dstllts', EnergyCommodityDistillates1, False)

	@property
	def Elctrcty(self):
		return self._Elctrcty

	@Elctrcty.setter
	def Elctrcty(self, value):
		self._Elctrcty = value if value is not None else base_types.UninitialisedField(self, 'Elctrcty', EnergyCommodityElectricity1, False)

	@Elctrcty.deleter
	def Elctrcty(self):
		del self._Elctrcty
		self._Elctrcty = base_types.UninitialisedField(self, 'Elctrcty', EnergyCommodityElectricity1, False)

	@property
	def IntrNrgy(self):
		return self._IntrNrgy

	@IntrNrgy.setter
	def IntrNrgy(self, value):
		self._IntrNrgy = value if value is not None else base_types.UninitialisedField(self, 'IntrNrgy', EnergyCommodityInterEnergy1, False)

	@IntrNrgy.deleter
	def IntrNrgy(self):
		del self._IntrNrgy
		self._IntrNrgy = base_types.UninitialisedField(self, 'IntrNrgy', EnergyCommodityInterEnergy1, False)

	@property
	def LghtEnd(self):
		return self._LghtEnd

	@LghtEnd.setter
	def LghtEnd(self, value):
		self._LghtEnd = value if value is not None else base_types.UninitialisedField(self, 'LghtEnd', EnergyCommodityLightEnd1, False)

	@LghtEnd.deleter
	def LghtEnd(self):
		del self._LghtEnd
		self._LghtEnd = base_types.UninitialisedField(self, 'LghtEnd', EnergyCommodityLightEnd1, False)

	@property
	def NtrlGas(self):
		return self._NtrlGas

	@NtrlGas.setter
	def NtrlGas(self, value):
		self._NtrlGas = value if value is not None else base_types.UninitialisedField(self, 'NtrlGas', EnergyCommodityNaturalGas1, False)

	@NtrlGas.deleter
	def NtrlGas(self):
		del self._NtrlGas
		self._NtrlGas = base_types.UninitialisedField(self, 'NtrlGas', EnergyCommodityNaturalGas1, False)

	@property
	def Oil(self):
		return self._Oil

	@Oil.setter
	def Oil(self, value):
		self._Oil = value if value is not None else base_types.UninitialisedField(self, 'Oil', EnergyCommodityOil1, False)

	@Oil.deleter
	def Oil(self):
		del self._Oil
		self._Oil = base_types.UninitialisedField(self, 'Oil', EnergyCommodityOil1, False)

	@property
	def RnwblNrgy(self):
		return self._RnwblNrgy

	@RnwblNrgy.setter
	def RnwblNrgy(self, value):
		self._RnwblNrgy = value if value is not None else base_types.UninitialisedField(self, 'RnwblNrgy', EnergyCommodityRenewableEnergy1, False)

	@RnwblNrgy.deleter
	def RnwblNrgy(self):
		del self._RnwblNrgy
		self._RnwblNrgy = base_types.UninitialisedField(self, 'RnwblNrgy', EnergyCommodityRenewableEnergy1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Coal', type=EnergyCommodityCoal1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dstllts', type=EnergyCommodityDistillates1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Elctrcty', type=EnergyCommodityElectricity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrNrgy', type=EnergyCommodityInterEnergy1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LghtEnd', type=EnergyCommodityLightEnd1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtrlGas', type=EnergyCommodityNaturalGas1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Oil', type=EnergyCommodityOil1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RnwblNrgy', type=EnergyCommodityRenewableEnergy1, min=0, max=1, mutex_group=1, array=False),
	))