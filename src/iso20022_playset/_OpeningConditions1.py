from . import base_types
from ._ISODate import ISODate
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._SettlementRateSource1 import SettlementRateSource1

class OpeningConditions1(base_types._BaseFieldType):

	__slots__ = ["_SttlmCcy", "_SttlmRateSrc", "_ValtnDt"]
	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != base_types.auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def SttlmRateSrc(self):
		return self._SttlmRateSrc

	@SttlmRateSrc.setter
	def SttlmRateSrc(self, value):
		self._SttlmRateSrc = value if type(value) != base_types.auto else self.make_default("SttlmRateSrc")

	@SttlmRateSrc.deleter
	def SttlmRateSrc(self):
		del self._SttlmRateSrc
		self._SttlmRateSrc = None

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if type(value) != base_types.auto else self.make_default("ValtnDt")

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmRateSrc', type=SettlementRateSource1, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

