# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaseOneRate import BaseOneRate
from ._ISODate import ISODate

class ResetDateAndValue1(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Val"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))