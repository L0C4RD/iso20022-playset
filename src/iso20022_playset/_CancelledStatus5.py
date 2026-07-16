# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatus12Choice
from . import Quantity51Choice

class CancelledStatus5(base_types._BaseFieldType):

	__slots__ = ["_CancQty", "_CxlRsn"]
	@property
	def CancQty(self):
		return self._CancQty

	@CancQty.setter
	def CancQty(self, value):
		self._CancQty = value if value is not None else base_types.UninitialisedField(self, 'CancQty', Quantity51Choice, False)

	@CancQty.deleter
	def CancQty(self):
		del self._CancQty
		self._CancQty = base_types.UninitialisedField(self, 'CancQty', Quantity51Choice, False)

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', CancelledStatus12Choice, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', CancelledStatus12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CancQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=CancelledStatus12Choice, min=1, max=1, mutex_group=None, array=False),
	))