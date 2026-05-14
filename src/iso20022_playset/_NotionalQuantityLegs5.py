# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NotionalQuantity9 import NotionalQuantity9

class NotionalQuantityLegs5(base_types._BaseFieldType):

	__slots__ = ["_FrstLeg", "_ScndLeg"]
	@property
	def FrstLeg(self):
		return self._FrstLeg

	@FrstLeg.setter
	def FrstLeg(self, value):
		self._FrstLeg = value if type(value) != base_types.auto else self.make_default("FrstLeg")

	@FrstLeg.deleter
	def FrstLeg(self):
		del self._FrstLeg
		self._FrstLeg = None

	@property
	def ScndLeg(self):
		return self._ScndLeg

	@ScndLeg.setter
	def ScndLeg(self, value):
		self._ScndLeg = value if type(value) != base_types.auto else self.make_default("ScndLeg")

	@ScndLeg.deleter
	def ScndLeg(self):
		del self._ScndLeg
		self._ScndLeg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstLeg', type=NotionalQuantity9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLeg', type=NotionalQuantity9, min=0, max=1, mutex_group=None, array=False),
	))