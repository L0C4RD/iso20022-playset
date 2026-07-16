# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import MandateRelatedInformation16
from . import Max35Text
from . import PartyIdentification272

class DirectDebitTransaction12(base_types._BaseFieldType):

	__slots__ = ["_CdtrSchmeId", "_MndtRltdInf", "_PreNtfctnDt", "_PreNtfctnId"]
	@property
	def CdtrSchmeId(self):
		return self._CdtrSchmeId

	@CdtrSchmeId.setter
	def CdtrSchmeId(self, value):
		self._CdtrSchmeId = value if value is not None else base_types.UninitialisedField(self, 'CdtrSchmeId', PartyIdentification272, False)

	@CdtrSchmeId.deleter
	def CdtrSchmeId(self):
		del self._CdtrSchmeId
		self._CdtrSchmeId = base_types.UninitialisedField(self, 'CdtrSchmeId', PartyIdentification272, False)

	@property
	def MndtRltdInf(self):
		return self._MndtRltdInf

	@MndtRltdInf.setter
	def MndtRltdInf(self, value):
		self._MndtRltdInf = value if value is not None else base_types.UninitialisedField(self, 'MndtRltdInf', MandateRelatedInformation16, False)

	@MndtRltdInf.deleter
	def MndtRltdInf(self):
		del self._MndtRltdInf
		self._MndtRltdInf = base_types.UninitialisedField(self, 'MndtRltdInf', MandateRelatedInformation16, False)

	@property
	def PreNtfctnDt(self):
		return self._PreNtfctnDt

	@PreNtfctnDt.setter
	def PreNtfctnDt(self, value):
		self._PreNtfctnDt = value if value is not None else base_types.UninitialisedField(self, 'PreNtfctnDt', ISODate, False)

	@PreNtfctnDt.deleter
	def PreNtfctnDt(self):
		del self._PreNtfctnDt
		self._PreNtfctnDt = base_types.UninitialisedField(self, 'PreNtfctnDt', ISODate, False)

	@property
	def PreNtfctnId(self):
		return self._PreNtfctnId

	@PreNtfctnId.setter
	def PreNtfctnId(self, value):
		self._PreNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'PreNtfctnId', Max35Text, False)

	@PreNtfctnId.deleter
	def PreNtfctnId(self):
		del self._PreNtfctnId
		self._PreNtfctnId = base_types.UninitialisedField(self, 'PreNtfctnId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtRltdInf', type=MandateRelatedInformation16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreNtfctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))