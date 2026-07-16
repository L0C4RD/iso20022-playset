# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import AccountOrBusinessError6Choice

class AccountReport35(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOrErr"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@property
	def AcctOrErr(self):
		return self._AcctOrErr

	@AcctOrErr.setter
	def AcctOrErr(self, value):
		self._AcctOrErr = value if value is not None else base_types.UninitialisedField(self, 'AcctOrErr', AccountOrBusinessError6Choice, False)

	@AcctOrErr.deleter
	def AcctOrErr(self):
		del self._AcctOrErr
		self._AcctOrErr = base_types.UninitialisedField(self, 'AcctOrErr', AccountOrBusinessError6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOrErr', type=AccountOrBusinessError6Choice, min=1, max=1, mutex_group=None, array=False),
	))