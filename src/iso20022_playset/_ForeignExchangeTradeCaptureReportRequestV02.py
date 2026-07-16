# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35NumericText
from . import Max35Text
from . import MessageIdentification1
from . import Period12
from . import QueryDataType1Code
from . import QueryOrderStatus1Code
from . import SupplementaryData1
from . import TrueFalseIndicator

class ForeignExchangeTradeCaptureReportRequestV02(base_types._BaseFieldType):

	__slots__ = ["_QryByPrd", "_QryEndId", "_QryOrdrSts", "_QryParamVal", "_QryPgSz", "_QryPrd", "_QryReqId", "_QryStartNb", "_QryTp", "_QryTradId", "_SplmtryData"]
	@property
	def QryByPrd(self):
		return self._QryByPrd

	@QryByPrd.setter
	def QryByPrd(self, value):
		self._QryByPrd = value if value is not None else base_types.UninitialisedField(self, 'QryByPrd', TrueFalseIndicator, False)

	@QryByPrd.deleter
	def QryByPrd(self):
		del self._QryByPrd
		self._QryByPrd = base_types.UninitialisedField(self, 'QryByPrd', TrueFalseIndicator, False)

	@property
	def QryEndId(self):
		return self._QryEndId

	@QryEndId.setter
	def QryEndId(self, value):
		self._QryEndId = value if value is not None else base_types.UninitialisedField(self, 'QryEndId', Max35Text, False)

	@QryEndId.deleter
	def QryEndId(self):
		del self._QryEndId
		self._QryEndId = base_types.UninitialisedField(self, 'QryEndId', Max35Text, False)

	@property
	def QryOrdrSts(self):
		return self._QryOrdrSts

	@QryOrdrSts.setter
	def QryOrdrSts(self, value):
		self._QryOrdrSts = value if value is not None else base_types.UninitialisedField(self, 'QryOrdrSts', QueryOrderStatus1Code, False)

	@QryOrdrSts.deleter
	def QryOrdrSts(self):
		del self._QryOrdrSts
		self._QryOrdrSts = base_types.UninitialisedField(self, 'QryOrdrSts', QueryOrderStatus1Code, False)

	@property
	def QryParamVal(self):
		return self._QryParamVal

	@QryParamVal.setter
	def QryParamVal(self, value):
		self._QryParamVal = value if value is not None else base_types.UninitialisedField(self, 'QryParamVal', Max35Text, False)

	@QryParamVal.deleter
	def QryParamVal(self):
		del self._QryParamVal
		self._QryParamVal = base_types.UninitialisedField(self, 'QryParamVal', Max35Text, False)

	@property
	def QryPgSz(self):
		return self._QryPgSz

	@QryPgSz.setter
	def QryPgSz(self, value):
		self._QryPgSz = value if value is not None else base_types.UninitialisedField(self, 'QryPgSz', Max35NumericText, False)

	@QryPgSz.deleter
	def QryPgSz(self):
		del self._QryPgSz
		self._QryPgSz = base_types.UninitialisedField(self, 'QryPgSz', Max35NumericText, False)

	@property
	def QryPrd(self):
		return self._QryPrd

	@QryPrd.setter
	def QryPrd(self, value):
		self._QryPrd = value if value is not None else base_types.UninitialisedField(self, 'QryPrd', Period12, False)

	@QryPrd.deleter
	def QryPrd(self):
		del self._QryPrd
		self._QryPrd = base_types.UninitialisedField(self, 'QryPrd', Period12, False)

	@property
	def QryReqId(self):
		return self._QryReqId

	@QryReqId.setter
	def QryReqId(self, value):
		self._QryReqId = value if value is not None else base_types.UninitialisedField(self, 'QryReqId', MessageIdentification1, False)

	@QryReqId.deleter
	def QryReqId(self):
		del self._QryReqId
		self._QryReqId = base_types.UninitialisedField(self, 'QryReqId', MessageIdentification1, False)

	@property
	def QryStartNb(self):
		return self._QryStartNb

	@QryStartNb.setter
	def QryStartNb(self, value):
		self._QryStartNb = value if value is not None else base_types.UninitialisedField(self, 'QryStartNb', Max35NumericText, False)

	@QryStartNb.deleter
	def QryStartNb(self):
		del self._QryStartNb
		self._QryStartNb = base_types.UninitialisedField(self, 'QryStartNb', Max35NumericText, False)

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', QueryDataType1Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', QueryDataType1Code, False)

	@property
	def QryTradId(self):
		return self._QryTradId

	@QryTradId.setter
	def QryTradId(self, value):
		self._QryTradId = value if value is not None else base_types.UninitialisedField(self, 'QryTradId', Max35Text, False)

	@QryTradId.deleter
	def QryTradId(self):
		del self._QryTradId
		self._QryTradId = base_types.UninitialisedField(self, 'QryTradId', Max35Text, False)

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
		base_types.FieldEntry(name='QryByPrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryOrdrSts', type=QueryOrderStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryParamVal', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPgSz', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPrd', type=Period12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=QueryDataType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))