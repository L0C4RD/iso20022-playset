# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ISODate
from . import SettlementRateSource1

class OpeningConditions1(base_types._BaseFieldType):

	__slots__ = ["_SttlmCcy", "_SttlmRateSrc", "_ValtnDt"]
	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def SttlmRateSrc(self):
		return self._SttlmRateSrc

	@SttlmRateSrc.setter
	def SttlmRateSrc(self, value):
		self._SttlmRateSrc = value if value is not None else base_types.UninitialisedField(self, 'SttlmRateSrc', SettlementRateSource1, False)

	@SttlmRateSrc.deleter
	def SttlmRateSrc(self):
		del self._SttlmRateSrc
		self._SttlmRateSrc = base_types.UninitialisedField(self, 'SttlmRateSrc', SettlementRateSource1, False)

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDt', ISODate, False)

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = base_types.UninitialisedField(self, 'ValtnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmRateSrc', type=SettlementRateSource1, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))