# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class MultimodalTransport3(base_types._BaseFieldType):

	__slots__ = ["_PlcOfFnlDstn", "_TakngInChrg"]
	@property
	def PlcOfFnlDstn(self):
		return self._PlcOfFnlDstn

	@PlcOfFnlDstn.setter
	def PlcOfFnlDstn(self, value):
		self._PlcOfFnlDstn = value if value is not None else base_types.UninitialisedField(self, 'PlcOfFnlDstn', Max35Text, False)

	@PlcOfFnlDstn.deleter
	def PlcOfFnlDstn(self):
		del self._PlcOfFnlDstn
		self._PlcOfFnlDstn = base_types.UninitialisedField(self, 'PlcOfFnlDstn', Max35Text, False)

	@property
	def TakngInChrg(self):
		return self._TakngInChrg

	@TakngInChrg.setter
	def TakngInChrg(self, value):
		self._TakngInChrg = value if value is not None else base_types.UninitialisedField(self, 'TakngInChrg', Max35Text, False)

	@TakngInChrg.deleter
	def TakngInChrg(self):
		del self._TakngInChrg
		self._TakngInChrg = base_types.UninitialisedField(self, 'TakngInChrg', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfFnlDstn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TakngInChrg', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))