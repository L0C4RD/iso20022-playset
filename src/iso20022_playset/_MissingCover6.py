# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementInstruction16
from . import YesNoIndicator

class MissingCover6(base_types._BaseFieldType):

	__slots__ = ["_CoverCrrctn", "_MssngCoverInd"]
	@property
	def CoverCrrctn(self):
		return self._CoverCrrctn

	@CoverCrrctn.setter
	def CoverCrrctn(self, value):
		self._CoverCrrctn = value if value is not None else base_types.UninitialisedField(self, 'CoverCrrctn', SettlementInstruction16, False)

	@CoverCrrctn.deleter
	def CoverCrrctn(self):
		del self._CoverCrrctn
		self._CoverCrrctn = base_types.UninitialisedField(self, 'CoverCrrctn', SettlementInstruction16, False)

	@property
	def MssngCoverInd(self):
		return self._MssngCoverInd

	@MssngCoverInd.setter
	def MssngCoverInd(self, value):
		self._MssngCoverInd = value if value is not None else base_types.UninitialisedField(self, 'MssngCoverInd', YesNoIndicator, False)

	@MssngCoverInd.deleter
	def MssngCoverInd(self):
		del self._MssngCoverInd
		self._MssngCoverInd = base_types.UninitialisedField(self, 'MssngCoverInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoverCrrctn', type=SettlementInstruction16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MssngCoverInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))