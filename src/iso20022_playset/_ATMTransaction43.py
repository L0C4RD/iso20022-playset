# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10000Binary
from . import Max35Text
from . import OnLinePIN5
from . import TransactionIdentifier3

class ATMTransaction43(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrNewPIN", "_ICCRltdData", "_RcncltnId", "_TxId"]
	@property
	def CrdhldrNewPIN(self):
		return self._CrdhldrNewPIN

	@CrdhldrNewPIN.setter
	def CrdhldrNewPIN(self, value):
		self._CrdhldrNewPIN = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrNewPIN', OnLinePIN5, False)

	@CrdhldrNewPIN.deleter
	def CrdhldrNewPIN(self):
		del self._CrdhldrNewPIN
		self._CrdhldrNewPIN = base_types.UninitialisedField(self, 'CrdhldrNewPIN', OnLinePIN5, False)

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
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

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
		base_types.FieldEntry(name='CrdhldrNewPIN', type=OnLinePIN5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))