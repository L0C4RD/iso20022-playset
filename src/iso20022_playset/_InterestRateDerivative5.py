# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._BondDerivative2 import BondDerivative2
from ._FloatingInterestRate8 import FloatingInterestRate8
from ._ISODate import ISODate
from ._InflationIndex1Choice import InflationIndex1Choice
from ._InterestRateDerivative2Choice import InterestRateDerivative2Choice

class InterestRateDerivative5(base_types._BaseFieldType):

	__slots__ = ["_InfltnIndx", "_IntrstRateRef", "_SwptnNtnlCcy", "_UndrlygBd", "_UndrlygSwpMtrtyDt", "_UndrlygTp"]
	@property
	def InfltnIndx(self):
		return self._InfltnIndx

	@InfltnIndx.setter
	def InfltnIndx(self, value):
		self._InfltnIndx = value if type(value) != base_types.auto else self.make_default("InfltnIndx")

	@InfltnIndx.deleter
	def InfltnIndx(self):
		del self._InfltnIndx
		self._InfltnIndx = None

	@property
	def IntrstRateRef(self):
		return self._IntrstRateRef

	@IntrstRateRef.setter
	def IntrstRateRef(self, value):
		self._IntrstRateRef = value if type(value) != base_types.auto else self.make_default("IntrstRateRef")

	@IntrstRateRef.deleter
	def IntrstRateRef(self):
		del self._IntrstRateRef
		self._IntrstRateRef = None

	@property
	def SwptnNtnlCcy(self):
		return self._SwptnNtnlCcy

	@SwptnNtnlCcy.setter
	def SwptnNtnlCcy(self, value):
		self._SwptnNtnlCcy = value if type(value) != base_types.auto else self.make_default("SwptnNtnlCcy")

	@SwptnNtnlCcy.deleter
	def SwptnNtnlCcy(self):
		del self._SwptnNtnlCcy
		self._SwptnNtnlCcy = None

	@property
	def UndrlygBd(self):
		return self._UndrlygBd

	@UndrlygBd.setter
	def UndrlygBd(self, value):
		self._UndrlygBd = value if type(value) != base_types.auto else self.make_default("UndrlygBd")

	@UndrlygBd.deleter
	def UndrlygBd(self):
		del self._UndrlygBd
		self._UndrlygBd = None

	@property
	def UndrlygSwpMtrtyDt(self):
		return self._UndrlygSwpMtrtyDt

	@UndrlygSwpMtrtyDt.setter
	def UndrlygSwpMtrtyDt(self, value):
		self._UndrlygSwpMtrtyDt = value if type(value) != base_types.auto else self.make_default("UndrlygSwpMtrtyDt")

	@UndrlygSwpMtrtyDt.deleter
	def UndrlygSwpMtrtyDt(self):
		del self._UndrlygSwpMtrtyDt
		self._UndrlygSwpMtrtyDt = None

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if type(value) != base_types.auto else self.make_default("UndrlygTp")

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfltnIndx', type=InflationIndex1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateRef', type=FloatingInterestRate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SwptnNtnlCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygBd', type=BondDerivative2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygSwpMtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=InterestRateDerivative2Choice, min=1, max=1, mutex_group=None, array=False),
	))