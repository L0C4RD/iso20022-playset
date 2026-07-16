# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndPlaceOfBirth1
from . import GenericPersonIdentification2

class PersonIdentification18(base_types._BaseFieldType):

	__slots__ = ["_DtAndPlcOfBirth", "_Othr"]
	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth1, False)

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = base_types.UninitialisedField(self, 'DtAndPlcOfBirth', DateAndPlaceOfBirth1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericPersonIdentification2, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericPersonIdentification2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=DateAndPlaceOfBirth1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification2, min=0, max=None, mutex_group=None, array=True),
	))