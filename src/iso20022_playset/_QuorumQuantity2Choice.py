# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Percentage14Rate

class QuorumQuantity2Choice(base_types._BaseFieldType):

	__slots__ = ["_QrmQty", "_QrmQtyPctg"]
	@property
	def QrmQty(self):
		return self._QrmQty

	@QrmQty.setter
	def QrmQty(self, value):
		self._QrmQty = value if value is not None else base_types.UninitialisedField(self, 'QrmQty', Max35Text, False)

	@QrmQty.deleter
	def QrmQty(self):
		del self._QrmQty
		self._QrmQty = base_types.UninitialisedField(self, 'QrmQty', Max35Text, False)

	@property
	def QrmQtyPctg(self):
		return self._QrmQtyPctg

	@QrmQtyPctg.setter
	def QrmQtyPctg(self, value):
		self._QrmQtyPctg = value if value is not None else base_types.UninitialisedField(self, 'QrmQtyPctg', Percentage14Rate, False)

	@QrmQtyPctg.deleter
	def QrmQtyPctg(self):
		del self._QrmQtyPctg
		self._QrmQtyPctg = base_types.UninitialisedField(self, 'QrmQtyPctg', Percentage14Rate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QrmQty', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QrmQtyPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))