# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOMonth
from . import ISOYear
from . import SystemAndCurrency1

class CalendarSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Mnth", "_Svc", "_Yr"]
	@property
	def Mnth(self):
		return self._Mnth

	@Mnth.setter
	def Mnth(self, value):
		self._Mnth = value if value is not None else base_types.UninitialisedField(self, 'Mnth', ISOMonth, False)

	@Mnth.deleter
	def Mnth(self):
		del self._Mnth
		self._Mnth = base_types.UninitialisedField(self, 'Mnth', ISOMonth, False)

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if value is not None else base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	@property
	def Yr(self):
		return self._Yr

	@Yr.setter
	def Yr(self, value):
		self._Yr = value if value is not None else base_types.UninitialisedField(self, 'Yr', ISOYear, False)

	@Yr.deleter
	def Yr(self):
		del self._Yr
		self._Yr = base_types.UninitialisedField(self, 'Yr', ISOYear, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mnth', type=ISOMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
	))