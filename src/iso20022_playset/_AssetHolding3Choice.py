# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Commodity2
from . import Guarantee1
from . import SecurityIdentificationAndAmount1
from . import TripartyCollateralAndAmount1

class AssetHolding3Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_Csh", "_Gold", "_Grnt", "_Scty", "_Trpty"]
	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', Commodity2, False)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', Commodity2, False)

	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if value is not None else base_types.UninitialisedField(self, 'Csh', ActiveCurrencyAndAmount, False)

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = base_types.UninitialisedField(self, 'Csh', ActiveCurrencyAndAmount, False)

	@property
	def Gold(self):
		return self._Gold

	@Gold.setter
	def Gold(self, value):
		self._Gold = value if value is not None else base_types.UninitialisedField(self, 'Gold', ActiveCurrencyAndAmount, False)

	@Gold.deleter
	def Gold(self):
		del self._Gold
		self._Gold = base_types.UninitialisedField(self, 'Gold', ActiveCurrencyAndAmount, False)

	@property
	def Grnt(self):
		return self._Grnt

	@Grnt.setter
	def Grnt(self, value):
		self._Grnt = value if value is not None else base_types.UninitialisedField(self, 'Grnt', Guarantee1, False)

	@Grnt.deleter
	def Grnt(self):
		del self._Grnt
		self._Grnt = base_types.UninitialisedField(self, 'Grnt', Guarantee1, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', SecurityIdentificationAndAmount1, False)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', SecurityIdentificationAndAmount1, False)

	@property
	def Trpty(self):
		return self._Trpty

	@Trpty.setter
	def Trpty(self, value):
		self._Trpty = value if value is not None else base_types.UninitialisedField(self, 'Trpty', TripartyCollateralAndAmount1, False)

	@Trpty.deleter
	def Trpty(self):
		del self._Trpty
		self._Trpty = base_types.UninitialisedField(self, 'Trpty', TripartyCollateralAndAmount1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmmdty', type=Commodity2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Csh', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gold', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Grnt', type=Guarantee1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=SecurityIdentificationAndAmount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Trpty', type=TripartyCollateralAndAmount1, min=0, max=1, mutex_group=1, array=False),
	))