# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import GenericPersonIdentification1

class PersonIdentification12(base_types._BaseFieldType):

	__slots__ = ["_CtryOfBrnch", "_Othr"]
	@property
	def CtryOfBrnch(self):
		return self._CtryOfBrnch

	@CtryOfBrnch.setter
	def CtryOfBrnch(self, value):
		self._CtryOfBrnch = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@CtryOfBrnch.deleter
	def CtryOfBrnch(self):
		del self._CtryOfBrnch
		self._CtryOfBrnch = base_types.UninitialisedField(self, 'CtryOfBrnch', CountryCode, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericPersonIdentification1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericPersonIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtryOfBrnch', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericPersonIdentification1, min=1, max=1, mutex_group=None, array=False),
	))