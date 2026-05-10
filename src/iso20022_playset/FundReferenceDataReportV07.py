from . import base_types
from .AdditionalReference10 import AdditionalReference10
from .FundReferenceDataReport5 import FundReferenceDataReport5
from .MessageIdentification1 import MessageIdentification1
from .Max35Text import Max35Text

class FundReferenceDataReportV07(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_FndRefDataRptId", "_Rpt", "_PrvsRef", "_RltdRef"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def FndRefDataRptId(self):
		return self._FndRefDataRptId

	@FndRefDataRptId.setter
	def FndRefDataRptId(self, value):
		self._FndRefDataRptId = value if type(value) != base_types.auto else self.make_default("FndRefDataRptId")

	@FndRefDataRptId.deleter
	def FndRefDataRptId(self):
		del self._FndRefDataRptId
		self._FndRefDataRptId = None

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != base_types.auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndRefDataRptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=FundReferenceDataReport5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
	))

