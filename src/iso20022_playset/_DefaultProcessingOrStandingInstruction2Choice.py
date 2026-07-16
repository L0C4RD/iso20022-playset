# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import YesNoIndicator

class DefaultProcessingOrStandingInstruction2Choice(base_types._BaseFieldType):

	__slots__ = ["_DfltOptnInd", "_StgInstrInd"]
	@property
	def DfltOptnInd(self):
		return self._DfltOptnInd

	@DfltOptnInd.setter
	def DfltOptnInd(self, value):
		self._DfltOptnInd = value if value is not None else base_types.UninitialisedField(self, 'DfltOptnInd', YesNoIndicator, False)

	@DfltOptnInd.deleter
	def DfltOptnInd(self):
		del self._DfltOptnInd
		self._DfltOptnInd = base_types.UninitialisedField(self, 'DfltOptnInd', YesNoIndicator, False)

	@property
	def StgInstrInd(self):
		return self._StgInstrInd

	@StgInstrInd.setter
	def StgInstrInd(self, value):
		self._StgInstrInd = value if value is not None else base_types.UninitialisedField(self, 'StgInstrInd', YesNoIndicator, False)

	@StgInstrInd.deleter
	def StgInstrInd(self):
		del self._StgInstrInd
		self._StgInstrInd = base_types.UninitialisedField(self, 'StgInstrInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltOptnInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StgInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))