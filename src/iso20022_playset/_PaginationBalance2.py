# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosingBalance3Choice
from . import OpeningBalance3Choice

class PaginationBalance2(base_types._BaseFieldType):

	__slots__ = ["_ClsgBal", "_OpngBal"]
	@property
	def ClsgBal(self):
		return self._ClsgBal

	@ClsgBal.setter
	def ClsgBal(self, value):
		self._ClsgBal = value if value is not None else base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance3Choice, False)

	@ClsgBal.deleter
	def ClsgBal(self):
		del self._ClsgBal
		self._ClsgBal = base_types.UninitialisedField(self, 'ClsgBal', ClosingBalance3Choice, False)

	@property
	def OpngBal(self):
		return self._OpngBal

	@OpngBal.setter
	def OpngBal(self, value):
		self._OpngBal = value if value is not None else base_types.UninitialisedField(self, 'OpngBal', OpeningBalance3Choice, False)

	@OpngBal.deleter
	def OpngBal(self):
		del self._OpngBal
		self._OpngBal = base_types.UninitialisedField(self, 'OpngBal', OpeningBalance3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgBal', type=ClosingBalance3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngBal', type=OpeningBalance3Choice, min=0, max=1, mutex_group=None, array=False),
	))