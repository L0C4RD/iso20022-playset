# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICIdentifier

class PartyIdentification3(base_types._BaseFieldType):

	__slots__ = ["_BICOrBEI"]
	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if value is not None else base_types.UninitialisedField(self, 'BICOrBEI', AnyBICIdentifier, False)

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = base_types.UninitialisedField(self, 'BICOrBEI', AnyBICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))