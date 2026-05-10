import base_types
import DetailedInstructionStatus21
import CancellationStatus31Choice

class InstructionTypeStatus7Choice(base_types._BaseFieldType):

	__slots__ = ["_InstrSts", "_CxlSts"]
	@property
	def InstrSts(self):
		return self._InstrSts

	@InstrSts.setter
	def InstrSts(self, value):
		self._InstrSts = value if type(value) != auto else self.make_default("InstrSts")

	@InstrSts.deleter
	def InstrSts(self):
		del self._InstrSts
		self._InstrSts = None

	@property
	def CxlSts(self):
		return self._CxlSts

	@CxlSts.setter
	def CxlSts(self, value):
		self._CxlSts = value if type(value) != auto else self.make_default("CxlSts")

	@CxlSts.deleter
	def CxlSts(self):
		del self._CxlSts
		self._CxlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrSts', type=DetailedInstructionStatus21, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='CxlSts', type=CancellationStatus31Choice, min=0, max=1, mutex_group=1, array=False),
	))

