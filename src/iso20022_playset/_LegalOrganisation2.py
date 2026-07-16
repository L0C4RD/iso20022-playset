# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max140Text
from . import Max35Text

class LegalOrganisation2(base_types._BaseFieldType):

	__slots__ = ["_EstblishmtDt", "_Id", "_Nm", "_RegnDt"]
	@property
	def EstblishmtDt(self):
		return self._EstblishmtDt

	@EstblishmtDt.setter
	def EstblishmtDt(self, value):
		self._EstblishmtDt = value if value is not None else base_types.UninitialisedField(self, 'EstblishmtDt', ISODate, False)

	@EstblishmtDt.deleter
	def EstblishmtDt(self):
		del self._EstblishmtDt
		self._EstblishmtDt = base_types.UninitialisedField(self, 'EstblishmtDt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if value is not None else base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EstblishmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))