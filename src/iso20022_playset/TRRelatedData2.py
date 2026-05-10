from . import base_types
from .TR34Command1Code import TR34Command1Code
from .Max100KBinary import Max100KBinary

class TRRelatedData2(base_types._BaseFieldType):

	__slots__ = ["_TR34Cmd", "_TRBlck"]
	@property
	def TR34Cmd(self):
		return self._TR34Cmd

	@TR34Cmd.setter
	def TR34Cmd(self, value):
		self._TR34Cmd = value if type(value) != auto else self.make_default("TR34Cmd")

	@TR34Cmd.deleter
	def TR34Cmd(self):
		del self._TR34Cmd
		self._TR34Cmd = None

	@property
	def TRBlck(self):
		return self._TRBlck

	@TRBlck.setter
	def TRBlck(self, value):
		self._TRBlck = value if type(value) != auto else self.make_default("TRBlck")

	@TRBlck.deleter
	def TRBlck(self):
		del self._TRBlck
		self._TRBlck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TR34Cmd', type=TR34Command1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TRBlck', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))

