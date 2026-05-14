# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CommodityDerivative5 import CommodityDerivative5
from ._CommodityDerivative6 import CommodityDerivative6

class CommodityDerivative2Choice(base_types._BaseFieldType):

	__slots__ = ["_Frght", "_Nrgy"]
	@property
	def Frght(self):
		return self._Frght

	@Frght.setter
	def Frght(self, value):
		self._Frght = value if type(value) != base_types.auto else self.make_default("Frght")

	@Frght.deleter
	def Frght(self):
		del self._Frght
		self._Frght = None

	@property
	def Nrgy(self):
		return self._Nrgy

	@Nrgy.setter
	def Nrgy(self, value):
		self._Nrgy = value if type(value) != base_types.auto else self.make_default("Nrgy")

	@Nrgy.deleter
	def Nrgy(self):
		del self._Nrgy
		self._Nrgy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frght', type=CommodityDerivative5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nrgy', type=CommodityDerivative6, min=0, max=1, mutex_group=1, array=False),
	))