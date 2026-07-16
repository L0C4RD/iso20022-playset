# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingAccount1
from . import CreditQuality1Code
from . import ISODate
from . import PartyIdentification118Choice
from . import TrueFalseIndicator

class ClearingMember1(base_types._BaseFieldType):

	__slots__ = ["_CdtQlty", "_ClrAcctOwnr", "_FutrsComssnMrchntInd", "_Id", "_MmbshVldFr", "_MmbshVldTo", "_SpnsrgClrMmbId", "_UltmtPrntId"]
	@property
	def CdtQlty(self):
		return self._CdtQlty

	@CdtQlty.setter
	def CdtQlty(self, value):
		self._CdtQlty = value if value is not None else base_types.UninitialisedField(self, 'CdtQlty', CreditQuality1Code, False)

	@CdtQlty.deleter
	def CdtQlty(self):
		del self._CdtQlty
		self._CdtQlty = base_types.UninitialisedField(self, 'CdtQlty', CreditQuality1Code, False)

	@property
	def ClrAcctOwnr(self):
		return self._ClrAcctOwnr

	@ClrAcctOwnr.setter
	def ClrAcctOwnr(self, value):
		self._ClrAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'ClrAcctOwnr', ClearingAccount1, True)

	@ClrAcctOwnr.deleter
	def ClrAcctOwnr(self):
		del self._ClrAcctOwnr
		self._ClrAcctOwnr = base_types.UninitialisedField(self, 'ClrAcctOwnr', ClearingAccount1, True)

	@property
	def FutrsComssnMrchntInd(self):
		return self._FutrsComssnMrchntInd

	@FutrsComssnMrchntInd.setter
	def FutrsComssnMrchntInd(self, value):
		self._FutrsComssnMrchntInd = value if value is not None else base_types.UninitialisedField(self, 'FutrsComssnMrchntInd', TrueFalseIndicator, False)

	@FutrsComssnMrchntInd.deleter
	def FutrsComssnMrchntInd(self):
		del self._FutrsComssnMrchntInd
		self._FutrsComssnMrchntInd = base_types.UninitialisedField(self, 'FutrsComssnMrchntInd', TrueFalseIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification118Choice, False)

	@property
	def MmbshVldFr(self):
		return self._MmbshVldFr

	@MmbshVldFr.setter
	def MmbshVldFr(self, value):
		self._MmbshVldFr = value if value is not None else base_types.UninitialisedField(self, 'MmbshVldFr', ISODate, False)

	@MmbshVldFr.deleter
	def MmbshVldFr(self):
		del self._MmbshVldFr
		self._MmbshVldFr = base_types.UninitialisedField(self, 'MmbshVldFr', ISODate, False)

	@property
	def MmbshVldTo(self):
		return self._MmbshVldTo

	@MmbshVldTo.setter
	def MmbshVldTo(self, value):
		self._MmbshVldTo = value if value is not None else base_types.UninitialisedField(self, 'MmbshVldTo', ISODate, False)

	@MmbshVldTo.deleter
	def MmbshVldTo(self):
		del self._MmbshVldTo
		self._MmbshVldTo = base_types.UninitialisedField(self, 'MmbshVldTo', ISODate, False)

	@property
	def SpnsrgClrMmbId(self):
		return self._SpnsrgClrMmbId

	@SpnsrgClrMmbId.setter
	def SpnsrgClrMmbId(self, value):
		self._SpnsrgClrMmbId = value if value is not None else base_types.UninitialisedField(self, 'SpnsrgClrMmbId', PartyIdentification118Choice, False)

	@SpnsrgClrMmbId.deleter
	def SpnsrgClrMmbId(self):
		del self._SpnsrgClrMmbId
		self._SpnsrgClrMmbId = base_types.UninitialisedField(self, 'SpnsrgClrMmbId', PartyIdentification118Choice, False)

	@property
	def UltmtPrntId(self):
		return self._UltmtPrntId

	@UltmtPrntId.setter
	def UltmtPrntId(self, value):
		self._UltmtPrntId = value if value is not None else base_types.UninitialisedField(self, 'UltmtPrntId', PartyIdentification118Choice, False)

	@UltmtPrntId.deleter
	def UltmtPrntId(self):
		del self._UltmtPrntId
		self._UltmtPrntId = base_types.UninitialisedField(self, 'UltmtPrntId', PartyIdentification118Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtQlty', type=CreditQuality1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcctOwnr', type=ClearingAccount1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FutrsComssnMrchntInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbshVldFr', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbshVldTo', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrgClrMmbId', type=PartyIdentification118Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtPrntId', type=PartyIdentification118Choice, min=0, max=1, mutex_group=None, array=False),
	))