# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import BranchAndFinancialInstitutionIdentification8
from . import ISODateTime
from . import UUIDv4Identifier

class CurrencyExchange26(base_types._BaseFieldType):

	__slots__ = ["_FXAgt", "_PreAgrdXchgRate", "_QtId", "_QtdCcy", "_QtnDtTm", "_UnitCcy"]
	@property
	def FXAgt(self):
		return self._FXAgt

	@FXAgt.setter
	def FXAgt(self, value):
		self._FXAgt = value if value is not None else base_types.UninitialisedField(self, 'FXAgt', BranchAndFinancialInstitutionIdentification8, False)

	@FXAgt.deleter
	def FXAgt(self):
		del self._FXAgt
		self._FXAgt = base_types.UninitialisedField(self, 'FXAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def PreAgrdXchgRate(self):
		return self._PreAgrdXchgRate

	@PreAgrdXchgRate.setter
	def PreAgrdXchgRate(self, value):
		self._PreAgrdXchgRate = value if value is not None else base_types.UninitialisedField(self, 'PreAgrdXchgRate', BaseOneRate, False)

	@PreAgrdXchgRate.deleter
	def PreAgrdXchgRate(self):
		del self._PreAgrdXchgRate
		self._PreAgrdXchgRate = base_types.UninitialisedField(self, 'PreAgrdXchgRate', BaseOneRate, False)

	@property
	def QtId(self):
		return self._QtId

	@QtId.setter
	def QtId(self, value):
		self._QtId = value if value is not None else base_types.UninitialisedField(self, 'QtId', UUIDv4Identifier, False)

	@QtId.deleter
	def QtId(self):
		del self._QtId
		self._QtId = base_types.UninitialisedField(self, 'QtId', UUIDv4Identifier, False)

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if value is not None else base_types.UninitialisedField(self, 'QtdCcy', ActiveOrHistoricCurrencyCode, False)

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = base_types.UninitialisedField(self, 'QtdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def QtnDtTm(self):
		return self._QtnDtTm

	@QtnDtTm.setter
	def QtnDtTm(self, value):
		self._QtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'QtnDtTm', ISODateTime, False)

	@QtnDtTm.deleter
	def QtnDtTm(self):
		del self._QtnDtTm
		self._QtnDtTm = base_types.UninitialisedField(self, 'QtnDtTm', ISODateTime, False)

	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if value is not None else base_types.UninitialisedField(self, 'UnitCcy', ActiveOrHistoricCurrencyCode, False)

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = base_types.UninitialisedField(self, 'UnitCcy', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FXAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreAgrdXchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtId', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))