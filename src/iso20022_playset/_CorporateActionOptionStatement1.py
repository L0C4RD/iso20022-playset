from . import base_types
from ._BuyerProtectionInstructionDetails1 import BuyerProtectionInstructionDetails1
from ._CorporateActionOption47Choice import CorporateActionOption47Choice
from ._Exact3NumericText import Exact3NumericText

class CorporateActionOptionStatement1(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnInstrDtls", "_OptnNb", "_OptnTp"]
	@property
	def BuyrPrtcnInstrDtls(self):
		return self._BuyrPrtcnInstrDtls

	@BuyrPrtcnInstrDtls.setter
	def BuyrPrtcnInstrDtls(self, value):
		self._BuyrPrtcnInstrDtls = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrDtls")

	@BuyrPrtcnInstrDtls.deleter
	def BuyrPrtcnInstrDtls(self):
		del self._BuyrPrtcnInstrDtls
		self._BuyrPrtcnInstrDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrPrtcnInstrDtls', type=BuyerProtectionInstructionDetails1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption47Choice, min=1, max=1, mutex_group=None, array=False),
	))

