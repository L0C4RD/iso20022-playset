from . import base_types
from .Max350Text import Max350Text

class AdditionalInformation24(base_types._BaseFieldType):

	__slots__ = ["_Note", "_CollInstr"]
	@property
	def Note(self):
		return self._Note

	@Note.setter
	def Note(self, value):
		self._Note = value if type(value) != base_types.auto else self.make_default("Note")

	@Note.deleter
	def Note(self):
		del self._Note
		self._Note = None

	@property
	def CollInstr(self):
		return self._CollInstr

	@CollInstr.setter
	def CollInstr(self, value):
		self._CollInstr = value if type(value) != base_types.auto else self.make_default("CollInstr")

	@CollInstr.deleter
	def CollInstr(self):
		del self._CollInstr
		self._CollInstr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Note', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollInstr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

