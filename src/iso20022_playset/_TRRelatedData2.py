# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100KBinary
from . import TR34Command1Code

class TRRelatedData2(base_types._BaseFieldType):

	__slots__ = ["_TR34Cmd", "_TRBlck"]
	@property
	def TR34Cmd(self):
		return self._TR34Cmd

	@TR34Cmd.setter
	def TR34Cmd(self, value):
		self._TR34Cmd = value if value is not None else base_types.UninitialisedField(self, 'TR34Cmd', TR34Command1Code, False)

	@TR34Cmd.deleter
	def TR34Cmd(self):
		del self._TR34Cmd
		self._TR34Cmd = base_types.UninitialisedField(self, 'TR34Cmd', TR34Command1Code, False)

	@property
	def TRBlck(self):
		return self._TRBlck

	@TRBlck.setter
	def TRBlck(self, value):
		self._TRBlck = value if value is not None else base_types.UninitialisedField(self, 'TRBlck', Max100KBinary, False)

	@TRBlck.deleter
	def TRBlck(self):
		del self._TRBlck
		self._TRBlck = base_types.UninitialisedField(self, 'TRBlck', Max100KBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TR34Cmd', type=TR34Command1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TRBlck', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))