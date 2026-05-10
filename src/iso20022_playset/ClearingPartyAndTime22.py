import base_types
import ClearingAccountType4Code
import ISODateTime
import OrganisationIdentification15Choice
import UniqueTransactionIdentifier2Choice

class ClearingPartyAndTime22(base_types._BaseFieldType):

	__slots__ = ["_ClrIdr", "_CCP", "_ClrAcctOrgn", "_ClrRctDtTm", "_OrgnlIdr", "_OrgnlTradRpstryIdr", "_ClrDtTm"]
	@property
	def ClrIdr(self):
		return self._ClrIdr

	@ClrIdr.setter
	def ClrIdr(self, value):
		self._ClrIdr = value if type(value) != auto else self.make_default("ClrIdr")

	@ClrIdr.deleter
	def ClrIdr(self):
		del self._ClrIdr
		self._ClrIdr = None

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if type(value) != auto else self.make_default("CCP")

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = None

	@property
	def ClrAcctOrgn(self):
		return self._ClrAcctOrgn

	@ClrAcctOrgn.setter
	def ClrAcctOrgn(self, value):
		self._ClrAcctOrgn = value if type(value) != auto else self.make_default("ClrAcctOrgn")

	@ClrAcctOrgn.deleter
	def ClrAcctOrgn(self):
		del self._ClrAcctOrgn
		self._ClrAcctOrgn = None

	@property
	def ClrRctDtTm(self):
		return self._ClrRctDtTm

	@ClrRctDtTm.setter
	def ClrRctDtTm(self, value):
		self._ClrRctDtTm = value if type(value) != auto else self.make_default("ClrRctDtTm")

	@ClrRctDtTm.deleter
	def ClrRctDtTm(self):
		del self._ClrRctDtTm
		self._ClrRctDtTm = None

	@property
	def OrgnlIdr(self):
		return self._OrgnlIdr

	@OrgnlIdr.setter
	def OrgnlIdr(self, value):
		self._OrgnlIdr = value if type(value) != auto else self.make_default("OrgnlIdr")

	@OrgnlIdr.deleter
	def OrgnlIdr(self):
		del self._OrgnlIdr
		self._OrgnlIdr = None

	@property
	def OrgnlTradRpstryIdr(self):
		return self._OrgnlTradRpstryIdr

	@OrgnlTradRpstryIdr.setter
	def OrgnlTradRpstryIdr(self, value):
		self._OrgnlTradRpstryIdr = value if type(value) != auto else self.make_default("OrgnlTradRpstryIdr")

	@OrgnlTradRpstryIdr.deleter
	def OrgnlTradRpstryIdr(self):
		del self._OrgnlTradRpstryIdr
		self._OrgnlTradRpstryIdr = None

	@property
	def ClrDtTm(self):
		return self._ClrDtTm

	@ClrDtTm.setter
	def ClrDtTm(self, value):
		self._ClrDtTm = value if type(value) != auto else self.make_default("ClrDtTm")

	@ClrDtTm.deleter
	def ClrDtTm(self):
		del self._ClrDtTm
		self._ClrDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrIdr', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAcctOrgn', type=ClearingAccountType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrRctDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlIdr', type=UniqueTransactionIdentifier2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTradRpstryIdr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

