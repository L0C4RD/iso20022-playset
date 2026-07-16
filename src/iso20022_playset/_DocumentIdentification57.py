# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class DocumentIdentification57(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnInstrId", "_PrcrInstrId"]
	@property
	def BuyrPrtcnInstrId(self):
		return self._BuyrPrtcnInstrId

	@BuyrPrtcnInstrId.setter
	def BuyrPrtcnInstrId(self, value):
		self._BuyrPrtcnInstrId = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrId', Max35Text, False)

	@BuyrPrtcnInstrId.deleter
	def BuyrPrtcnInstrId(self):
		del self._BuyrPrtcnInstrId
		self._BuyrPrtcnInstrId = base_types.UninitialisedField(self, 'BuyrPrtcnInstrId', Max35Text, False)

	@property
	def PrcrInstrId(self):
		return self._PrcrInstrId

	@PrcrInstrId.setter
	def PrcrInstrId(self, value):
		self._PrcrInstrId = value if value is not None else base_types.UninitialisedField(self, 'PrcrInstrId', Max35Text, False)

	@PrcrInstrId.deleter
	def PrcrInstrId(self):
		del self._PrcrInstrId
		self._PrcrInstrId = base_types.UninitialisedField(self, 'PrcrInstrId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrPrtcnInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))