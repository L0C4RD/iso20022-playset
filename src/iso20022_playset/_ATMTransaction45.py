from . import base_types
from ._ATMCommand7 import ATMCommand7
from ._Max10000Binary import Max10000Binary
from ._Response12Code import Response12Code
from ._TransactionIdentifier3 import TransactionIdentifier3
from ._ResultDetail5Code import ResultDetail5Code

class ATMTransaction45(base_types._BaseFieldType):

	__slots__ = ["_Cmd", "_RspnRsn", "_ICCRltdData", "_Rspn", "_TxId"]
	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != base_types.auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

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
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if type(value) != base_types.auto else self.make_default("RspnRsn")

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = None

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
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response12Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=ResultDetail5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))

