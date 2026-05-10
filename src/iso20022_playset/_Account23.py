from . import base_types
from ._Max35Text import Max35Text
from ._GenericIdentification1 import GenericIdentification1

class Account23(base_types._BaseFieldType):

	__slots__ = ["_RltdAcctDtls", "_AcctId"]
	@property
	def RltdAcctDtls(self):
		return self._RltdAcctDtls

	@RltdAcctDtls.setter
	def RltdAcctDtls(self, value):
		self._RltdAcctDtls = value if type(value) != base_types.auto else self.make_default("RltdAcctDtls")

	@RltdAcctDtls.deleter
	def RltdAcctDtls(self):
		del self._RltdAcctDtls
		self._RltdAcctDtls = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdAcctDtls', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

