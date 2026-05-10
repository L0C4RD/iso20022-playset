from . import base_types
from ._BatchBookingIndicator import BatchBookingIndicator
from ._DecimalNumber import DecimalNumber
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._PaymentReversalReason10 import PaymentReversalReason10
from ._PaymentTransaction156 import PaymentTransaction156
from ._TrueFalseIndicator import TrueFalseIndicator

class OriginalPaymentInstruction50(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_OrgnlCtrlSum", "_OrgnlNbOfTxs", "_OrgnlPmtInfId", "_PmtInfRvsl", "_RvslPmtInfId", "_RvslRsnInf", "_TxInf"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if type(value) != base_types.auto else self.make_default("BtchBookg")

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = None

	@property
	def OrgnlCtrlSum(self):
		return self._OrgnlCtrlSum

	@OrgnlCtrlSum.setter
	def OrgnlCtrlSum(self, value):
		self._OrgnlCtrlSum = value if type(value) != base_types.auto else self.make_default("OrgnlCtrlSum")

	@OrgnlCtrlSum.deleter
	def OrgnlCtrlSum(self):
		del self._OrgnlCtrlSum
		self._OrgnlCtrlSum = None

	@property
	def OrgnlNbOfTxs(self):
		return self._OrgnlNbOfTxs

	@OrgnlNbOfTxs.setter
	def OrgnlNbOfTxs(self, value):
		self._OrgnlNbOfTxs = value if type(value) != base_types.auto else self.make_default("OrgnlNbOfTxs")

	@OrgnlNbOfTxs.deleter
	def OrgnlNbOfTxs(self):
		del self._OrgnlNbOfTxs
		self._OrgnlNbOfTxs = None

	@property
	def OrgnlPmtInfId(self):
		return self._OrgnlPmtInfId

	@OrgnlPmtInfId.setter
	def OrgnlPmtInfId(self, value):
		self._OrgnlPmtInfId = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfId")

	@OrgnlPmtInfId.deleter
	def OrgnlPmtInfId(self):
		del self._OrgnlPmtInfId
		self._OrgnlPmtInfId = None

	@property
	def PmtInfRvsl(self):
		return self._PmtInfRvsl

	@PmtInfRvsl.setter
	def PmtInfRvsl(self, value):
		self._PmtInfRvsl = value if type(value) != base_types.auto else self.make_default("PmtInfRvsl")

	@PmtInfRvsl.deleter
	def PmtInfRvsl(self):
		del self._PmtInfRvsl
		self._PmtInfRvsl = None

	@property
	def RvslPmtInfId(self):
		return self._RvslPmtInfId

	@RvslPmtInfId.setter
	def RvslPmtInfId(self, value):
		self._RvslPmtInfId = value if type(value) != base_types.auto else self.make_default("RvslPmtInfId")

	@RvslPmtInfId.deleter
	def RvslPmtInfId(self):
		del self._RvslPmtInfId
		self._RvslPmtInfId = None

	@property
	def RvslRsnInf(self):
		return self._RvslRsnInf

	@RvslRsnInf.setter
	def RvslRsnInf(self, value):
		self._RvslRsnInf = value if type(value) != base_types.auto else self.make_default("RvslRsnInf")

	@RvslRsnInf.deleter
	def RvslRsnInf(self):
		del self._RvslRsnInf
		self._RvslRsnInf = None

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if type(value) != base_types.auto else self.make_default("TxInf")

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = None

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

