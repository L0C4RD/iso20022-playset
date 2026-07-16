# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionDetails1
from . import CorporateActionOption47Choice
from . import Exact3NumericText

class CorporateActionOptionStatement1(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnInstrDtls", "_OptnNb", "_OptnTp"]
	@property
	def BuyrPrtcnInstrDtls(self):
		return self._BuyrPrtcnInstrDtls

	@BuyrPrtcnInstrDtls.setter
	def BuyrPrtcnInstrDtls(self, value):
		self._BuyrPrtcnInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrDtls', BuyerProtectionInstructionDetails1, True)

	@BuyrPrtcnInstrDtls.deleter
	def BuyrPrtcnInstrDtls(self):
		del self._BuyrPrtcnInstrDtls
		self._BuyrPrtcnInstrDtls = base_types.UninitialisedField(self, 'BuyrPrtcnInstrDtls', BuyerProtectionInstructionDetails1, True)

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
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption47Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', CorporateActionOption47Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrPrtcnInstrDtls', type=BuyerProtectionInstructionDetails1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OptnNb', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=CorporateActionOption47Choice, min=1, max=1, mutex_group=None, array=False),
	))