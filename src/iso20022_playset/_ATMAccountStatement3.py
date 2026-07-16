# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMAccountStatement2
from . import AccountIdentification80Choice
from . import Max70Text

class ATMAccountStatement3(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctNm", "_AcctStmt"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if value is not None else base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@property
	def AcctStmt(self):
		return self._AcctStmt

	@AcctStmt.setter
	def AcctStmt(self, value):
		self._AcctStmt = value if value is not None else base_types.UninitialisedField(self, 'AcctStmt', ATMAccountStatement2, True)

	@AcctStmt.deleter
	def AcctStmt(self):
		del self._AcctStmt
		self._AcctStmt = base_types.UninitialisedField(self, 'AcctStmt', ATMAccountStatement2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctStmt', type=ATMAccountStatement2, min=0, max=None, mutex_group=None, array=True),
	))