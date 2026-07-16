# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import SecuritiesAccount19

class AccountIdentification38Choice(base_types._BaseFieldType):

	__slots__ = ["_CshAcctId", "_SctiesAcctId"]
	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', AccountIdentification4Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=0, max=1, mutex_group=1, array=False),
	))