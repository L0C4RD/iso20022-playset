# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NetObligation3
from . import NetReportData2
from . import PartyIdentification242Choice
from . import SupplementaryData1

class NetReportV03(base_types._BaseFieldType):

	__slots__ = ["_NetOblgtn", "_NetRptData", "_NetSvcCtrPtyId", "_NetSvcPtcptId", "_SplmtryData"]
	@property
	def NetOblgtn(self):
		return self._NetOblgtn

	@NetOblgtn.setter
	def NetOblgtn(self, value):
		self._NetOblgtn = value if value is not None else base_types.UninitialisedField(self, 'NetOblgtn', NetObligation3, True)

	@NetOblgtn.deleter
	def NetOblgtn(self):
		del self._NetOblgtn
		self._NetOblgtn = base_types.UninitialisedField(self, 'NetOblgtn', NetObligation3, True)

	@property
	def NetRptData(self):
		return self._NetRptData

	@NetRptData.setter
	def NetRptData(self, value):
		self._NetRptData = value if value is not None else base_types.UninitialisedField(self, 'NetRptData', NetReportData2, False)

	@NetRptData.deleter
	def NetRptData(self):
		del self._NetRptData
		self._NetRptData = base_types.UninitialisedField(self, 'NetRptData', NetReportData2, False)

	@property
	def NetSvcCtrPtyId(self):
		return self._NetSvcCtrPtyId

	@NetSvcCtrPtyId.setter
	def NetSvcCtrPtyId(self, value):
		self._NetSvcCtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'NetSvcCtrPtyId', PartyIdentification242Choice, False)

	@NetSvcCtrPtyId.deleter
	def NetSvcCtrPtyId(self):
		del self._NetSvcCtrPtyId
		self._NetSvcCtrPtyId = base_types.UninitialisedField(self, 'NetSvcCtrPtyId', PartyIdentification242Choice, False)

	@property
	def NetSvcPtcptId(self):
		return self._NetSvcPtcptId

	@NetSvcPtcptId.setter
	def NetSvcPtcptId(self, value):
		self._NetSvcPtcptId = value if value is not None else base_types.UninitialisedField(self, 'NetSvcPtcptId', PartyIdentification242Choice, False)

	@NetSvcPtcptId.deleter
	def NetSvcPtcptId(self):
		del self._NetSvcPtcptId
		self._NetSvcPtcptId = base_types.UninitialisedField(self, 'NetSvcPtcptId', PartyIdentification242Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetOblgtn', type=NetObligation3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetRptData', type=NetReportData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcCtrPtyId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))