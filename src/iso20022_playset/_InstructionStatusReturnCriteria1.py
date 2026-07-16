# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class InstructionStatusReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrStsDtTmInd", "_PmtInstrStsInd", "_PmtInstrStsRsnInd"]
	@property
	def PmtInstrStsDtTmInd(self):
		return self._PmtInstrStsDtTmInd

	@PmtInstrStsDtTmInd.setter
	def PmtInstrStsDtTmInd(self, value):
		self._PmtInstrStsDtTmInd = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrStsDtTmInd', RequestedIndicator, False)

	@PmtInstrStsDtTmInd.deleter
	def PmtInstrStsDtTmInd(self):
		del self._PmtInstrStsDtTmInd
		self._PmtInstrStsDtTmInd = base_types.UninitialisedField(self, 'PmtInstrStsDtTmInd', RequestedIndicator, False)

	@property
	def PmtInstrStsInd(self):
		return self._PmtInstrStsInd

	@PmtInstrStsInd.setter
	def PmtInstrStsInd(self, value):
		self._PmtInstrStsInd = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrStsInd', RequestedIndicator, False)

	@PmtInstrStsInd.deleter
	def PmtInstrStsInd(self):
		del self._PmtInstrStsInd
		self._PmtInstrStsInd = base_types.UninitialisedField(self, 'PmtInstrStsInd', RequestedIndicator, False)

	@property
	def PmtInstrStsRsnInd(self):
		return self._PmtInstrStsRsnInd

	@PmtInstrStsRsnInd.setter
	def PmtInstrStsRsnInd(self, value):
		self._PmtInstrStsRsnInd = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrStsRsnInd', RequestedIndicator, False)

	@PmtInstrStsRsnInd.deleter
	def PmtInstrStsRsnInd(self):
		del self._PmtInstrStsRsnInd
		self._PmtInstrStsRsnInd = base_types.UninitialisedField(self, 'PmtInstrStsRsnInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrStsDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrStsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrStsRsnInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))