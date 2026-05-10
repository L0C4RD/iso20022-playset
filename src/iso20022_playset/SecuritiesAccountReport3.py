from . import base_types
import SecuritiesAccountOrBusinessError3Choice
import SecuritiesAccount19

class SecuritiesAccountReport3(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctId", "_SctiesAcctOrErr"]
	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if type(value) != auto else self.make_default("SctiesAcctId")

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = None

	@property
	def SctiesAcctOrErr(self):
		return self._SctiesAcctOrErr

	@SctiesAcctOrErr.setter
	def SctiesAcctOrErr(self, value):
		self._SctiesAcctOrErr = value if type(value) != auto else self.make_default("SctiesAcctOrErr")

	@SctiesAcctOrErr.deleter
	def SctiesAcctOrErr(self):
		del self._SctiesAcctOrErr
		self._SctiesAcctOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctOrErr', type=SecuritiesAccountOrBusinessError3Choice, min=1, max=1, mutex_group=None, array=False),
	))

