from . import base_types
from .Commodity2 import Commodity2
from .TripartyCollateralAndAmount1 import TripartyCollateralAndAmount1
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Guarantee1 import Guarantee1
from .SecurityIdentificationAndAmount1 import SecurityIdentificationAndAmount1

class AssetHolding3Choice(base_types._BaseFieldType):

	__slots__ = ["_Grnt", "_Trpty", "_Csh", "_Cmmdty", "_Gold", "_Scty"]
	@property
	def Grnt(self):
		return self._Grnt

	@Grnt.setter
	def Grnt(self, value):
		self._Grnt = value if type(value) != base_types.auto else self.make_default("Grnt")

	@Grnt.deleter
	def Grnt(self):
		del self._Grnt
		self._Grnt = None

	@property
	def Trpty(self):
		return self._Trpty

	@Trpty.setter
	def Trpty(self, value):
		self._Trpty = value if type(value) != base_types.auto else self.make_default("Trpty")

	@Trpty.deleter
	def Trpty(self):
		del self._Trpty
		self._Trpty = None

	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if type(value) != base_types.auto else self.make_default("Csh")

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	@property
	def Gold(self):
		return self._Gold

	@Gold.setter
	def Gold(self, value):
		self._Gold = value if type(value) != base_types.auto else self.make_default("Gold")

	@Gold.deleter
	def Gold(self):
		del self._Gold
		self._Gold = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != base_types.auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Grnt', type=Guarantee1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trpty', type=TripartyCollateralAndAmount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Csh', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmmdty', type=Commodity2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gold', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityIdentificationAndAmount1, min=0, max=1, mutex_group=1, array=False),
	))

