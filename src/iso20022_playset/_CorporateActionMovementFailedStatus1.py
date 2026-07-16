# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FailedMovement1
from . import Max35Text
from . import PartyIdentification2Choice

class CorporateActionMovementFailedStatus1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_AgtAcctId", "_ClntAcctId", "_RsrcDtls"]
	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = base_types.UninitialisedField(self, 'AcctOwnrId', PartyIdentification2Choice, False)

	@property
	def AgtAcctId(self):
		return self._AgtAcctId

	@AgtAcctId.setter
	def AgtAcctId(self, value):
		self._AgtAcctId = value if value is not None else base_types.UninitialisedField(self, 'AgtAcctId', Max35Text, False)

	@AgtAcctId.deleter
	def AgtAcctId(self):
		del self._AgtAcctId
		self._AgtAcctId = base_types.UninitialisedField(self, 'AgtAcctId', Max35Text, False)

	@property
	def ClntAcctId(self):
		return self._ClntAcctId

	@ClntAcctId.setter
	def ClntAcctId(self, value):
		self._ClntAcctId = value if value is not None else base_types.UninitialisedField(self, 'ClntAcctId', Max35Text, False)

	@ClntAcctId.deleter
	def ClntAcctId(self):
		del self._ClntAcctId
		self._ClntAcctId = base_types.UninitialisedField(self, 'ClntAcctId', Max35Text, False)

	@property
	def RsrcDtls(self):
		return self._RsrcDtls

	@RsrcDtls.setter
	def RsrcDtls(self, value):
		self._RsrcDtls = value if value is not None else base_types.UninitialisedField(self, 'RsrcDtls', FailedMovement1, True)

	@RsrcDtls.deleter
	def RsrcDtls(self):
		del self._RsrcDtls
		self._RsrcDtls = base_types.UninitialisedField(self, 'RsrcDtls', FailedMovement1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtAcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcDtls', type=FailedMovement1, min=1, max=None, mutex_group=None, array=True),
	))