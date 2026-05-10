from . import base_types
from .CustomerOrder1 import CustomerOrder1
from .LoyaltyAccount3 import LoyaltyAccount3

class LoyaltyAccountRequest3(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_CstmrOrdr"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

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
		base_types.FieldEntry(name='Acct', type=LoyaltyAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
	))

