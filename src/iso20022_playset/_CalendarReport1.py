# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalendarOrBusinessError1Choice
from . import SystemAndCurrency1

class CalendarReport1(base_types._BaseFieldType):

	__slots__ = ["_CalOrErr", "_Svc"]
	@property
	def CalOrErr(self):
		return self._CalOrErr

	@CalOrErr.setter
	def CalOrErr(self, value):
		self._CalOrErr = value if value is not None else base_types.UninitialisedField(self, 'CalOrErr', CalendarOrBusinessError1Choice, False)

	@CalOrErr.deleter
	def CalOrErr(self):
		del self._CalOrErr
		self._CalOrErr = base_types.UninitialisedField(self, 'CalOrErr', CalendarOrBusinessError1Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CalOrErr', type=CalendarOrBusinessError1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))