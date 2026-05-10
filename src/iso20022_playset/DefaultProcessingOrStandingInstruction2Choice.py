from . import base_types
import YesNoIndicator

class DefaultProcessingOrStandingInstruction2Choice(base_types._BaseFieldType):

	__slots__ = ["_DfltOptnInd", "_StgInstrInd"]
	@property
	def DfltOptnInd(self):
		return self._DfltOptnInd

	@DfltOptnInd.setter
	def DfltOptnInd(self, value):
		self._DfltOptnInd = value if type(value) != auto else self.make_default("DfltOptnInd")

	@DfltOptnInd.deleter
	def DfltOptnInd(self):
		del self._DfltOptnInd
		self._DfltOptnInd = None

	@property
	def StgInstrInd(self):
		return self._StgInstrInd

	@StgInstrInd.setter
	def StgInstrInd(self, value):
		self._StgInstrInd = value if type(value) != auto else self.make_default("StgInstrInd")

	@StgInstrInd.deleter
	def StgInstrInd(self):
		del self._StgInstrInd
		self._StgInstrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltOptnInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))

