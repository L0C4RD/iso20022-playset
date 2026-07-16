# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import BondDerivative2
from . import FloatingInterestRate8
from . import ISODate
from . import InflationIndex1Choice
from . import InterestRateDerivative2Choice

class InterestRateDerivative5(base_types._BaseFieldType):

	__slots__ = ["_InfltnIndx", "_IntrstRateRef", "_SwptnNtnlCcy", "_UndrlygBd", "_UndrlygSwpMtrtyDt", "_UndrlygTp"]
	@property
	def InfltnIndx(self):
		return self._InfltnIndx

	@InfltnIndx.setter
	def InfltnIndx(self, value):
		self._InfltnIndx = value if value is not None else base_types.UninitialisedField(self, 'InfltnIndx', InflationIndex1Choice, False)

	@InfltnIndx.deleter
	def InfltnIndx(self):
		del self._InfltnIndx
		self._InfltnIndx = base_types.UninitialisedField(self, 'InfltnIndx', InflationIndex1Choice, False)

	@property
	def IntrstRateRef(self):
		return self._IntrstRateRef

	@IntrstRateRef.setter
	def IntrstRateRef(self, value):
		self._IntrstRateRef = value if value is not None else base_types.UninitialisedField(self, 'IntrstRateRef', FloatingInterestRate8, False)

	@IntrstRateRef.deleter
	def IntrstRateRef(self):
		del self._IntrstRateRef
		self._IntrstRateRef = base_types.UninitialisedField(self, 'IntrstRateRef', FloatingInterestRate8, False)

	@property
	def SwptnNtnlCcy(self):
		return self._SwptnNtnlCcy

	@SwptnNtnlCcy.setter
	def SwptnNtnlCcy(self, value):
		self._SwptnNtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'SwptnNtnlCcy', ActiveCurrencyCode, False)

	@SwptnNtnlCcy.deleter
	def SwptnNtnlCcy(self):
		del self._SwptnNtnlCcy
		self._SwptnNtnlCcy = base_types.UninitialisedField(self, 'SwptnNtnlCcy', ActiveCurrencyCode, False)

	@property
	def UndrlygBd(self):
		return self._UndrlygBd

	@UndrlygBd.setter
	def UndrlygBd(self, value):
		self._UndrlygBd = value if value is not None else base_types.UninitialisedField(self, 'UndrlygBd', BondDerivative2, False)

	@UndrlygBd.deleter
	def UndrlygBd(self):
		del self._UndrlygBd
		self._UndrlygBd = base_types.UninitialisedField(self, 'UndrlygBd', BondDerivative2, False)

	@property
	def UndrlygSwpMtrtyDt(self):
		return self._UndrlygSwpMtrtyDt

	@UndrlygSwpMtrtyDt.setter
	def UndrlygSwpMtrtyDt(self, value):
		self._UndrlygSwpMtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'UndrlygSwpMtrtyDt', ISODate, False)

	@UndrlygSwpMtrtyDt.deleter
	def UndrlygSwpMtrtyDt(self):
		del self._UndrlygSwpMtrtyDt
		self._UndrlygSwpMtrtyDt = base_types.UninitialisedField(self, 'UndrlygSwpMtrtyDt', ISODate, False)

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if value is not None else base_types.UninitialisedField(self, 'UndrlygTp', InterestRateDerivative2Choice, False)

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = base_types.UninitialisedField(self, 'UndrlygTp', InterestRateDerivative2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfltnIndx', type=InflationIndex1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateRef', type=FloatingInterestRate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwptnNtnlCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygBd', type=BondDerivative2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygSwpMtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=InterestRateDerivative2Choice, min=1, max=1, mutex_group=None, array=False),
	))