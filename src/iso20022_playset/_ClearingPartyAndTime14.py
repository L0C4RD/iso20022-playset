# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max52Text
from . import OrganisationIdentification15Choice

class ClearingPartyAndTime14(base_types._BaseFieldType):

	__slots__ = ["_CCP", "_ClrDtTm", "_PrtflCd", "_RptTrckgNb"]
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
	def PrtflCd(self):
		return self._PrtflCd

	@PrtflCd.setter
	def PrtflCd(self, value):
		self._PrtflCd = value if value is not None else base_types.UninitialisedField(self, 'PrtflCd', Max52Text, False)

	@PrtflCd.deleter
	def PrtflCd(self):
		del self._PrtflCd
		self._PrtflCd = base_types.UninitialisedField(self, 'PrtflCd', Max52Text, False)

	@property
	def RptTrckgNb(self):
		return self._RptTrckgNb

	@RptTrckgNb.setter
	def RptTrckgNb(self, value):
		self._RptTrckgNb = value if value is not None else base_types.UninitialisedField(self, 'RptTrckgNb', Max52Text, False)

	@RptTrckgNb.deleter
	def RptTrckgNb(self):
		del self._RptTrckgNb
		self._RptTrckgNb = base_types.UninitialisedField(self, 'RptTrckgNb', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCP', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflCd', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTrckgNb', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
	))