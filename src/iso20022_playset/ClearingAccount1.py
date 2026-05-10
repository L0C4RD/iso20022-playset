import base_types
import CollateralAccount5
import ClearingAccountType3Code

class ClearingAccount1(base_types._BaseFieldType):

	__slots__ = ["_CollAcctOwnr", "_AcctTp"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollAcctOwnr', type=CollateralAccount5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctTp', type=ClearingAccountType3Code, min=1, max=1, mutex_group=None, array=False),
	))

