from . import base_types
from .SettlementDataVolume2 import SettlementDataVolume2
from .SettlementFailsCurrency2 import SettlementFailsCurrency2
from .SettlementFailsSecuritiesRange1 import SettlementFailsSecuritiesRange1
from .SettlementFailsParticipantRange1 import SettlementFailsParticipantRange1
from .SettlementTotalData1 import SettlementTotalData1
from .SettlementFailureReason3 import SettlementFailureReason3
from .SettlementFailsTransactionType2 import SettlementFailsTransactionType2
from .SettlementFailsInstrument2 import SettlementFailsInstrument2

class SettlementFailsData3(base_types._BaseFieldType):

	__slots__ = ["_Ttl", "_TtlSttlmPnlties", "_FlsPerTxTp", "_SctiesInFail", "_FailrRsn", "_FlsPerFinInstrmTp", "_PtcptInFail", "_FlsPerCcy"]
	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if type(value) != base_types.auto else self.make_default("Ttl")

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = None

	@property
	def TtlSttlmPnlties(self):
		return self._TtlSttlmPnlties

	@TtlSttlmPnlties.setter
	def TtlSttlmPnlties(self, value):
		self._TtlSttlmPnlties = value if type(value) != base_types.auto else self.make_default("TtlSttlmPnlties")

	@TtlSttlmPnlties.deleter
	def TtlSttlmPnlties(self):
		del self._TtlSttlmPnlties
		self._TtlSttlmPnlties = None

	@property
	def FlsPerTxTp(self):
		return self._FlsPerTxTp

	@FlsPerTxTp.setter
	def FlsPerTxTp(self, value):
		self._FlsPerTxTp = value if type(value) != base_types.auto else self.make_default("FlsPerTxTp")

	@FlsPerTxTp.deleter
	def FlsPerTxTp(self):
		del self._FlsPerTxTp
		self._FlsPerTxTp = None

	@property
	def SctiesInFail(self):
		return self._SctiesInFail

	@SctiesInFail.setter
	def SctiesInFail(self, value):
		self._SctiesInFail = value if type(value) != base_types.auto else self.make_default("SctiesInFail")

	@SctiesInFail.deleter
	def SctiesInFail(self):
		del self._SctiesInFail
		self._SctiesInFail = None

	@property
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if type(value) != base_types.auto else self.make_default("FailrRsn")

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = None

	@property
	def FlsPerFinInstrmTp(self):
		return self._FlsPerFinInstrmTp

	@FlsPerFinInstrmTp.setter
	def FlsPerFinInstrmTp(self, value):
		self._FlsPerFinInstrmTp = value if type(value) != base_types.auto else self.make_default("FlsPerFinInstrmTp")

	@FlsPerFinInstrmTp.deleter
	def FlsPerFinInstrmTp(self):
		del self._FlsPerFinInstrmTp
		self._FlsPerFinInstrmTp = None

	@property
	def PtcptInFail(self):
		return self._PtcptInFail

	@PtcptInFail.setter
	def PtcptInFail(self, value):
		self._PtcptInFail = value if type(value) != base_types.auto else self.make_default("PtcptInFail")

	@PtcptInFail.deleter
	def PtcptInFail(self):
		del self._PtcptInFail
		self._PtcptInFail = None

	@property
	def FlsPerCcy(self):
		return self._FlsPerCcy

	@FlsPerCcy.setter
	def FlsPerCcy(self, value):
		self._FlsPerCcy = value if type(value) != base_types.auto else self.make_default("FlsPerCcy")

	@FlsPerCcy.deleter
	def FlsPerCcy(self):
		del self._FlsPerCcy
		self._FlsPerCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ttl', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmPnlties', type=SettlementDataVolume2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsPerTxTp', type=SettlementFailsTransactionType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesInFail', type=SettlementFailsSecuritiesRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=SettlementFailureReason3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsPerFinInstrmTp', type=SettlementFailsInstrument2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptInFail', type=SettlementFailsParticipantRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsPerCcy', type=SettlementFailsCurrency2, min=0, max=None, mutex_group=None, array=True),
	))

