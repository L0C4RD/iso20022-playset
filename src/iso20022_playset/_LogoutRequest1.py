# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TrueFalseIndicator

class LogoutRequest1(base_types._BaseFieldType):

	__slots__ = ["_MntncAllwd"]
	@property
	def MntncAllwd(self):
		return self._MntncAllwd

	@MntncAllwd.setter
	def MntncAllwd(self, value):
		self._MntncAllwd = value if value is not None else base_types.UninitialisedField(self, 'MntncAllwd', TrueFalseIndicator, False)

	@MntncAllwd.deleter
	def MntncAllwd(self):
		del self._MntncAllwd
		self._MntncAllwd = base_types.UninitialisedField(self, 'MntncAllwd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MntncAllwd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))