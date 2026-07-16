# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountIdentification1Choice
from . import Max35Text
from . import PartyIdentification2Choice

class ProceedsDelivery1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrId", "_AcctSvcrId", "_CshAcctId", "_SctiesAcctId"]
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
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrId', PartyIdentification2Choice, False)

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = base_types.UninitialisedField(self, 'AcctSvcrId', PartyIdentification2Choice, False)

	@property
	def CshAcctId(self):
		return self._CshAcctId

	@CshAcctId.setter
	def CshAcctId(self, value):
		self._CshAcctId = value if value is not None else base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification1Choice, False)

	@CshAcctId.deleter
	def CshAcctId(self):
		del self._CshAcctId
		self._CshAcctId = base_types.UninitialisedField(self, 'CshAcctId', CashAccountIdentification1Choice, False)

	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctId', Max35Text, False)

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = base_types.UninitialisedField(self, 'SctiesAcctId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctId', type=CashAccountIdentification1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))