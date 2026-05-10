from . import base_types
import YesNoIndicator
import SettlementInstruction16

class MissingCover6(base_types._BaseFieldType):

	__slots__ = ["_MssngCoverInd", "_CoverCrrctn"]
	@property
	def MssngCoverInd(self):
		return self._MssngCoverInd

	@MssngCoverInd.setter
	def MssngCoverInd(self, value):
		self._MssngCoverInd = value if type(value) != auto else self.make_default("MssngCoverInd")

	@MssngCoverInd.deleter
	def MssngCoverInd(self):
		del self._MssngCoverInd
		self._MssngCoverInd = None

	@property
	def CoverCrrctn(self):
		return self._CoverCrrctn

	@CoverCrrctn.setter
	def CoverCrrctn(self, value):
		self._CoverCrrctn = value if type(value) != auto else self.make_default("CoverCrrctn")

	@CoverCrrctn.deleter
	def CoverCrrctn(self):
		del self._CoverCrrctn
		self._CoverCrrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MssngCoverInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverCrrctn', type=SettlementInstruction16, min=0, max=1, mutex_group=None, array=False),
	))

