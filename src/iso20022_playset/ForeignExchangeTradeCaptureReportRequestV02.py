from . import base_types
import MessageIdentification1
import QueryDataType1Code
import SupplementaryData1
import Max35Text
import QueryOrderStatus1Code
import Max35NumericText
import TrueFalseIndicator
import Period12

class ForeignExchangeTradeCaptureReportRequestV02(base_types._BaseFieldType):

	__slots__ = ["_QryStartNb", "_QryEndId", "_QryParamVal", "_QryTradId", "_SplmtryData", "_QryPrd", "_QryByPrd", "_QryReqId", "_QryOrdrSts", "_QryTp", "_QryPgSz"]
	@property
	def QryStartNb(self):
		return self._QryStartNb

	@QryStartNb.setter
	def QryStartNb(self, value):
		self._QryStartNb = value if type(value) != auto else self.make_default("QryStartNb")

	@QryStartNb.deleter
	def QryStartNb(self):
		del self._QryStartNb
		self._QryStartNb = None

	@property
	def QryEndId(self):
		return self._QryEndId

	@QryEndId.setter
	def QryEndId(self, value):
		self._QryEndId = value if type(value) != auto else self.make_default("QryEndId")

	@QryEndId.deleter
	def QryEndId(self):
		del self._QryEndId
		self._QryEndId = None

	@property
	def QryParamVal(self):
		return self._QryParamVal

	@QryParamVal.setter
	def QryParamVal(self, value):
		self._QryParamVal = value if type(value) != auto else self.make_default("QryParamVal")

	@QryParamVal.deleter
	def QryParamVal(self):
		del self._QryParamVal
		self._QryParamVal = None

	@property
	def QryTradId(self):
		return self._QryTradId

	@QryTradId.setter
	def QryTradId(self, value):
		self._QryTradId = value if type(value) != auto else self.make_default("QryTradId")

	@QryTradId.deleter
	def QryTradId(self):
		del self._QryTradId
		self._QryTradId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def QryPrd(self):
		return self._QryPrd

	@QryPrd.setter
	def QryPrd(self, value):
		self._QryPrd = value if type(value) != auto else self.make_default("QryPrd")

	@QryPrd.deleter
	def QryPrd(self):
		del self._QryPrd
		self._QryPrd = None

	@property
	def QryByPrd(self):
		return self._QryByPrd

	@QryByPrd.setter
	def QryByPrd(self, value):
		self._QryByPrd = value if type(value) != auto else self.make_default("QryByPrd")

	@QryByPrd.deleter
	def QryByPrd(self):
		del self._QryByPrd
		self._QryByPrd = None

	@property
	def QryReqId(self):
		return self._QryReqId

	@QryReqId.setter
	def QryReqId(self, value):
		self._QryReqId = value if type(value) != auto else self.make_default("QryReqId")

	@QryReqId.deleter
	def QryReqId(self):
		del self._QryReqId
		self._QryReqId = None

	@property
	def QryOrdrSts(self):
		return self._QryOrdrSts

	@QryOrdrSts.setter
	def QryOrdrSts(self, value):
		self._QryOrdrSts = value if type(value) != auto else self.make_default("QryOrdrSts")

	@QryOrdrSts.deleter
	def QryOrdrSts(self):
		del self._QryOrdrSts
		self._QryOrdrSts = None

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def QryPgSz(self):
		return self._QryPgSz

	@QryPgSz.setter
	def QryPgSz(self, value):
		self._QryPgSz = value if type(value) != auto else self.make_default("QryPgSz")

	@QryPgSz.deleter
	def QryPgSz(self):
		del self._QryPgSz
		self._QryPgSz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryParamVal', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QryPrd', type=Period12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryByPrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryOrdrSts', type=QueryOrderStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryDataType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPgSz', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))

