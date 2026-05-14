# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndCurrency1 import AmountAndCurrency1
from ._CardAccount20 import CardAccount20
from ._ContentInformationType10 import ContentInformationType10
from ._DetailedAmount12 import DetailedAmount12
from ._Max10000Binary import Max10000Binary
from ._TransactionIdentifier3 import TransactionIdentifier3

class ATMTransaction42(base_types._BaseFieldType):

	__slots__ = ["_AcctData", "_DtldReqdAmt", "_ICCRltdData", "_PrtctdAcctData", "_TtlReqdAmt", "_TxId"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != base_types.auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != base_types.auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != base_types.auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if type(value) != base_types.auto else self.make_default("TtlReqdAmt")

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctData', type=CardAccount20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=AmountAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))