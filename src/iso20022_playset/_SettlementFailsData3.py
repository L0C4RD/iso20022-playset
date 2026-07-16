# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementDataVolume2
from . import SettlementFailsCurrency2
from . import SettlementFailsInstrument2
from . import SettlementFailsParticipantRange1
from . import SettlementFailsSecuritiesRange1
from . import SettlementFailsTransactionType2
from . import SettlementFailureReason3
from . import SettlementTotalData1

class SettlementFailsData3(base_types._BaseFieldType):

	__slots__ = ["_FailrRsn", "_FlsPerCcy", "_FlsPerFinInstrmTp", "_FlsPerTxTp", "_PtcptInFail", "_SctiesInFail", "_Ttl", "_TtlSttlmPnlties"]
	@property
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if value is not None else base_types.UninitialisedField(self, 'FailrRsn', SettlementFailureReason3, False)

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = base_types.UninitialisedField(self, 'FailrRsn', SettlementFailureReason3, False)

	@property
	def FlsPerCcy(self):
		return self._FlsPerCcy

	@FlsPerCcy.setter
	def FlsPerCcy(self, value):
		self._FlsPerCcy = value if value is not None else base_types.UninitialisedField(self, 'FlsPerCcy', SettlementFailsCurrency2, True)

	@FlsPerCcy.deleter
	def FlsPerCcy(self):
		del self._FlsPerCcy
		self._FlsPerCcy = base_types.UninitialisedField(self, 'FlsPerCcy', SettlementFailsCurrency2, True)

	@property
	def FlsPerFinInstrmTp(self):
		return self._FlsPerFinInstrmTp

	@FlsPerFinInstrmTp.setter
	def FlsPerFinInstrmTp(self, value):
		self._FlsPerFinInstrmTp = value if value is not None else base_types.UninitialisedField(self, 'FlsPerFinInstrmTp', SettlementFailsInstrument2, False)

	@FlsPerFinInstrmTp.deleter
	def FlsPerFinInstrmTp(self):
		del self._FlsPerFinInstrmTp
		self._FlsPerFinInstrmTp = base_types.UninitialisedField(self, 'FlsPerFinInstrmTp', SettlementFailsInstrument2, False)

	@property
	def FlsPerTxTp(self):
		return self._FlsPerTxTp

	@FlsPerTxTp.setter
	def FlsPerTxTp(self, value):
		self._FlsPerTxTp = value if value is not None else base_types.UninitialisedField(self, 'FlsPerTxTp', SettlementFailsTransactionType2, False)

	@FlsPerTxTp.deleter
	def FlsPerTxTp(self):
		del self._FlsPerTxTp
		self._FlsPerTxTp = base_types.UninitialisedField(self, 'FlsPerTxTp', SettlementFailsTransactionType2, False)

	@property
	def PtcptInFail(self):
		return self._PtcptInFail

	@PtcptInFail.setter
	def PtcptInFail(self, value):
		self._PtcptInFail = value if value is not None else base_types.UninitialisedField(self, 'PtcptInFail', SettlementFailsParticipantRange1, False)

	@PtcptInFail.deleter
	def PtcptInFail(self):
		del self._PtcptInFail
		self._PtcptInFail = base_types.UninitialisedField(self, 'PtcptInFail', SettlementFailsParticipantRange1, False)

	@property
	def SctiesInFail(self):
		return self._SctiesInFail

	@SctiesInFail.setter
	def SctiesInFail(self, value):
		self._SctiesInFail = value if value is not None else base_types.UninitialisedField(self, 'SctiesInFail', SettlementFailsSecuritiesRange1, False)

	@SctiesInFail.deleter
	def SctiesInFail(self):
		del self._SctiesInFail
		self._SctiesInFail = base_types.UninitialisedField(self, 'SctiesInFail', SettlementFailsSecuritiesRange1, False)

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if value is not None else base_types.UninitialisedField(self, 'Ttl', SettlementTotalData1, False)

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = base_types.UninitialisedField(self, 'Ttl', SettlementTotalData1, False)

	@property
	def TtlSttlmPnlties(self):
		return self._TtlSttlmPnlties

	@TtlSttlmPnlties.setter
	def TtlSttlmPnlties(self, value):
		self._TtlSttlmPnlties = value if value is not None else base_types.UninitialisedField(self, 'TtlSttlmPnlties', SettlementDataVolume2, False)

	@TtlSttlmPnlties.deleter
	def TtlSttlmPnlties(self):
		del self._TtlSttlmPnlties
		self._TtlSttlmPnlties = base_types.UninitialisedField(self, 'TtlSttlmPnlties', SettlementDataVolume2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FailrRsn', type=SettlementFailureReason3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsPerCcy', type=SettlementFailsCurrency2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FlsPerFinInstrmTp', type=SettlementFailsInstrument2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlsPerTxTp', type=SettlementFailsTransactionType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptInFail', type=SettlementFailsParticipantRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesInFail', type=SettlementFailsSecuritiesRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmPnlties', type=SettlementDataVolume2, min=0, max=1, mutex_group=None, array=False),
	))