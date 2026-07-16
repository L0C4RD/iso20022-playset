# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference10
from . import FundReferenceDataReport5
from . import Max35Text
from . import MessageIdentification1

class FundReferenceDataReportV07(base_types._BaseFieldType):

	__slots__ = ["_FndRefDataRptId", "_MsgId", "_PrvsRef", "_RltdRef", "_Rpt"]
	@property
	def FndRefDataRptId(self):
		return self._FndRefDataRptId

	@FndRefDataRptId.setter
	def FndRefDataRptId(self, value):
		self._FndRefDataRptId = value if value is not None else base_types.UninitialisedField(self, 'FndRefDataRptId', Max35Text, False)

	@FndRefDataRptId.deleter
	def FndRefDataRptId(self):
		del self._FndRefDataRptId
		self._FndRefDataRptId = base_types.UninitialisedField(self, 'FndRefDataRptId', Max35Text, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, True)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, True)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if value is not None else base_types.UninitialisedField(self, 'Rpt', FundReferenceDataReport5, True)

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = base_types.UninitialisedField(self, 'Rpt', FundReferenceDataReport5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndRefDataRptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=FundReferenceDataReport5, min=1, max=None, mutex_group=None, array=True),
	))