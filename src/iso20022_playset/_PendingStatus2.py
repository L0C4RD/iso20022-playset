# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PendingStatus76Choice
from . import Quantity54Choice

class PendingStatus2(base_types._BaseFieldType):

	__slots__ = ["_PdgQty", "_PdgRsn"]
	@property
	def PdgQty(self):
		return self._PdgQty

	@PdgQty.setter
	def PdgQty(self, value):
		self._PdgQty = value if value is not None else base_types.UninitialisedField(self, 'PdgQty', Quantity54Choice, False)

	@PdgQty.deleter
	def PdgQty(self):
		del self._PdgQty
		self._PdgQty = base_types.UninitialisedField(self, 'PdgQty', Quantity54Choice, False)

	@property
	def PdgRsn(self):
		return self._PdgRsn

	@PdgRsn.setter
	def PdgRsn(self, value):
		self._PdgRsn = value if value is not None else base_types.UninitialisedField(self, 'PdgRsn', PendingStatus76Choice, False)

	@PdgRsn.deleter
	def PdgRsn(self):
		del self._PdgRsn
		self._PdgRsn = base_types.UninitialisedField(self, 'PdgRsn', PendingStatus76Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgRsn', type=PendingStatus76Choice, min=1, max=1, mutex_group=None, array=False),
	))