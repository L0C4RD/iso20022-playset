# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import Max50Text

class Reconciliation5(base_types._BaseFieldType):

	__slots__ = ["_ChckptRef", "_Dt", "_Id"]
	@property
	def ChckptRef(self):
		return self._ChckptRef

	@ChckptRef.setter
	def ChckptRef(self, value):
		self._ChckptRef = value if value is not None else base_types.UninitialisedField(self, 'ChckptRef', Max35Text, False)

	@ChckptRef.deleter
	def ChckptRef(self):
		del self._ChckptRef
		self._ChckptRef = base_types.UninitialisedField(self, 'ChckptRef', Max35Text, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max50Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max50Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChckptRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))