# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCommand7
from . import Max10000Binary
from . import Response12Code
from . import ResultDetail5Code
from . import TransactionIdentifier3

class ATMTransaction45(base_types._BaseFieldType):

	__slots__ = ["_Cmd", "_ICCRltdData", "_Rspn", "_RspnRsn", "_TxId"]
	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', Response12Code, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', Response12Code, False)

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if value is not None else base_types.UninitialisedField(self, 'RspnRsn', ResultDetail5Code, False)

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = base_types.UninitialisedField(self, 'RspnRsn', ResultDetail5Code, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response12Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=ResultDetail5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))