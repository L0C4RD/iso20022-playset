from . import base_types
import AccountOrBusinessError6Choice
import AccountIdentification4Choice

class AccountReport35(base_types._BaseFieldType):

	__slots__ = ["_AcctOrErr", "_AcctId"]
	@property
	def AcctOrErr(self):
		return self._AcctOrErr

	@AcctOrErr.setter
	def AcctOrErr(self, value):
		self._AcctOrErr = value if type(value) != auto else self.make_default("AcctOrErr")

	@AcctOrErr.deleter
	def AcctOrErr(self):
		del self._AcctOrErr
		self._AcctOrErr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOrErr', type=AccountOrBusinessError6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
	))

