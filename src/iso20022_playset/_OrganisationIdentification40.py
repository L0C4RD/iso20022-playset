# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import GenericOrganisationIdentification3
from . import LEIIdentifier
from . import Max256Text

class OrganisationIdentification40(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_EmailAdr", "_LEI", "_Othr"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericOrganisationIdentification3, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericOrganisationIdentification3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericOrganisationIdentification3, min=0, max=None, mutex_group=None, array=True),
	))