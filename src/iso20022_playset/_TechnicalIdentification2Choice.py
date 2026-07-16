# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICFIDec2014Identifier
from . import Max256Text

class TechnicalIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_TechAdr"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if value is not None else base_types.UninitialisedField(self, 'BICFI', BICFIDec2014Identifier, False)

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = base_types.UninitialisedField(self, 'BICFI', BICFIDec2014Identifier, False)

	@property
	def TechAdr(self):
		return self._TechAdr

	@TechAdr.setter
	def TechAdr(self, value):
		self._TechAdr = value if value is not None else base_types.UninitialisedField(self, 'TechAdr', Max256Text, False)

	@TechAdr.deleter
	def TechAdr(self):
		del self._TechAdr
		self._TechAdr = base_types.UninitialisedField(self, 'TechAdr', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TechAdr', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
	))