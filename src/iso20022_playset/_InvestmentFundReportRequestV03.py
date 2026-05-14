# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._FundParameters4Choice import FundParameters4Choice
from ._MessageIdentification1 import MessageIdentification1

class InvestmentFundReportRequestV03(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_PrvsRef", "_RltdRef", "_RptReq"]
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

	@property
	def RptReq(self):
		return self._RptReq

	@RptReq.setter
	def RptReq(self, value):
		self._RptReq = value if type(value) != base_types.auto else self.make_default("RptReq")

	@RptReq.deleter
	def RptReq(self):
		del self._RptReq
		self._RptReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptReq', type=FundParameters4Choice, min=1, max=None, mutex_group=None, array=True),
	))