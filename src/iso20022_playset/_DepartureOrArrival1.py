# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._Max256Text import Max256Text
from ._Max70Text import Max70Text

class DepartureOrArrival1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Dt", "_Lctn", "_Tm"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

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
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != base_types.auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

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
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
	))