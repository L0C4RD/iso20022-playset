from . import base_types
from ._NetObligation3 import NetObligation3
from ._NetReportData2 import NetReportData2
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._SupplementaryData1 import SupplementaryData1

class NetReportV03(base_types._BaseFieldType):

	__slots__ = ["_NetOblgtn", "_NetRptData", "_NetSvcCtrPtyId", "_NetSvcPtcptId", "_SplmtryData"]
	@property
	def NetOblgtn(self):
		return self._NetOblgtn

	@NetOblgtn.setter
	def NetOblgtn(self, value):
		self._NetOblgtn = value if type(value) != base_types.auto else self.make_default("NetOblgtn")

	@NetOblgtn.deleter
	def NetOblgtn(self):
		del self._NetOblgtn
		self._NetOblgtn = None

	@property
	def NetRptData(self):
		return self._NetRptData

	@NetRptData.setter
	def NetRptData(self, value):
		self._NetRptData = value if type(value) != base_types.auto else self.make_default("NetRptData")

	@NetRptData.deleter
	def NetRptData(self):
		del self._NetRptData
		self._NetRptData = None

	@property
	def NetSvcCtrPtyId(self):
		return self._NetSvcCtrPtyId

	@NetSvcCtrPtyId.setter
	def NetSvcCtrPtyId(self, value):
		self._NetSvcCtrPtyId = value if type(value) != base_types.auto else self.make_default("NetSvcCtrPtyId")

	@NetSvcCtrPtyId.deleter
	def NetSvcCtrPtyId(self):
		del self._NetSvcCtrPtyId
		self._NetSvcCtrPtyId = None

	@property
	def NetSvcPtcptId(self):
		return self._NetSvcPtcptId

	@NetSvcPtcptId.setter
	def NetSvcPtcptId(self, value):
		self._NetSvcPtcptId = value if type(value) != base_types.auto else self.make_default("NetSvcPtcptId")

	@NetSvcPtcptId.deleter
	def NetSvcPtcptId(self):
		del self._NetSvcPtcptId
		self._NetSvcPtcptId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetOblgtn', type=NetObligation3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetRptData', type=NetReportData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcCtrPtyId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

