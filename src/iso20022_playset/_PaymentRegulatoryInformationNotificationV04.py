# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyControlHeader9
from . import RegulatoryReportingNotification4
from . import SupplementaryData1

class PaymentRegulatoryInformationNotificationV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_TxNtfctn"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader9, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', CurrencyControlHeader9, False)

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
	def TxNtfctn(self):
		return self._TxNtfctn

	@TxNtfctn.setter
	def TxNtfctn(self, value):
		self._TxNtfctn = value if value is not None else base_types.UninitialisedField(self, 'TxNtfctn', RegulatoryReportingNotification4, True)

	@TxNtfctn.deleter
	def TxNtfctn(self):
		del self._TxNtfctn
		self._TxNtfctn = base_types.UninitialisedField(self, 'TxNtfctn', RegulatoryReportingNotification4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxNtfctn', type=RegulatoryReportingNotification4, min=1, max=None, mutex_group=None, array=True),
	))