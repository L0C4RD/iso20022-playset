# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import ReconciliationStatus8Choice
from . import TradeTransactionIdentification19
from . import TrueFalseIndicator

class ReconciliationReport8(base_types._BaseFieldType):

	__slots__ = ["_Modfd", "_RcncltnSts", "_TechRcrdId", "_TxId"]
	@property
	def Modfd(self):
		return self._Modfd

	@Modfd.setter
	def Modfd(self, value):
		self._Modfd = value if value is not None else base_types.UninitialisedField(self, 'Modfd', TrueFalseIndicator, False)

	@Modfd.deleter
	def Modfd(self):
		del self._Modfd
		self._Modfd = base_types.UninitialisedField(self, 'Modfd', TrueFalseIndicator, False)

	@property
	def RcncltnSts(self):
		return self._RcncltnSts

	@RcncltnSts.setter
	def RcncltnSts(self, value):
		self._RcncltnSts = value if value is not None else base_types.UninitialisedField(self, 'RcncltnSts', ReconciliationStatus8Choice, False)

	@RcncltnSts.deleter
	def RcncltnSts(self):
		del self._RcncltnSts
		self._RcncltnSts = base_types.UninitialisedField(self, 'RcncltnSts', ReconciliationStatus8Choice, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification19, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TradeTransactionIdentification19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Modfd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnSts', type=ReconciliationStatus8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TradeTransactionIdentification19, min=1, max=1, mutex_group=None, array=False),
	))