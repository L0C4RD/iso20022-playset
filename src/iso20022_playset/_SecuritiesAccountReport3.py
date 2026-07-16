# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccount19
from . import SecuritiesAccountOrBusinessError3Choice

class SecuritiesAccountReport3(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctId", "_SctiesAcctOrErr"]
	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctId', SecuritiesAccount19, False)

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = base_types.UninitialisedField(self, 'SctiesAcctId', SecuritiesAccount19, False)

	@property
	def SctiesAcctOrErr(self):
		return self._SctiesAcctOrErr

	@SctiesAcctOrErr.setter
	def SctiesAcctOrErr(self, value):
		self._SctiesAcctOrErr = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctOrErr', SecuritiesAccountOrBusinessError3Choice, False)

	@SctiesAcctOrErr.deleter
	def SctiesAcctOrErr(self):
		del self._SctiesAcctOrErr
		self._SctiesAcctOrErr = base_types.UninitialisedField(self, 'SctiesAcctOrErr', SecuritiesAccountOrBusinessError3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctOrErr', type=SecuritiesAccountOrBusinessError3Choice, min=1, max=1, mutex_group=None, array=False),
	))