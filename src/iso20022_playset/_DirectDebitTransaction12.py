from . import base_types
from ._ISODate import ISODate
from ._MandateRelatedInformation16 import MandateRelatedInformation16
from ._Max35Text import Max35Text
from ._PartyIdentification272 import PartyIdentification272

class DirectDebitTransaction12(base_types._BaseFieldType):

	__slots__ = ["_CdtrSchmeId", "_MndtRltdInf", "_PreNtfctnDt", "_PreNtfctnId"]
	@property
	def CdtrSchmeId(self):
		return self._CdtrSchmeId

	@CdtrSchmeId.setter
	def CdtrSchmeId(self, value):
		self._CdtrSchmeId = value if type(value) != base_types.auto else self.make_default("CdtrSchmeId")

	@CdtrSchmeId.deleter
	def CdtrSchmeId(self):
		del self._CdtrSchmeId
		self._CdtrSchmeId = None

	@property
	def MndtRltdInf(self):
		return self._MndtRltdInf

	@MndtRltdInf.setter
	def MndtRltdInf(self, value):
		self._MndtRltdInf = value if type(value) != base_types.auto else self.make_default("MndtRltdInf")

	@MndtRltdInf.deleter
	def MndtRltdInf(self):
		del self._MndtRltdInf
		self._MndtRltdInf = None

	@property
	def PreNtfctnDt(self):
		return self._PreNtfctnDt

	@PreNtfctnDt.setter
	def PreNtfctnDt(self, value):
		self._PreNtfctnDt = value if type(value) != base_types.auto else self.make_default("PreNtfctnDt")

	@PreNtfctnDt.deleter
	def PreNtfctnDt(self):
		del self._PreNtfctnDt
		self._PreNtfctnDt = None

	@property
	def PreNtfctnId(self):
		return self._PreNtfctnId

	@PreNtfctnId.setter
	def PreNtfctnId(self, value):
		self._PreNtfctnId = value if type(value) != base_types.auto else self.make_default("PreNtfctnId")

	@PreNtfctnId.deleter
	def PreNtfctnId(self):
		del self._PreNtfctnId
		self._PreNtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtRltdInf', type=MandateRelatedInformation16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreNtfctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreNtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

