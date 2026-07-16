# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SearchOr1

class SearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_SchOr"]
	@property
	def SchOr(self):
		return self._SchOr

	@SchOr.setter
	def SchOr(self, value):
		self._SchOr = value if value is not None else base_types.UninitialisedField(self, 'SchOr', SearchOr1, True)

	@SchOr.deleter
	def SchOr(self):
		del self._SchOr
		self._SchOr = base_types.UninitialisedField(self, 'SchOr', SearchOr1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchOr', type=SearchOr1, min=1, max=None, mutex_group=None, array=True),
	))