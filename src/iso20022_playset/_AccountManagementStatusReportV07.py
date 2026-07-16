# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountManagementStatusAndReason5
from . import AdditionalReference13
from . import Extension1
from . import MarketPracticeVersion1
from . import MessageIdentification1

class AccountManagementStatusReportV07(base_types._BaseFieldType):

	__slots__ = ["_MktPrctcVrsn", "_MsgId", "_RltdRef", "_StsRpt", "_Xtnsn"]
	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if value is not None else base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

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
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference13, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference13, False)

	@property
	def StsRpt(self):
		return self._StsRpt

	@StsRpt.setter
	def StsRpt(self, value):
		self._StsRpt = value if value is not None else base_types.UninitialisedField(self, 'StsRpt', AccountManagementStatusAndReason5, False)

	@StsRpt.deleter
	def StsRpt(self):
		del self._StsRpt
		self._StsRpt = base_types.UninitialisedField(self, 'StsRpt', AccountManagementStatusAndReason5, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference13, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRpt', type=AccountManagementStatusAndReason5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))