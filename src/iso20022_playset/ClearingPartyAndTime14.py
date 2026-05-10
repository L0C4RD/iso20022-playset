from . import base_types
from .OrganisationIdentification15Choice import OrganisationIdentification15Choice
from .ISODateTime import ISODateTime
from .Max52Text import Max52Text

class ClearingPartyAndTime14(base_types._BaseFieldType):

	__slots__ = ["_RptTrckgNb", "_ClrDtTm", "_CCP", "_PrtflCd"]
	@property
	def RptTrckgNb(self):
		return self._RptTrckgNb

	@RptTrckgNb.setter
	def RptTrckgNb(self, value):
		self._RptTrckgNb = value if type(value) != auto else self.make_default("RptTrckgNb")

	@RptTrckgNb.deleter
	def RptTrckgNb(self):
		del self._RptTrckgNb
		self._RptTrckgNb = None

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
	def PrtflCd(self):
		return self._PrtflCd

	@PrtflCd.setter
	def PrtflCd(self, value):
		self._PrtflCd = value if type(value) != auto else self.make_default("PrtflCd")

	@PrtflCd.deleter
	def PrtflCd(self):
		del self._PrtflCd
		self._PrtflCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptTrckgNb', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCd', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
	))

