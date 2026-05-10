from . import base_types
from ._BaseOneRate import BaseOneRate
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._UUIDv4Identifier import UUIDv4Identifier
from ._ISODateTime import ISODateTime

class CurrencyExchange26(base_types._BaseFieldType):

	__slots__ = ["_QtdCcy", "_QtId", "_PreAgrdXchgRate", "_FXAgt", "_QtnDtTm", "_UnitCcy"]
	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if type(value) != base_types.auto else self.make_default("QtdCcy")

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = None

	@property
	def QtId(self):
		return self._QtId

	@QtId.setter
	def QtId(self, value):
		self._QtId = value if type(value) != base_types.auto else self.make_default("QtId")

	@QtId.deleter
	def QtId(self):
		del self._QtId
		self._QtId = None

	@property
	def PreAgrdXchgRate(self):
		return self._PreAgrdXchgRate

	@PreAgrdXchgRate.setter
	def PreAgrdXchgRate(self, value):
		self._PreAgrdXchgRate = value if type(value) != base_types.auto else self.make_default("PreAgrdXchgRate")

	@PreAgrdXchgRate.deleter
	def PreAgrdXchgRate(self):
		del self._PreAgrdXchgRate
		self._PreAgrdXchgRate = None

	@property
	def FXAgt(self):
		return self._FXAgt

	@FXAgt.setter
	def FXAgt(self, value):
		self._FXAgt = value if type(value) != base_types.auto else self.make_default("FXAgt")

	@FXAgt.deleter
	def FXAgt(self):
		del self._FXAgt
		self._FXAgt = None

	@property
	def QtnDtTm(self):
		return self._QtnDtTm

	@QtnDtTm.setter
	def QtnDtTm(self, value):
		self._QtnDtTm = value if type(value) != base_types.auto else self.make_default("QtnDtTm")

	@QtnDtTm.deleter
	def QtnDtTm(self):
		del self._QtnDtTm
		self._QtnDtTm = None

	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if type(value) != base_types.auto else self.make_default("UnitCcy")

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtId', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreAgrdXchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

