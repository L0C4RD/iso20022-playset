# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import SupplementaryDataEnvelope1

class SupplementaryData1(base_types._BaseFieldType):

	__slots__ = ["_Envlp", "_PlcAndNm"]
	@property
	def Envlp(self):
		return self._Envlp

	@Envlp.setter
	def Envlp(self, value):
		self._Envlp = value if value is not None else base_types.UninitialisedField(self, 'Envlp', SupplementaryDataEnvelope1, False)

	@Envlp.deleter
	def Envlp(self):
		del self._Envlp
		self._Envlp = base_types.UninitialisedField(self, 'Envlp', SupplementaryDataEnvelope1, False)

	@property
	def PlcAndNm(self):
		return self._PlcAndNm

	@PlcAndNm.setter
	def PlcAndNm(self, value):
		self._PlcAndNm = value if value is not None else base_types.UninitialisedField(self, 'PlcAndNm', Max350Text, False)

	@PlcAndNm.deleter
	def PlcAndNm(self):
		del self._PlcAndNm
		self._PlcAndNm = base_types.UninitialisedField(self, 'PlcAndNm', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envlp', type=SupplementaryDataEnvelope1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcAndNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))