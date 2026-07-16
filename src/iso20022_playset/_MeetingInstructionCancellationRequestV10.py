# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelInstruction5
from . import Max35Text
from . import MeetingReference10
from . import SecurityIdentification19
from . import SupplementaryData1

class MeetingInstructionCancellationRequestV10(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_MtgInstrId", "_MtgRef", "_SplmtryData", "_ToBeCancInstr"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def MtgInstrId(self):
		return self._MtgInstrId

	@MtgInstrId.setter
	def MtgInstrId(self, value):
		self._MtgInstrId = value if value is not None else base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

	@MtgInstrId.deleter
	def MtgInstrId(self):
		del self._MtgInstrId
		self._MtgInstrId = base_types.UninitialisedField(self, 'MtgInstrId', Max35Text, False)

	@property
	def MtgRef(self):
		return self._MtgRef

	@MtgRef.setter
	def MtgRef(self, value):
		self._MtgRef = value if value is not None else base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@MtgRef.deleter
	def MtgRef(self):
		del self._MtgRef
		self._MtgRef = base_types.UninitialisedField(self, 'MtgRef', MeetingReference10, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def ToBeCancInstr(self):
		return self._ToBeCancInstr

	@ToBeCancInstr.setter
	def ToBeCancInstr(self, value):
		self._ToBeCancInstr = value if value is not None else base_types.UninitialisedField(self, 'ToBeCancInstr', CancelInstruction5, True)

	@ToBeCancInstr.deleter
	def ToBeCancInstr(self):
		del self._ToBeCancInstr
		self._ToBeCancInstr = base_types.UninitialisedField(self, 'ToBeCancInstr', CancelInstruction5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgRef', type=MeetingReference10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ToBeCancInstr', type=CancelInstruction5, min=0, max=None, mutex_group=None, array=True),
	))