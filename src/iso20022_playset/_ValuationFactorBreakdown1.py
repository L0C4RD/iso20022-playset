# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate

class ValuationFactorBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_Hrcut", "_InfltnFctr", "_PoolFctr", "_ValtnFctr"]
	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', BaseOneRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', BaseOneRate, False)

	@property
	def InfltnFctr(self):
		return self._InfltnFctr

	@InfltnFctr.setter
	def InfltnFctr(self, value):
		self._InfltnFctr = value if value is not None else base_types.UninitialisedField(self, 'InfltnFctr', BaseOneRate, False)

	@InfltnFctr.deleter
	def InfltnFctr(self):
		del self._InfltnFctr
		self._InfltnFctr = base_types.UninitialisedField(self, 'InfltnFctr', BaseOneRate, False)

	@property
	def PoolFctr(self):
		return self._PoolFctr

	@PoolFctr.setter
	def PoolFctr(self, value):
		self._PoolFctr = value if value is not None else base_types.UninitialisedField(self, 'PoolFctr', BaseOneRate, False)

	@PoolFctr.deleter
	def PoolFctr(self):
		del self._PoolFctr
		self._PoolFctr = base_types.UninitialisedField(self, 'PoolFctr', BaseOneRate, False)

	@property
	def ValtnFctr(self):
		return self._ValtnFctr

	@ValtnFctr.setter
	def ValtnFctr(self, value):
		self._ValtnFctr = value if value is not None else base_types.UninitialisedField(self, 'ValtnFctr', BaseOneRate, False)

	@ValtnFctr.deleter
	def ValtnFctr(self):
		del self._ValtnFctr
		self._ValtnFctr = base_types.UninitialisedField(self, 'ValtnFctr', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrcut', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfltnFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))