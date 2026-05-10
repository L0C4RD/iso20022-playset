from . import base_types
from .ISODateTime import ISODateTime

class SettlementDateTimeIndication1(base_types._BaseFieldType):

	__slots__ = ["_DbtDtTm", "_CdtDtTm"]
	@property
	def DbtDtTm(self):
		return self._DbtDtTm

	@DbtDtTm.setter
	def DbtDtTm(self, value):
		self._DbtDtTm = value if type(value) != auto else self.make_default("DbtDtTm")

	@DbtDtTm.deleter
	def DbtDtTm(self):
		del self._DbtDtTm
		self._DbtDtTm = None

	@property
	def CdtDtTm(self):
		return self._CdtDtTm

	@CdtDtTm.setter
	def CdtDtTm(self, value):
		self._CdtDtTm = value if type(value) != auto else self.make_default("CdtDtTm")

	@CdtDtTm.deleter
	def CdtDtTm(self):
		del self._CdtDtTm
		self._CdtDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

