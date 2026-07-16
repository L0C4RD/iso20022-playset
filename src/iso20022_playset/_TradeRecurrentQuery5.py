# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max1000Text
from . import TradeQueryExecutionFrequency3

class TradeRecurrentQuery5(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_QryTp", "_VldUntil"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', TradeQueryExecutionFrequency3, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', TradeQueryExecutionFrequency3, False)

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', Max1000Text, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', Max1000Text, False)

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if value is not None else base_types.UninitialisedField(self, 'VldUntil', ISODate, False)

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = base_types.UninitialisedField(self, 'VldUntil', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=TradeQueryExecutionFrequency3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTp', type=Max1000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))