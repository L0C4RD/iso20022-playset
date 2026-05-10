from . import base_types
from ._Max140Text import Max140Text
from ._ReconciliationStatus8Choice import ReconciliationStatus8Choice
from ._TradeTransactionIdentification19 import TradeTransactionIdentification19
from ._TrueFalseIndicator import TrueFalseIndicator

class ReconciliationReport8(base_types._BaseFieldType):

	__slots__ = ["_Modfd", "_RcncltnSts", "_TechRcrdId", "_TxId"]
	@property
	def Modfd(self):
		return self._Modfd

	@Modfd.setter
	def Modfd(self, value):
		self._Modfd = value if type(value) != base_types.auto else self.make_default("Modfd")

	@Modfd.deleter
	def Modfd(self):
		del self._Modfd
		self._Modfd = None

	@property
	def RcncltnSts(self):
		return self._RcncltnSts

	@RcncltnSts.setter
	def RcncltnSts(self, value):
		self._RcncltnSts = value if type(value) != base_types.auto else self.make_default("RcncltnSts")

	@RcncltnSts.deleter
	def RcncltnSts(self):
		del self._RcncltnSts
		self._RcncltnSts = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

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
		base_types.FieldEntry(name='Modfd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnSts', type=ReconciliationStatus8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

