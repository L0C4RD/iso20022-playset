# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalPartyRole1Code
from . import LEIIdentifier
from . import MICIdentifier
from . import PersonIdentification10

class PersonOrOrganisation1Choice(base_types._BaseFieldType):

	__slots__ = ["_Intl", "_LEI", "_MIC", "_Prsn"]
	@property
	def Intl(self):
		return self._Intl

	@Intl.setter
	def Intl(self, value):
		self._Intl = value if value is not None else base_types.UninitialisedField(self, 'Intl', InternalPartyRole1Code, False)

	@Intl.deleter
	def Intl(self):
		del self._Intl
		self._Intl = base_types.UninitialisedField(self, 'Intl', InternalPartyRole1Code, False)

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
	def MIC(self):
		return self._MIC

	@MIC.setter
	def MIC(self, value):
		self._MIC = value if value is not None else base_types.UninitialisedField(self, 'MIC', MICIdentifier, False)

	@MIC.deleter
	def MIC(self):
		del self._MIC
		self._MIC = base_types.UninitialisedField(self, 'MIC', MICIdentifier, False)

	@property
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if value is not None else base_types.UninitialisedField(self, 'Prsn', PersonIdentification10, False)

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = base_types.UninitialisedField(self, 'Prsn', PersonIdentification10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intl', type=InternalPartyRole1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MIC', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prsn', type=PersonIdentification10, min=0, max=1, mutex_group=1, array=False),
	))