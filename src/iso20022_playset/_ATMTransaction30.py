from . import base_types
from ._ATMCassette3 import ATMCassette3
from ._ATMOperation2Code import ATMOperation2Code
from ._Max35Text import Max35Text
from ._TransactionIdentifier3 import TransactionIdentifier3

class ATMTransaction30(base_types._BaseFieldType):

	__slots__ = ["_Csstt", "_RcncltnId", "_TpOfOpr", "_TxId"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfOpr', type=ATMOperation2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=0, max=1, mutex_group=None, array=False),
	))

