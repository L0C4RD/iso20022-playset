# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import Max35Text

class Account23(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_RltdAcctDtls"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def RltdAcctDtls(self):
		return self._RltdAcctDtls

	@RltdAcctDtls.setter
	def RltdAcctDtls(self, value):
		self._RltdAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'RltdAcctDtls', GenericIdentification1, False)

	@RltdAcctDtls.deleter
	def RltdAcctDtls(self):
		del self._RltdAcctDtls
		self._RltdAcctDtls = base_types.UninitialisedField(self, 'RltdAcctDtls', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAcctDtls', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
	))