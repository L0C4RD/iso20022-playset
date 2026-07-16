# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PartyIdentification43

class Presentation2(base_types._BaseFieldType):

	__slots__ = ["_BnfcryPresntnDt", "_Presntr"]
	@property
	def BnfcryPresntnDt(self):
		return self._BnfcryPresntnDt

	@BnfcryPresntnDt.setter
	def BnfcryPresntnDt(self, value):
		self._BnfcryPresntnDt = value if value is not None else base_types.UninitialisedField(self, 'BnfcryPresntnDt', ISODate, False)

	@BnfcryPresntnDt.deleter
	def BnfcryPresntnDt(self):
		del self._BnfcryPresntnDt
		self._BnfcryPresntnDt = base_types.UninitialisedField(self, 'BnfcryPresntnDt', ISODate, False)

	@property
	def Presntr(self):
		return self._Presntr

	@Presntr.setter
	def Presntr(self, value):
		self._Presntr = value if value is not None else base_types.UninitialisedField(self, 'Presntr', PartyIdentification43, False)

	@Presntr.deleter
	def Presntr(self):
		del self._Presntr
		self._Presntr = base_types.UninitialisedField(self, 'Presntr', PartyIdentification43, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryPresntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Presntr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
	))