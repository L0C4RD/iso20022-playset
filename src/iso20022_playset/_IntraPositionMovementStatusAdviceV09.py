# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionDetails60 import IntraPositionDetails60
from ._IntraPositionProcessingStatus11Choice import IntraPositionProcessingStatus11Choice
from ._Linkages75 import Linkages75
from ._SettlementStatus34Choice import SettlementStatus34Choice
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionIdentifications29 import TransactionIdentifications29

class IntraPositionMovementStatusAdviceV09(base_types._BaseFieldType):

	__slots__ = ["_Lkg", "_PrcgSts", "_SplmtryData", "_SttlmSts", "_TxDtls", "_TxId"]
	@property
	def Lkg(self):
		return self._Lkg

	@Lkg.setter
	def Lkg(self, value):
		self._Lkg = value if type(value) != base_types.auto else self.make_default("Lkg")

	@Lkg.deleter
	def Lkg(self):
		del self._Lkg
		self._Lkg = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

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

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lkg', type=Linkages75, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=IntraPositionProcessingStatus11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=IntraPositionDetails60, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications29, min=1, max=1, mutex_group=None, array=False),
	))