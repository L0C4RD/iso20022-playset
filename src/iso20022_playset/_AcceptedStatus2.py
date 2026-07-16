# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptedStatus8Choice
from . import Quantity51Choice

class AcceptedStatus2(base_types._BaseFieldType):

	__slots__ = ["_AccptdQty", "_AccptdRsn"]
	@property
	def AccptdQty(self):
		return self._AccptdQty

	@AccptdQty.setter
	def AccptdQty(self, value):
		self._AccptdQty = value if value is not None else base_types.UninitialisedField(self, 'AccptdQty', Quantity51Choice, False)

	@AccptdQty.deleter
	def AccptdQty(self):
		del self._AccptdQty
		self._AccptdQty = base_types.UninitialisedField(self, 'AccptdQty', Quantity51Choice, False)

	@property
	def AccptdRsn(self):
		return self._AccptdRsn

	@AccptdRsn.setter
	def AccptdRsn(self, value):
		self._AccptdRsn = value if value is not None else base_types.UninitialisedField(self, 'AccptdRsn', AcceptedStatus8Choice, False)

	@AccptdRsn.deleter
	def AccptdRsn(self):
		del self._AccptdRsn
		self._AccptdRsn = base_types.UninitialisedField(self, 'AccptdRsn', AcceptedStatus8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdRsn', type=AcceptedStatus8Choice, min=1, max=1, mutex_group=None, array=False),
	))