# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BytePadding1Code
from . import Max500Binary

class Parameter7(base_types._BaseFieldType):

	__slots__ = ["_BPddg", "_InitlstnVctr"]
	@property
	def BPddg(self):
		return self._BPddg

	@BPddg.setter
	def BPddg(self, value):
		self._BPddg = value if value is not None else base_types.UninitialisedField(self, 'BPddg', BytePadding1Code, False)

	@BPddg.deleter
	def BPddg(self):
		del self._BPddg
		self._BPddg = base_types.UninitialisedField(self, 'BPddg', BytePadding1Code, False)

	@property
	def InitlstnVctr(self):
		return self._InitlstnVctr

	@InitlstnVctr.setter
	def InitlstnVctr(self, value):
		self._InitlstnVctr = value if value is not None else base_types.UninitialisedField(self, 'InitlstnVctr', Max500Binary, False)

	@InitlstnVctr.deleter
	def InitlstnVctr(self):
		del self._InitlstnVctr
		self._InitlstnVctr = base_types.UninitialisedField(self, 'InitlstnVctr', Max500Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BPddg', type=BytePadding1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlstnVctr', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
	))