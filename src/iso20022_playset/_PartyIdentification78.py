# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationType1Code
from . import Max35Text

class PartyIdentification78(base_types._BaseFieldType):

	__slots__ = ["_PtySrc", "_TradPtyId"]
	@property
	def PtySrc(self):
		return self._PtySrc

	@PtySrc.setter
	def PtySrc(self, value):
		self._PtySrc = value if value is not None else base_types.UninitialisedField(self, 'PtySrc', IdentificationType1Code, False)

	@PtySrc.deleter
	def PtySrc(self):
		del self._PtySrc
		self._PtySrc = base_types.UninitialisedField(self, 'PtySrc', IdentificationType1Code, False)

	@property
	def TradPtyId(self):
		return self._TradPtyId

	@TradPtyId.setter
	def TradPtyId(self, value):
		self._TradPtyId = value if value is not None else base_types.UninitialisedField(self, 'TradPtyId', Max35Text, False)

	@TradPtyId.deleter
	def TradPtyId(self):
		del self._TradPtyId
		self._TradPtyId = base_types.UninitialisedField(self, 'TradPtyId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtySrc', type=IdentificationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPtyId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))