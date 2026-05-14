# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._TrueFalseIndicator import TrueFalseIndicator

class CorrectionIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Ind", "_Tm"]
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
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if type(value) != base_types.auto else self.make_default("Ind")

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ind', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))