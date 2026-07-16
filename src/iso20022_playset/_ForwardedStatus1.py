# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoSpecifiedReason1
from . import Quantity51Choice

class ForwardedStatus1(base_types._BaseFieldType):

	__slots__ = ["_FwddQty", "_FwddRsn"]
	@property
	def FwddQty(self):
		return self._FwddQty

	@FwddQty.setter
	def FwddQty(self, value):
		self._FwddQty = value if value is not None else base_types.UninitialisedField(self, 'FwddQty', Quantity51Choice, False)

	@FwddQty.deleter
	def FwddQty(self):
		del self._FwddQty
		self._FwddQty = base_types.UninitialisedField(self, 'FwddQty', Quantity51Choice, False)

	@property
	def FwddRsn(self):
		return self._FwddRsn

	@FwddRsn.setter
	def FwddRsn(self, value):
		self._FwddRsn = value if value is not None else base_types.UninitialisedField(self, 'FwddRsn', NoSpecifiedReason1, False)

	@FwddRsn.deleter
	def FwddRsn(self):
		del self._FwddRsn
		self._FwddRsn = base_types.UninitialisedField(self, 'FwddRsn', NoSpecifiedReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FwddQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwddRsn', type=NoSpecifiedReason1, min=1, max=1, mutex_group=None, array=False),
	))