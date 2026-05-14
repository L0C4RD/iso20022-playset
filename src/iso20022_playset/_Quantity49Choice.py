# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ProprietaryQuantity7 import ProprietaryQuantity7
from ._Quantity50Choice import Quantity50Choice

class Quantity49Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryQty", "_QtyChc"]
	@property
	def PrtryQty(self):
		return self._PrtryQty

	@PrtryQty.setter
	def PrtryQty(self, value):
		self._PrtryQty = value if type(value) != base_types.auto else self.make_default("PrtryQty")

	@PrtryQty.deleter
	def PrtryQty(self):
		del self._PrtryQty
		self._PrtryQty = None

	@property
	def QtyChc(self):
		return self._QtyChc

	@QtyChc.setter
	def QtyChc(self, value):
		self._QtyChc = value if type(value) != base_types.auto else self.make_default("QtyChc")

	@QtyChc.deleter
	def QtyChc(self):
		del self._QtyChc
		self._QtyChc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryQty', type=ProprietaryQuantity7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyChc', type=Quantity50Choice, min=0, max=1, mutex_group=1, array=False),
	))