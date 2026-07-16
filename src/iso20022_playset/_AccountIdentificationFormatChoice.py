# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification1
from . import AccountIdentification3
from . import AccountIdentificationAndPurpose

class AccountIdentificationFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_IdAndPurp", "_IdAsDSS", "_SmplId"]
	@property
	def IdAndPurp(self):
		return self._IdAndPurp

	@IdAndPurp.setter
	def IdAndPurp(self, value):
		self._IdAndPurp = value if value is not None else base_types.UninitialisedField(self, 'IdAndPurp', AccountIdentificationAndPurpose, False)

	@IdAndPurp.deleter
	def IdAndPurp(self):
		del self._IdAndPurp
		self._IdAndPurp = base_types.UninitialisedField(self, 'IdAndPurp', AccountIdentificationAndPurpose, False)

	@property
	def IdAsDSS(self):
		return self._IdAsDSS

	@IdAsDSS.setter
	def IdAsDSS(self, value):
		self._IdAsDSS = value if value is not None else base_types.UninitialisedField(self, 'IdAsDSS', AccountIdentification3, False)

	@IdAsDSS.deleter
	def IdAsDSS(self):
		del self._IdAsDSS
		self._IdAsDSS = base_types.UninitialisedField(self, 'IdAsDSS', AccountIdentification3, False)

	@property
	def SmplId(self):
		return self._SmplId

	@SmplId.setter
	def SmplId(self, value):
		self._SmplId = value if value is not None else base_types.UninitialisedField(self, 'SmplId', AccountIdentification1, False)

	@SmplId.deleter
	def SmplId(self):
		del self._SmplId
		self._SmplId = base_types.UninitialisedField(self, 'SmplId', AccountIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdAndPurp', type=AccountIdentificationAndPurpose, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsDSS', type=AccountIdentification3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SmplId', type=AccountIdentification1, min=0, max=1, mutex_group=1, array=False),
	))