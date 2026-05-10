import base_types
import SettlementStatus16Choice
import ProprietaryReason4
import ProcessingStatus67Choice

class IntraBalanceStatusAndReason2(base_types._BaseFieldType):

	__slots__ = ["_PrcgSts", "_SttlmSts", "_Sttld"]
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
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if type(value) != auto else self.make_default("Sttld")

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus67Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus16Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
	))

