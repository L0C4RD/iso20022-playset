# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyIn4
from . import Max35Text
from . import PartyIdentification35Choice
from . import SettlementObligation7
from . import SupplementaryData1

class BuyInNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_NtfctnDtls", "_OrgnlSttlmOblgtn", "_SplmtryData", "_TxId"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification35Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification35Choice, False)

	@property
	def NtfctnDtls(self):
		return self._NtfctnDtls

	@NtfctnDtls.setter
	def NtfctnDtls(self, value):
		self._NtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'NtfctnDtls', BuyIn4, False)

	@NtfctnDtls.deleter
	def NtfctnDtls(self):
		del self._NtfctnDtls
		self._NtfctnDtls = base_types.UninitialisedField(self, 'NtfctnDtls', BuyIn4, False)

	@property
	def OrgnlSttlmOblgtn(self):
		return self._OrgnlSttlmOblgtn

	@OrgnlSttlmOblgtn.setter
	def OrgnlSttlmOblgtn(self, value):
		self._OrgnlSttlmOblgtn = value if value is not None else base_types.UninitialisedField(self, 'OrgnlSttlmOblgtn', SettlementObligation7, False)

	@OrgnlSttlmOblgtn.deleter
	def OrgnlSttlmOblgtn(self):
		del self._OrgnlSttlmOblgtn
		self._OrgnlSttlmOblgtn = base_types.UninitialisedField(self, 'OrgnlSttlmOblgtn', SettlementObligation7, False)

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
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnDtls', type=BuyIn4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSttlmOblgtn', type=SettlementObligation7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))