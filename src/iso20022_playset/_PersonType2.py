# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericPersonType1
from . import RequestedIndicator

class PersonType2(base_types._BaseFieldType):

	__slots__ = ["_DtAndPlcOfBirth", "_EmailAdr", "_Othr"]
	@property
	def DtAndPlcOfBirth(self):
		return self._DtAndPlcOfBirth

	@DtAndPlcOfBirth.setter
	def DtAndPlcOfBirth(self, value):
		self._DtAndPlcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtAndPlcOfBirth', RequestedIndicator, False)

	@DtAndPlcOfBirth.deleter
	def DtAndPlcOfBirth(self):
		del self._DtAndPlcOfBirth
		self._DtAndPlcOfBirth = base_types.UninitialisedField(self, 'DtAndPlcOfBirth', RequestedIndicator, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', RequestedIndicator, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', RequestedIndicator, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericPersonType1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericPersonType1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtAndPlcOfBirth', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericPersonType1, min=0, max=None, mutex_group=None, array=True),
	))