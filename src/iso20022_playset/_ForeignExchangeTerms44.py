# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BaseOneRate
from . import ISODateTime
from . import PartyIdentification139

class ForeignExchangeTerms44(base_types._BaseFieldType):

	__slots__ = ["_QtdCcy", "_QtgInstn", "_QtnDt", "_UnitCcy", "_XchgRate"]
	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if value is not None else base_types.UninitialisedField(self, 'QtdCcy', ActiveCurrencyCode, False)

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = base_types.UninitialisedField(self, 'QtdCcy', ActiveCurrencyCode, False)

	@property
	def QtgInstn(self):
		return self._QtgInstn

	@QtgInstn.setter
	def QtgInstn(self, value):
		self._QtgInstn = value if value is not None else base_types.UninitialisedField(self, 'QtgInstn', PartyIdentification139, False)

	@QtgInstn.deleter
	def QtgInstn(self):
		del self._QtgInstn
		self._QtgInstn = base_types.UninitialisedField(self, 'QtgInstn', PartyIdentification139, False)

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if value is not None else base_types.UninitialisedField(self, 'UnitCcy', ActiveCurrencyCode, False)

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = base_types.UninitialisedField(self, 'UnitCcy', ActiveCurrencyCode, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtdCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtgInstn', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))