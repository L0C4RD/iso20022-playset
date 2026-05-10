from . import base_types
import TrueFalseIndicator
import Max140Text
import ReconciliationStatus8Choice
import TradeTransactionIdentification19

class ReconciliationReport8(base_types._BaseFieldType):

	__slots__ = ["_RcncltnSts", "_TxId", "_Modfd", "_TechRcrdId"]
	@property
	def RcncltnSts(self):
		return self._RcncltnSts

	@RcncltnSts.setter
	def RcncltnSts(self, value):
		self._RcncltnSts = value if type(value) != auto else self.make_default("RcncltnSts")

	@RcncltnSts.deleter
	def RcncltnSts(self):
		del self._RcncltnSts
		self._RcncltnSts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def Modfd(self):
		return self._Modfd

	@Modfd.setter
	def Modfd(self, value):
		self._Modfd = value if type(value) != auto else self.make_default("Modfd")

	@Modfd.deleter
	def Modfd(self):
		del self._Modfd
		self._Modfd = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnSts', type=ReconciliationStatus8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Modfd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

