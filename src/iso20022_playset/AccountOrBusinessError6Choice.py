import base_types
import CashAccountData1
import ErrorHandling5

class AccountOrBusinessError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_Acct"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Acct', type=CashAccountData1, min=0, max=1, mutex_group=1, array=False),
	))

