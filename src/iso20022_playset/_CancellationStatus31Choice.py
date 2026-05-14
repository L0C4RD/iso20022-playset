# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CancellationStatus32Choice import CancellationStatus32Choice
from ._DetailedInstructionCancellationStatus15 import DetailedInstructionCancellationStatus15

class CancellationStatus31Choice(base_types._BaseFieldType):

	__slots__ = ["_DtldCxlSts", "_GblCxlSts"]
	@property
	def DtldCxlSts(self):
		return self._DtldCxlSts

	@DtldCxlSts.setter
	def DtldCxlSts(self, value):
		self._DtldCxlSts = value if type(value) != base_types.auto else self.make_default("DtldCxlSts")

	@DtldCxlSts.deleter
	def DtldCxlSts(self):
		del self._DtldCxlSts
		self._DtldCxlSts = None

	@property
	def GblCxlSts(self):
		return self._GblCxlSts

	@GblCxlSts.setter
	def GblCxlSts(self, value):
		self._GblCxlSts = value if type(value) != base_types.auto else self.make_default("GblCxlSts")

	@GblCxlSts.deleter
	def GblCxlSts(self):
		del self._GblCxlSts
		self._GblCxlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldCxlSts', type=DetailedInstructionCancellationStatus15, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='GblCxlSts', type=CancellationStatus32Choice, min=0, max=1, mutex_group=1, array=False),
	))