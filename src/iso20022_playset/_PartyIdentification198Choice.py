# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import GenericIdentification36
from . import LEIIdentifier
from . import Max35Text
from . import Max50Text

class PartyIdentification198Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_ClntId", "_LEI", "_NtlRegnNb", "_PrtryId"]
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
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if value is not None else base_types.UninitialisedField(self, 'ClntId', Max50Text, False)

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = base_types.UninitialisedField(self, 'ClntId', Max50Text, False)

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
	def NtlRegnNb(self):
		return self._NtlRegnNb

	@NtlRegnNb.setter
	def NtlRegnNb(self, value):
		self._NtlRegnNb = value if value is not None else base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

	@NtlRegnNb.deleter
	def NtlRegnNb(self):
		del self._NtlRegnNb
		self._NtlRegnNb = base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification36, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClntId', type=Max50Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))