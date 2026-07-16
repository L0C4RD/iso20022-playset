# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountingStatementOfHoldings2
from . import AdditionalReference2
from . import MessageIdentification1
from . import Pagination

class AccountingStatementOfHoldingsCancellationV02(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_MsgPgntn", "_PrvsRef", "_RltdRef", "_StmtToBeCanc"]
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
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference2, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference2, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference2, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference2, False)

	@property
	def StmtToBeCanc(self):
		return self._StmtToBeCanc

	@StmtToBeCanc.setter
	def StmtToBeCanc(self, value):
		self._StmtToBeCanc = value if value is not None else base_types.UninitialisedField(self, 'StmtToBeCanc', AccountingStatementOfHoldings2, False)

	@StmtToBeCanc.deleter
	def StmtToBeCanc(self):
		del self._StmtToBeCanc
		self._StmtToBeCanc = base_types.UninitialisedField(self, 'StmtToBeCanc', AccountingStatementOfHoldings2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtToBeCanc', type=AccountingStatementOfHoldings2, min=0, max=1, mutex_group=None, array=False),
	))