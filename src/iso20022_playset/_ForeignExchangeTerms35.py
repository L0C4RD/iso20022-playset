# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._BaseOneRate import BaseOneRate
from ._ISODateTime import ISODateTime
from ._PartyIdentification137Choice import PartyIdentification137Choice

class ForeignExchangeTerms35(base_types._BaseFieldType):

	__slots__ = ["_QtdCcy", "_QtgInstn", "_QtnDt", "_UnitCcy", "_XchgRate"]
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
	def QtgInstn(self):
		return self._QtgInstn

	@QtgInstn.setter
	def QtgInstn(self, value):
		self._QtgInstn = value if type(value) != base_types.auto else self.make_default("QtgInstn")

	@QtgInstn.deleter
	def QtgInstn(self):
		del self._QtgInstn
		self._QtgInstn = None

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != base_types.auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

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

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtdCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtgInstn', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))