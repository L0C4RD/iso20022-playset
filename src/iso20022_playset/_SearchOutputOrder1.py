# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CriteriaOrder1

class SearchOutputOrder1(base_types._BaseFieldType):

	__slots__ = ["_CritOrdr"]
	@property
	def CritOrdr(self):
		return self._CritOrdr

	@CritOrdr.setter
	def CritOrdr(self, value):
		self._CritOrdr = value if value is not None else base_types.UninitialisedField(self, 'CritOrdr', CriteriaOrder1, True)

	@CritOrdr.deleter
	def CritOrdr(self):
		del self._CritOrdr
		self._CritOrdr = base_types.UninitialisedField(self, 'CritOrdr', CriteriaOrder1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CritOrdr', type=CriteriaOrder1, min=1, max=None, mutex_group=None, array=True),
	))