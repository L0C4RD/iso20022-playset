# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InstructionProcessingStatus45Choice import InstructionProcessingStatus45Choice
from ._MatchingStatus32Choice import MatchingStatus32Choice
from ._ProprietaryStatusAndReason7 import ProprietaryStatusAndReason7
from ._SettlementStatus31Choice import SettlementStatus31Choice

class Status39Choice(base_types._BaseFieldType):

	__slots__ = ["_IfrrdMtchgSts", "_InstrPrcgSts", "_MtchgSts", "_Prtry", "_SttlmSts"]
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
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus32Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus45Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus32Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus31Choice, min=0, max=1, mutex_group=1, array=False),
	))