# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InstructionProcessingStatus63Choice import InstructionProcessingStatus63Choice
from ._MatchingStatus24Choice import MatchingStatus24Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6
from ._SettlementStatus32Choice import SettlementStatus32Choice

class StatusAndReason52(base_types._BaseFieldType):

	__slots__ = ["_IfrrdMtchgSts", "_InstrPrcgSts", "_MtchgSts", "_Prtry", "_Sttld", "_SttlmSts"]
	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if type(value) != base_types.auto else self.make_default("IfrrdMtchgSts")

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = None

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if type(value) != base_types.auto else self.make_default("InstrPrcgSts")

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != base_types.auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != base_types.auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != base_types.auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus63Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus32Choice, min=0, max=1, mutex_group=None, array=False),
	))