import base_types
import Max70Text
import AccountIdentification80Choice
import ATMAccountStatement2

class ATMAccountStatement3(base_types._BaseFieldType):

	__slots__ = ["_AcctNm", "_AcctStmt", "_AcctIdr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctStmt', type=ATMAccountStatement2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=1, max=1, mutex_group=None, array=False),
	))

