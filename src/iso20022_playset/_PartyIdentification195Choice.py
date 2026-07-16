# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import GenericIdentification36
from . import LEIIdentifier

class PartyIdentification195Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_LEI", "_PrtryId"]
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
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))