# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericAccountIdentification1
from . import IBAN2007Identifier

class AccountIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_IBAN", "_Othr"]
	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if value is not None else base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericAccountIdentification1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericAccountIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericAccountIdentification1, min=0, max=1, mutex_group=1, array=False),
	))