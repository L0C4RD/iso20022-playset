# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionDeactivationInstructionProcessingStatus1
from . import CorporateActionDeactivationInstructionRejectionStatus1
from . import CorporateActionOption1FormatChoice
from . import Exact3NumericText

class CorporateActionDeactivationInstructionStatus1(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_OptnTp", "_PrcdSts", "_RjctdSts"]
	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if value is not None else base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = base_types.UninitialisedField(self, 'OptnNb', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption1FormatChoice, False)

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if value is not None else base_types.UninitialisedField(self, 'PrcdSts', CorporateActionDeactivationInstructionProcessingStatus1, False)

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = base_types.UninitialisedField(self, 'PrcdSts', CorporateActionDeactivationInstructionProcessingStatus1, False)

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if value is not None else base_types.UninitialisedField(self, 'RjctdSts', CorporateActionDeactivationInstructionRejectionStatus1, False)

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = base_types.UninitialisedField(self, 'RjctdSts', CorporateActionDeactivationInstructionRejectionStatus1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdSts', type=CorporateActionDeactivationInstructionProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionDeactivationInstructionRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
	))