from . import base_types
from .Max70Text import Max70Text
from .ATMAccountStatement2 import ATMAccountStatement2
from .AccountIdentification80Choice import AccountIdentification80Choice

class ATMAccountStatement3(base_types._BaseFieldType):

	__slots__ = ["_AcctStmt", "_AcctIdr", "_AcctNm"]
	@property
	def AcctStmt(self):
		return self._AcctStmt

	@AcctStmt.setter
	def AcctStmt(self, value):
		self._AcctStmt = value if type(value) != auto else self.make_default("AcctStmt")

	@AcctStmt.deleter
	def AcctStmt(self):
		del self._AcctStmt
		self._AcctStmt = None

	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if type(value) != auto else self.make_default("AcctIdr")

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctStmt', type=ATMAccountStatement2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

