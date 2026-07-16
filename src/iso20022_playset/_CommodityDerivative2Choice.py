# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommodityDerivative5
from . import CommodityDerivative6

class CommodityDerivative2Choice(base_types._BaseFieldType):

	__slots__ = ["_Frght", "_Nrgy"]
	@property
	def Frght(self):
		return self._Frght

	@Frght.setter
	def Frght(self, value):
		self._Frght = value if value is not None else base_types.UninitialisedField(self, 'Frght', CommodityDerivative5, False)

	@Frght.deleter
	def Frght(self):
		del self._Frght
		self._Frght = base_types.UninitialisedField(self, 'Frght', CommodityDerivative5, False)

	@property
	def Nrgy(self):
		return self._Nrgy

	@Nrgy.setter
	def Nrgy(self, value):
		self._Nrgy = value if value is not None else base_types.UninitialisedField(self, 'Nrgy', CommodityDerivative6, False)

	@Nrgy.deleter
	def Nrgy(self):
		del self._Nrgy
		self._Nrgy = base_types.UninitialisedField(self, 'Nrgy', CommodityDerivative6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frght', type=CommodityDerivative5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nrgy', type=CommodityDerivative6, min=0, max=1, mutex_group=1, array=False),
	))