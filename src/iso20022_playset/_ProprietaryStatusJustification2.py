# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max256Text
from . import Max4AlphaNumericText

class ProprietaryStatusJustification2(base_types._BaseFieldType):

	__slots__ = ["_PrtryStsRsn", "_Rsn"]
	@property
	def PrtryStsRsn(self):
		return self._PrtryStsRsn

	@PrtryStsRsn.setter
	def PrtryStsRsn(self, value):
		self._PrtryStsRsn = value if value is not None else base_types.UninitialisedField(self, 'PrtryStsRsn', Max4AlphaNumericText, False)

	@PrtryStsRsn.deleter
	def PrtryStsRsn(self):
		del self._PrtryStsRsn
		self._PrtryStsRsn = base_types.UninitialisedField(self, 'PrtryStsRsn', Max4AlphaNumericText, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', Max256Text, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryStsRsn', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))