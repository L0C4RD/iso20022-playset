# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text

class DocumentIdentification57(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnInstrId", "_PrcrInstrId"]
	@property
	def BuyrPrtcnInstrId(self):
		return self._BuyrPrtcnInstrId

	@BuyrPrtcnInstrId.setter
	def BuyrPrtcnInstrId(self, value):
		self._BuyrPrtcnInstrId = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrId")

	@BuyrPrtcnInstrId.deleter
	def BuyrPrtcnInstrId(self):
		del self._BuyrPrtcnInstrId
		self._BuyrPrtcnInstrId = None

	@property
	def PrcrInstrId(self):
		return self._PrcrInstrId

	@PrcrInstrId.setter
	def PrcrInstrId(self, value):
		self._PrcrInstrId = value if type(value) != base_types.auto else self.make_default("PrcrInstrId")

	@PrcrInstrId.deleter
	def PrcrInstrId(self):
		del self._PrcrInstrId
		self._PrcrInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrPrtcnInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))