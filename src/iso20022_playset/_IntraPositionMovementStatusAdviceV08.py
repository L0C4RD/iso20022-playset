# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionDetails60
from . import IntraPositionProcessingStatus9Choice
from . import Linkages75
from . import SettlementStatus16Choice
from . import SupplementaryData1
from . import TransactionIdentifications29

class IntraPositionMovementStatusAdviceV08(base_types._BaseFieldType):

	__slots__ = ["_Lkg", "_PrcgSts", "_SplmtryData", "_SttlmSts", "_TxDtls", "_TxId"]
	@property
	def Lkg(self):
		return self._Lkg

	@Lkg.setter
	def Lkg(self, value):
		self._Lkg = value if value is not None else base_types.UninitialisedField(self, 'Lkg', Linkages75, False)

	@Lkg.deleter
	def Lkg(self):
		del self._Lkg
		self._Lkg = base_types.UninitialisedField(self, 'Lkg', Linkages75, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', IntraPositionProcessingStatus9Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', IntraPositionProcessingStatus9Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus16Choice, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus16Choice, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', IntraPositionDetails60, False)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', IntraPositionDetails60, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifications29, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifications29, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lkg', type=Linkages75, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=IntraPositionProcessingStatus9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus16Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=IntraPositionDetails60, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications29, min=1, max=1, mutex_group=None, array=False),
	))