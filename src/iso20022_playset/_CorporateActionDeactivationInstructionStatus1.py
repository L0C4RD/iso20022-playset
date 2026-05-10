from . import base_types
from ._CorporateActionDeactivationInstructionRejectionStatus1 import CorporateActionDeactivationInstructionRejectionStatus1
from ._CorporateActionOption1FormatChoice import CorporateActionOption1FormatChoice
from ._Exact3NumericText import Exact3NumericText
from ._CorporateActionDeactivationInstructionProcessingStatus1 import CorporateActionDeactivationInstructionProcessingStatus1

class CorporateActionDeactivationInstructionStatus1(base_types._BaseFieldType):

	__slots__ = ["_OptnNb", "_OptnTp", "_PrcdSts", "_RjctdSts"]
	@property
	def OptnNb(self):
		return self._OptnNb

	@OptnNb.setter
	def OptnNb(self, value):
		self._OptnNb = value if type(value) != base_types.auto else self.make_default("OptnNb")

	@OptnNb.deleter
	def OptnNb(self):
		del self._OptnNb
		self._OptnNb = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if type(value) != base_types.auto else self.make_default("PrcdSts")

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = None

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if type(value) != base_types.auto else self.make_default("RjctdSts")

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcdSts', type=CorporateActionDeactivationInstructionProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionDeactivationInstructionRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
	))

