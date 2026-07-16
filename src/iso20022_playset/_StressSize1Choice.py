# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Absolute1
from . import BaseOneRate

class StressSize1Choice(base_types._BaseFieldType):

	__slots__ = ["_Abs", "_Rltv"]
	@property
	def Abs(self):
		return self._Abs

	@Abs.setter
	def Abs(self, value):
		self._Abs = value if value is not None else base_types.UninitialisedField(self, 'Abs', Absolute1, False)

	@Abs.deleter
	def Abs(self):
		del self._Abs
		self._Abs = base_types.UninitialisedField(self, 'Abs', Absolute1, False)

	@property
	def Rltv(self):
		return self._Rltv

	@Rltv.setter
	def Rltv(self, value):
		self._Rltv = value if value is not None else base_types.UninitialisedField(self, 'Rltv', BaseOneRate, False)

	@Rltv.deleter
	def Rltv(self):
		del self._Rltv
		self._Rltv = base_types.UninitialisedField(self, 'Rltv', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Abs', type=Absolute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rltv', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
	))