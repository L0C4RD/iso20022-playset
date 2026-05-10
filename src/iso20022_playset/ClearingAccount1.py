from . import base_types
from .ClearingAccountType3Code import ClearingAccountType3Code
from .CollateralAccount5 import CollateralAccount5

class ClearingAccount1(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_CollAcctOwnr"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def CollAcctOwnr(self):
		return self._CollAcctOwnr

	@CollAcctOwnr.setter
	def CollAcctOwnr(self, value):
		self._CollAcctOwnr = value if type(value) != auto else self.make_default("CollAcctOwnr")

	@CollAcctOwnr.deleter
	def CollAcctOwnr(self):
		del self._CollAcctOwnr
		self._CollAcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=ClearingAccountType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctOwnr', type=CollateralAccount5, min=1, max=None, mutex_group=None, array=True),
	))

