# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text

class AdditionalInformation24(base_types._BaseFieldType):

	__slots__ = ["_CollInstr", "_Note"]
	@property
	def CollInstr(self):
		return self._CollInstr

	@CollInstr.setter
	def CollInstr(self, value):
		self._CollInstr = value if value is not None else base_types.UninitialisedField(self, 'CollInstr', Max350Text, False)

	@CollInstr.deleter
	def CollInstr(self):
		del self._CollInstr
		self._CollInstr = base_types.UninitialisedField(self, 'CollInstr', Max350Text, False)

	@property
	def Note(self):
		return self._Note

	@Note.setter
	def Note(self, value):
		self._Note = value if value is not None else base_types.UninitialisedField(self, 'Note', Max350Text, False)

	@Note.deleter
	def Note(self):
		del self._Note
		self._Note = base_types.UninitialisedField(self, 'Note', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollInstr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Note', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))