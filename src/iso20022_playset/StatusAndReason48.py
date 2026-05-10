from . import base_types
import ProcessingStatus52Choice
import MatchingStatus24Choice
import SettlementStatus32Choice

class StatusAndReason48(base_types._BaseFieldType):

	__slots__ = ["_SttlmSts", "_MtchgSts", "_PrcgSts", "_IfrrdMtchgSts"]
	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if type(value) != auto else self.make_default("IfrrdMtchgSts")

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus52Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus24Choice, min=0, max=1, mutex_group=None, array=False),
	))

