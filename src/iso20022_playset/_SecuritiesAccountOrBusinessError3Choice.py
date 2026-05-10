from . import base_types
from ._SystemSecuritiesAccount6 import SystemSecuritiesAccount6
from ._ErrorHandling5 import ErrorHandling5

class SecuritiesAccountOrBusinessError3Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcct", "_BizErr"]
	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if type(value) != base_types.auto else self.make_default("SctiesAcct")

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcct', type=SystemSecuritiesAccount6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

