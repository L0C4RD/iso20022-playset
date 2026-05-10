from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .ClearingAccount1 import ClearingAccount1
from .ISODate import ISODate
from .CreditQuality1Code import CreditQuality1Code
from .PartyIdentification118Choice import PartyIdentification118Choice

class ClearingMember1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_CdtQlty", "_SpnsrgClrMmbId", "_ClrAcctOwnr", "_UltmtPrntId", "_FutrsComssnMrchntInd", "_MmbshVldFr", "_MmbshVldTo"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def CdtQlty(self):
		return self._CdtQlty

	@CdtQlty.setter
	def CdtQlty(self, value):
		self._CdtQlty = value if type(value) != base_types.auto else self.make_default("CdtQlty")

	@CdtQlty.deleter
	def CdtQlty(self):
		del self._CdtQlty
		self._CdtQlty = None

	@property
	def SpnsrgClrMmbId(self):
		return self._SpnsrgClrMmbId

	@SpnsrgClrMmbId.setter
	def SpnsrgClrMmbId(self, value):
		self._SpnsrgClrMmbId = value if type(value) != base_types.auto else self.make_default("SpnsrgClrMmbId")

	@SpnsrgClrMmbId.deleter
	def SpnsrgClrMmbId(self):
		del self._SpnsrgClrMmbId
		self._SpnsrgClrMmbId = None

	@property
	def ClrAcctOwnr(self):
		return self._ClrAcctOwnr

	@ClrAcctOwnr.setter
	def ClrAcctOwnr(self, value):
		self._ClrAcctOwnr = value if type(value) != base_types.auto else self.make_default("ClrAcctOwnr")

	@ClrAcctOwnr.deleter
	def ClrAcctOwnr(self):
		del self._ClrAcctOwnr
		self._ClrAcctOwnr = None

	@property
	def UltmtPrntId(self):
		return self._UltmtPrntId

	@UltmtPrntId.setter
	def UltmtPrntId(self, value):
		self._UltmtPrntId = value if type(value) != base_types.auto else self.make_default("UltmtPrntId")

	@UltmtPrntId.deleter
	def UltmtPrntId(self):
		del self._UltmtPrntId
		self._UltmtPrntId = None

	@property
	def FutrsComssnMrchntInd(self):
		return self._FutrsComssnMrchntInd

	@FutrsComssnMrchntInd.setter
	def FutrsComssnMrchntInd(self, value):
		self._FutrsComssnMrchntInd = value if type(value) != base_types.auto else self.make_default("FutrsComssnMrchntInd")

	@FutrsComssnMrchntInd.deleter
	def FutrsComssnMrchntInd(self):
		del self._FutrsComssnMrchntInd
		self._FutrsComssnMrchntInd = None

	@property
	def MmbshVldFr(self):
		return self._MmbshVldFr

	@MmbshVldFr.setter
	def MmbshVldFr(self, value):
		self._MmbshVldFr = value if type(value) != base_types.auto else self.make_default("MmbshVldFr")

	@MmbshVldFr.deleter
	def MmbshVldFr(self):
		del self._MmbshVldFr
		self._MmbshVldFr = None

	@property
	def MmbshVldTo(self):
		return self._MmbshVldTo

	@MmbshVldTo.setter
	def MmbshVldTo(self, value):
		self._MmbshVldTo = value if type(value) != base_types.auto else self.make_default("MmbshVldTo")

	@MmbshVldTo.deleter
	def MmbshVldTo(self):
		del self._MmbshVldTo
		self._MmbshVldTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtQlty', type=CreditQuality1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrgClrMmbId', type=PartyIdentification118Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcctOwnr', type=ClearingAccount1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UltmtPrntId', type=PartyIdentification118Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FutrsComssnMrchntInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbshVldFr', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbshVldTo', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

