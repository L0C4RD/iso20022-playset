from . import base_types
import GenericIdentification1
import Max35Text

class Account23(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_RltdAcctDtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def RltdAcctDtls(self):
		return self._RltdAcctDtls

	@RltdAcctDtls.setter
	def RltdAcctDtls(self, value):
		self._RltdAcctDtls = value if type(value) != auto else self.make_default("RltdAcctDtls")

	@RltdAcctDtls.deleter
	def RltdAcctDtls(self):
		del self._RltdAcctDtls
		self._RltdAcctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAcctDtls', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

