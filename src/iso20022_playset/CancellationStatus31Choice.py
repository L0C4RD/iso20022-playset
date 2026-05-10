import base_types
import DetailedInstructionCancellationStatus15
import CancellationStatus32Choice

class CancellationStatus31Choice(base_types._BaseFieldType):

	__slots__ = ["_GblCxlSts", "_DtldCxlSts"]
	@property
	def GblCxlSts(self):
		return self._GblCxlSts

	@GblCxlSts.setter
	def GblCxlSts(self, value):
		self._GblCxlSts = value if type(value) != auto else self.make_default("GblCxlSts")

	@GblCxlSts.deleter
	def GblCxlSts(self):
		del self._GblCxlSts
		self._GblCxlSts = None

	@property
	def DtldCxlSts(self):
		return self._DtldCxlSts

	@DtldCxlSts.setter
	def DtldCxlSts(self, value):
		self._DtldCxlSts = value if type(value) != auto else self.make_default("DtldCxlSts")

	@DtldCxlSts.deleter
	def DtldCxlSts(self):
		del self._DtldCxlSts
		self._DtldCxlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GblCxlSts', type=CancellationStatus32Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtldCxlSts', type=DetailedInstructionCancellationStatus15, min=1, max=None, mutex_group=1, array=True),
	))

