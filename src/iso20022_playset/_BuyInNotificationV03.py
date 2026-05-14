# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyIn4 import BuyIn4
from ._Max35Text import Max35Text
from ._PartyIdentification35Choice import PartyIdentification35Choice
from ._SettlementObligation7 import SettlementObligation7
from ._SupplementaryData1 import SupplementaryData1

class BuyInNotificationV03(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_NtfctnDtls", "_OrgnlSttlmOblgtn", "_SplmtryData", "_TxId"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def NtfctnDtls(self):
		return self._NtfctnDtls

	@NtfctnDtls.setter
	def NtfctnDtls(self, value):
		self._NtfctnDtls = value if type(value) != base_types.auto else self.make_default("NtfctnDtls")

	@NtfctnDtls.deleter
	def NtfctnDtls(self):
		del self._NtfctnDtls
		self._NtfctnDtls = None

	@property
	def OrgnlSttlmOblgtn(self):
		return self._OrgnlSttlmOblgtn

	@OrgnlSttlmOblgtn.setter
	def OrgnlSttlmOblgtn(self, value):
		self._OrgnlSttlmOblgtn = value if type(value) != base_types.auto else self.make_default("OrgnlSttlmOblgtn")

	@OrgnlSttlmOblgtn.deleter
	def OrgnlSttlmOblgtn(self):
		del self._OrgnlSttlmOblgtn
		self._OrgnlSttlmOblgtn = None

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
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnDtls', type=BuyIn4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSttlmOblgtn', type=SettlementObligation7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))