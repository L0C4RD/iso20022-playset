# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SearchAnd1

class SearchOr1(base_types._BaseFieldType):

	__slots__ = ["_SchAnd"]
	@property
	def SchAnd(self):
		return self._SchAnd

	@SchAnd.setter
	def SchAnd(self, value):
		self._SchAnd = value if value is not None else base_types.UninitialisedField(self, 'SchAnd', SearchAnd1, True)

	@SchAnd.deleter
	def SchAnd(self):
		del self._SchAnd
		self._SchAnd = base_types.UninitialisedField(self, 'SchAnd', SearchAnd1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchAnd', type=SearchAnd1, min=1, max=None, mutex_group=None, array=True),
	))