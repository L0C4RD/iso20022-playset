# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingAccountType4Code
from . import ISODateTime
from . import OrganisationIdentification15Choice
from . import UniqueTransactionIdentifier2Choice

class ClearingPartyAndTime22(base_types._BaseFieldType):

	__slots__ = ["_CCP", "_ClrAcctOrgn", "_ClrDtTm", "_ClrIdr", "_ClrRctDtTm", "_OrgnlIdr", "_OrgnlTradRpstryIdr"]
	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if value is not None else base_types.UninitialisedField(self, 'CCP', OrganisationIdentification15Choice, False)

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = base_types.UninitialisedField(self, 'CCP', OrganisationIdentification15Choice, False)

	@property
	def ClrAcctOrgn(self):
		return self._ClrAcctOrgn

	@ClrAcctOrgn.setter
	def ClrAcctOrgn(self, value):
		self._ClrAcctOrgn = value if value is not None else base_types.UninitialisedField(self, 'ClrAcctOrgn', ClearingAccountType4Code, False)

	@ClrAcctOrgn.deleter
	def ClrAcctOrgn(self):
		del self._ClrAcctOrgn
		self._ClrAcctOrgn = base_types.UninitialisedField(self, 'ClrAcctOrgn', ClearingAccountType4Code, False)

	@property
	def ClrDtTm(self):
		return self._ClrDtTm

	@ClrDtTm.setter
	def ClrDtTm(self, value):
		self._ClrDtTm = value if value is not None else base_types.UninitialisedField(self, 'ClrDtTm', ISODateTime, False)

	@ClrDtTm.deleter
	def ClrDtTm(self):
		del self._ClrDtTm
		self._ClrDtTm = base_types.UninitialisedField(self, 'ClrDtTm', ISODateTime, False)

	@property
	def ClrIdr(self):
		return self._ClrIdr

	@ClrIdr.setter
	def ClrIdr(self, value):
		self._ClrIdr = value if value is not None else base_types.UninitialisedField(self, 'ClrIdr', UniqueTransactionIdentifier2Choice, False)

	@ClrIdr.deleter
	def ClrIdr(self):
		del self._ClrIdr
		self._ClrIdr = base_types.UninitialisedField(self, 'ClrIdr', UniqueTransactionIdentifier2Choice, False)

	@property
	def ClrRctDtTm(self):
		return self._ClrRctDtTm

	@ClrRctDtTm.setter
	def ClrRctDtTm(self, value):
		self._ClrRctDtTm = value if value is not None else base_types.UninitialisedField(self, 'ClrRctDtTm', ISODateTime, False)

	@ClrRctDtTm.deleter
	def ClrRctDtTm(self):
		del self._ClrRctDtTm
		self._ClrRctDtTm = base_types.UninitialisedField(self, 'ClrRctDtTm', ISODateTime, False)

	@property
	def OrgnlIdr(self):
		return self._OrgnlIdr

	@OrgnlIdr.setter
	def OrgnlIdr(self, value):
		self._OrgnlIdr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlIdr', UniqueTransactionIdentifier2Choice, False)

	@OrgnlIdr.deleter
	def OrgnlIdr(self):
		del self._OrgnlIdr
		self._OrgnlIdr = base_types.UninitialisedField(self, 'OrgnlIdr', UniqueTransactionIdentifier2Choice, False)

	@property
	def OrgnlTradRpstryIdr(self):
		return self._OrgnlTradRpstryIdr

	@OrgnlTradRpstryIdr.setter
	def OrgnlTradRpstryIdr(self, value):
		self._OrgnlTradRpstryIdr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTradRpstryIdr', OrganisationIdentification15Choice, False)

	@OrgnlTradRpstryIdr.deleter
	def OrgnlTradRpstryIdr(self):
		del self._OrgnlTradRpstryIdr
		self._OrgnlTradRpstryIdr = base_types.UninitialisedField(self, 'OrgnlTradRpstryIdr', OrganisationIdentification15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCP', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcctOrgn', type=ClearingAccountType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrIdr', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrRctDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIdr', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTradRpstryIdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))