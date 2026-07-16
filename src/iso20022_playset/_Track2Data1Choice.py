# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max19HexBinaryText
from . import Max37Text

class Track2Data1Choice(base_types._BaseFieldType):

	__slots__ = ["_HexBinryVal", "_TxtVal"]
	@property
	def HexBinryVal(self):
		return self._HexBinryVal

	@HexBinryVal.setter
	def HexBinryVal(self, value):
		self._HexBinryVal = value if value is not None else base_types.UninitialisedField(self, 'HexBinryVal', Max19HexBinaryText, False)

	@HexBinryVal.deleter
	def HexBinryVal(self):
		del self._HexBinryVal
		self._HexBinryVal = base_types.UninitialisedField(self, 'HexBinryVal', Max19HexBinaryText, False)

	@property
	def TxtVal(self):
		return self._TxtVal

	@TxtVal.setter
	def TxtVal(self, value):
		self._TxtVal = value if value is not None else base_types.UninitialisedField(self, 'TxtVal', Max37Text, False)

	@TxtVal.deleter
	def TxtVal(self):
		del self._TxtVal
		self._TxtVal = base_types.UninitialisedField(self, 'TxtVal', Max37Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HexBinryVal', type=Max19HexBinaryText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxtVal', type=Max37Text, min=0, max=1, mutex_group=1, array=False),
	))