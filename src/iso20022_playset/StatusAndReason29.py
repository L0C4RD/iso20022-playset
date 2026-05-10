import base_types
import MatchingStatus32Choice
import ProcessingStatus62Choice
import SettlementStatus22Choice

class StatusAndReason29(base_types._BaseFieldType):

	__slots__ = ["_SttlmSts", "_MtchgSts", "_IfrrdMtchgSts", "_PrcgSts"]
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
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if type(value) != auto else self.make_default("IfrrdMtchgSts")

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus62Choice, min=0, max=1, mutex_group=None, array=False),
	))

