# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TerminalManagementActionResult5Code
from . import TerminalManagementErrorAction2Code

class ErrorAction5(base_types._BaseFieldType):

	__slots__ = ["_ActnRslt", "_ActnToPrc"]
	@property
	def ActnRslt(self):
		return self._ActnRslt

	@ActnRslt.setter
	def ActnRslt(self, value):
		self._ActnRslt = value if value is not None else base_types.UninitialisedField(self, 'ActnRslt', TerminalManagementActionResult5Code, True)

	@ActnRslt.deleter
	def ActnRslt(self):
		del self._ActnRslt
		self._ActnRslt = base_types.UninitialisedField(self, 'ActnRslt', TerminalManagementActionResult5Code, True)

	@property
	def ActnToPrc(self):
		return self._ActnToPrc

	@ActnToPrc.setter
	def ActnToPrc(self, value):
		self._ActnToPrc = value if value is not None else base_types.UninitialisedField(self, 'ActnToPrc', TerminalManagementErrorAction2Code, False)

	@ActnToPrc.deleter
	def ActnToPrc(self):
		del self._ActnToPrc
		self._ActnToPrc = base_types.UninitialisedField(self, 'ActnToPrc', TerminalManagementErrorAction2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnRslt', type=TerminalManagementActionResult5Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnToPrc', type=TerminalManagementErrorAction2Code, min=1, max=1, mutex_group=None, array=False),
	))