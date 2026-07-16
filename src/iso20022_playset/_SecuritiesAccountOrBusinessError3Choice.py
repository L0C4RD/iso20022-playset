# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import SystemSecuritiesAccount6

class SecuritiesAccountOrBusinessError3Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_SctiesAcct"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcct', SystemSecuritiesAccount6, False)

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = base_types.UninitialisedField(self, 'SctiesAcct', SystemSecuritiesAccount6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAcct', type=SystemSecuritiesAccount6, min=0, max=1, mutex_group=1, array=False),
	))