# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Quantity10

class Consignment3(base_types._BaseFieldType):

	__slots__ = ["_TtlQty", "_TtlVol", "_TtlWght"]
	@property
	def TtlQty(self):
		return self._TtlQty

	@TtlQty.setter
	def TtlQty(self, value):
		self._TtlQty = value if value is not None else base_types.UninitialisedField(self, 'TtlQty', Quantity10, False)

	@TtlQty.deleter
	def TtlQty(self):
		del self._TtlQty
		self._TtlQty = base_types.UninitialisedField(self, 'TtlQty', Quantity10, False)

	@property
	def TtlVol(self):
		return self._TtlVol

	@TtlVol.setter
	def TtlVol(self, value):
		self._TtlVol = value if value is not None else base_types.UninitialisedField(self, 'TtlVol', Quantity10, False)

	@TtlVol.deleter
	def TtlVol(self):
		del self._TtlVol
		self._TtlVol = base_types.UninitialisedField(self, 'TtlVol', Quantity10, False)

	@property
	def TtlWght(self):
		return self._TtlWght

	@TtlWght.setter
	def TtlWght(self, value):
		self._TtlWght = value if value is not None else base_types.UninitialisedField(self, 'TtlWght', Quantity10, False)

	@TtlWght.deleter
	def TtlWght(self):
		del self._TtlWght
		self._TtlWght = base_types.UninitialisedField(self, 'TtlWght', Quantity10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlQty', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVol', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlWght', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
	))