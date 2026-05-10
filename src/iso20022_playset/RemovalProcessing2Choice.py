from . import base_types
from .CountryCode import CountryCode
from .SecurityIdentification19 import SecurityIdentification19
from .GenericIdentification37 import GenericIdentification37

class RemovalProcessing2Choice(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_IssrCtry", "_IndxId"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def IssrCtry(self):
		return self._IssrCtry

	@IssrCtry.setter
	def IssrCtry(self, value):
		self._IssrCtry = value if type(value) != auto else self.make_default("IssrCtry")

	@IssrCtry.deleter
	def IssrCtry(self):
		del self._IssrCtry
		self._IssrCtry = None

	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if type(value) != auto else self.make_default("IndxId")

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrCtry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxId', type=GenericIdentification37, min=0, max=1, mutex_group=1, array=False),
	))

