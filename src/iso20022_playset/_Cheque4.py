# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NameAndAddress5

class Cheque4(base_types._BaseFieldType):

	__slots__ = ["_PyeeId"]
	@property
	def PyeeId(self):
		return self._PyeeId

	@PyeeId.setter
	def PyeeId(self, value):
		self._PyeeId = value if value is not None else base_types.UninitialisedField(self, 'PyeeId', NameAndAddress5, False)

	@PyeeId.deleter
	def PyeeId(self):
		del self._PyeeId
		self._PyeeId = base_types.UninitialisedField(self, 'PyeeId', NameAndAddress5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyeeId', type=NameAndAddress5, min=1, max=1, mutex_group=None, array=False),
	))