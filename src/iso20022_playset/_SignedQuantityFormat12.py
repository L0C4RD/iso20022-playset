# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Quantity53Choice
from . import ShortLong1Code

class SignedQuantityFormat12(base_types._BaseFieldType):

	__slots__ = ["_QtyChc", "_ShrtLngPos"]
	@property
	def QtyChc(self):
		return self._QtyChc

	@QtyChc.setter
	def QtyChc(self, value):
		self._QtyChc = value if value is not None else base_types.UninitialisedField(self, 'QtyChc', Quantity53Choice, False)

	@QtyChc.deleter
	def QtyChc(self):
		del self._QtyChc
		self._QtyChc = base_types.UninitialisedField(self, 'QtyChc', Quantity53Choice, False)

	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if value is not None else base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyChc', type=Quantity53Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))