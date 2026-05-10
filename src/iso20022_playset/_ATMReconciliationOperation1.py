from . import base_types
from ._ATMTotals4 import ATMTotals4
from ._TransactionIdentifier3 import TransactionIdentifier3
from ._Number import Number
from ._ATMTotals3 import ATMTotals3
from ._ATMCassette3 import ATMCassette3
from ._Max35Text import Max35Text
from ._FailureReason9Code import FailureReason9Code
from ._ATMOperation2Code import ATMOperation2Code
from ._Max140Text import Max140Text

class ATMReconciliationOperation1(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_RtndCard", "_AddtlTxInf", "_TxTtls", "_ATMTtls", "_Incdnt", "_TpOfOpr", "_RcncltnId", "_Csstt"]
	@property
	def ATMTtls(self):
		return self._ATMTtls

	@ATMTtls.setter
	def ATMTtls(self, value):
		self._ATMTtls = value if type(value) != base_types.auto else self.make_default("ATMTtls")

	@ATMTtls.deleter
	def ATMTtls(self):
		del self._ATMTtls
		self._ATMTtls = None

	@property
	def AddtlTxInf(self):
		return self._AddtlTxInf

	@AddtlTxInf.setter
	def AddtlTxInf(self, value):
		self._AddtlTxInf = value if type(value) != base_types.auto else self.make_default("AddtlTxInf")

	@AddtlTxInf.deleter
	def AddtlTxInf(self):
		del self._AddtlTxInf
		self._AddtlTxInf = None

	@property
	def Csstt(self):
		return self._Csstt

	@Csstt.setter
	def Csstt(self, value):
		self._Csstt = value if type(value) != base_types.auto else self.make_default("Csstt")

	@Csstt.deleter
	def Csstt(self):
		del self._Csstt
		self._Csstt = None

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if type(value) != base_types.auto else self.make_default("Incdnt")

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def RtndCard(self):
		return self._RtndCard

	@RtndCard.setter
	def RtndCard(self, value):
		self._RtndCard = value if type(value) != base_types.auto else self.make_default("RtndCard")

	@RtndCard.deleter
	def RtndCard(self):
		del self._RtndCard
		self._RtndCard = None

	@property
	def TpOfOpr(self):
		return self._TpOfOpr

	@TpOfOpr.setter
	def TpOfOpr(self, value):
		self._TpOfOpr = value if type(value) != base_types.auto else self.make_default("TpOfOpr")

	@TpOfOpr.deleter
	def TpOfOpr(self):
		del self._TpOfOpr
		self._TpOfOpr = None

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

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != base_types.auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMTtls', type=ATMTotals4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtndCard', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfOpr', type=ATMOperation2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=ATMTotals3, min=0, max=None, mutex_group=None, array=True),
	))

