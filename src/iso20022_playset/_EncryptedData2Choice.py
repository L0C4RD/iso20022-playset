# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100KBinary
from . import Max9999HexBinaryText

class EncryptedData2Choice(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_HexBinry"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if value is not None else base_types.UninitialisedField(self, 'Binry', Max100KBinary, False)

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = base_types.UninitialisedField(self, 'Binry', Max100KBinary, False)

	@property
	def HexBinry(self):
		return self._HexBinry

	@HexBinry.setter
	def HexBinry(self, value):
		self._HexBinry = value if value is not None else base_types.UninitialisedField(self, 'HexBinry', Max9999HexBinaryText, False)

	@HexBinry.deleter
	def HexBinry(self):
		del self._HexBinry
		self._HexBinry = base_types.UninitialisedField(self, 'HexBinry', Max9999HexBinaryText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max100KBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HexBinry', type=Max9999HexBinaryText, min=0, max=1, mutex_group=1, array=False),
	))