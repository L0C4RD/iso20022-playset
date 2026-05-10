from . import base_types
from .Max35Text import Max35Text
from .CustomerOrder1 import CustomerOrder1
from .CardAccountType3Code import CardAccountType3Code

class PaymentAccountRequest1(base_types._BaseFieldType):

	__slots__ = ["_AcctRef", "_AcctTp", "_CstmrOrdr"]
	@property
	def AcctRef(self):
		return self._AcctRef

	@AcctRef.setter
	def AcctRef(self, value):
		self._AcctRef = value if type(value) != base_types.auto else self.make_default("AcctRef")

	@AcctRef.deleter
	def AcctRef(self):
		del self._AcctRef
		self._AcctRef = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != base_types.auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
	))

