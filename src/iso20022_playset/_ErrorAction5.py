from . import base_types
from ._TerminalManagementActionResult5Code import TerminalManagementActionResult5Code
from ._TerminalManagementErrorAction2Code import TerminalManagementErrorAction2Code

class ErrorAction5(base_types._BaseFieldType):

	__slots__ = ["_ActnRslt", "_ActnToPrc"]
	@property
	def ActnRslt(self):
		return self._ActnRslt

	@ActnRslt.setter
	def ActnRslt(self, value):
		self._ActnRslt = value if type(value) != base_types.auto else self.make_default("ActnRslt")

	@ActnRslt.deleter
	def ActnRslt(self):
		del self._ActnRslt
		self._ActnRslt = None

	@property
	def ActnToPrc(self):
		return self._ActnToPrc

	@ActnToPrc.setter
	def ActnToPrc(self, value):
		self._ActnToPrc = value if type(value) != base_types.auto else self.make_default("ActnToPrc")

	@ActnToPrc.deleter
	def ActnToPrc(self):
		del self._ActnToPrc
		self._ActnToPrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnRslt', type=TerminalManagementActionResult5Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnToPrc', type=TerminalManagementErrorAction2Code, min=1, max=1, mutex_group=None, array=False),
	))

