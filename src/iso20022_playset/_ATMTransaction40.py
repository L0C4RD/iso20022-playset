# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import FailureReason8Code
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier3

class ATMTransaction40(base_types._BaseFieldType):

	__slots__ = ["_ElctrncPrsBal", "_RcncltnId", "_TxId", "_Xcptn", "_XcptnDtl"]
	@property
	def ElctrncPrsBal(self):
		return self._ElctrncPrsBal

	@ElctrncPrsBal.setter
	def ElctrncPrsBal(self, value):
		self._ElctrncPrsBal = value if value is not None else base_types.UninitialisedField(self, 'ElctrncPrsBal', CurrencyAndAmount, False)

	@ElctrncPrsBal.deleter
	def ElctrncPrsBal(self):
		del self._ElctrncPrsBal
		self._ElctrncPrsBal = base_types.UninitialisedField(self, 'ElctrncPrsBal', CurrencyAndAmount, False)

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

	@property
	def Xcptn(self):
		return self._Xcptn

	@Xcptn.setter
	def Xcptn(self, value):
		self._Xcptn = value if value is not None else base_types.UninitialisedField(self, 'Xcptn', FailureReason8Code, True)

	@Xcptn.deleter
	def Xcptn(self):
		del self._Xcptn
		self._Xcptn = base_types.UninitialisedField(self, 'Xcptn', FailureReason8Code, True)

	@property
	def XcptnDtl(self):
		return self._XcptnDtl

	@XcptnDtl.setter
	def XcptnDtl(self, value):
		self._XcptnDtl = value if value is not None else base_types.UninitialisedField(self, 'XcptnDtl', Max70Text, True)

	@XcptnDtl.deleter
	def XcptnDtl(self):
		del self._XcptnDtl
		self._XcptnDtl = base_types.UninitialisedField(self, 'XcptnDtl', Max70Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncPrsBal', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xcptn', type=FailureReason8Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XcptnDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
	))