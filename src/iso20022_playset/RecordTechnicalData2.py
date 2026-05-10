from . import base_types
from .CancelledStatusReason15Code import CancelledStatusReason15Code
from .ISODateTime import ISODateTime

class RecordTechnicalData2(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_RctDtTm"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def RctDtTm(self):
		return self._RctDtTm

	@RctDtTm.setter
	def RctDtTm(self, value):
		self._RctDtTm = value if type(value) != base_types.auto else self.make_default("RctDtTm")

	@RctDtTm.deleter
	def RctDtTm(self):
		del self._RctDtTm
		self._RctDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=CancelledStatusReason15Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

