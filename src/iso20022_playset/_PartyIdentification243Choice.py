# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import GenericIdentification30

class PartyIdentification243Choice(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_PrtryId"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if value is not None else base_types.UninitialisedField(self, 'BIC', AnyBICDec2014Identifier, False)

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = base_types.UninitialisedField(self, 'BIC', AnyBICDec2014Identifier, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))