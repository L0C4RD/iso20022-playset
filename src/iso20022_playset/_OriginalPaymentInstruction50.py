# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchBookingIndicator
from . import DecimalNumber
from . import Max15NumericText
from . import Max35Text
from . import PaymentReversalReason10
from . import PaymentTransaction156
from . import TrueFalseIndicator

class OriginalPaymentInstruction50(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_OrgnlCtrlSum", "_OrgnlNbOfTxs", "_OrgnlPmtInfId", "_PmtInfRvsl", "_RvslPmtInfId", "_RvslRsnInf", "_TxInf"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if value is not None else base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

	@property
	def OrgnlCtrlSum(self):
		return self._OrgnlCtrlSum

	@OrgnlCtrlSum.setter
	def OrgnlCtrlSum(self, value):
		self._OrgnlCtrlSum = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCtrlSum', DecimalNumber, False)

	@OrgnlCtrlSum.deleter
	def OrgnlCtrlSum(self):
		del self._OrgnlCtrlSum
		self._OrgnlCtrlSum = base_types.UninitialisedField(self, 'OrgnlCtrlSum', DecimalNumber, False)

	@property
	def OrgnlNbOfTxs(self):
		return self._OrgnlNbOfTxs

	@OrgnlNbOfTxs.setter
	def OrgnlNbOfTxs(self, value):
		self._OrgnlNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'OrgnlNbOfTxs', Max15NumericText, False)

	@OrgnlNbOfTxs.deleter
	def OrgnlNbOfTxs(self):
		del self._OrgnlNbOfTxs
		self._OrgnlNbOfTxs = base_types.UninitialisedField(self, 'OrgnlNbOfTxs', Max15NumericText, False)

	@property
	def OrgnlPmtInfId(self):
		return self._OrgnlPmtInfId

	@OrgnlPmtInfId.setter
	def OrgnlPmtInfId(self, value):
		self._OrgnlPmtInfId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPmtInfId', Max35Text, False)

	@OrgnlPmtInfId.deleter
	def OrgnlPmtInfId(self):
		del self._OrgnlPmtInfId
		self._OrgnlPmtInfId = base_types.UninitialisedField(self, 'OrgnlPmtInfId', Max35Text, False)

	@property
	def PmtInfRvsl(self):
		return self._PmtInfRvsl

	@PmtInfRvsl.setter
	def PmtInfRvsl(self, value):
		self._PmtInfRvsl = value if value is not None else base_types.UninitialisedField(self, 'PmtInfRvsl', TrueFalseIndicator, False)

	@PmtInfRvsl.deleter
	def PmtInfRvsl(self):
		del self._PmtInfRvsl
		self._PmtInfRvsl = base_types.UninitialisedField(self, 'PmtInfRvsl', TrueFalseIndicator, False)

	@property
	def RvslPmtInfId(self):
		return self._RvslPmtInfId

	@RvslPmtInfId.setter
	def RvslPmtInfId(self, value):
		self._RvslPmtInfId = value if value is not None else base_types.UninitialisedField(self, 'RvslPmtInfId', Max35Text, False)

	@RvslPmtInfId.deleter
	def RvslPmtInfId(self):
		del self._RvslPmtInfId
		self._RvslPmtInfId = base_types.UninitialisedField(self, 'RvslPmtInfId', Max35Text, False)

	@property
	def RvslRsnInf(self):
		return self._RvslRsnInf

	@RvslRsnInf.setter
	def RvslRsnInf(self, value):
		self._RvslRsnInf = value if value is not None else base_types.UninitialisedField(self, 'RvslRsnInf', PaymentReversalReason10, True)

	@RvslRsnInf.deleter
	def RvslRsnInf(self):
		del self._RvslRsnInf
		self._RvslRsnInf = base_types.UninitialisedField(self, 'RvslRsnInf', PaymentReversalReason10, True)

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if value is not None else base_types.UninitialisedField(self, 'TxInf', PaymentTransaction156, True)

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = base_types.UninitialisedField(self, 'TxInf', PaymentTransaction156, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchBookg', type=BatchBookingIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfRvsl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslPmtInfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsnInf', type=PaymentReversalReason10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction156, min=0, max=None, mutex_group=None, array=True),
	))