# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationData2
from . import InternalisationDataRate1

class InternalisationData1(base_types._BaseFieldType):

	__slots__ = ["_Aggt", "_FaildRate"]
	@property
	def Aggt(self):
		return self._Aggt

	@Aggt.setter
	def Aggt(self, value):
		self._Aggt = value if value is not None else base_types.UninitialisedField(self, 'Aggt', InternalisationData2, False)

	@Aggt.deleter
	def Aggt(self):
		del self._Aggt
		self._Aggt = base_types.UninitialisedField(self, 'Aggt', InternalisationData2, False)

	@property
	def FaildRate(self):
		return self._FaildRate

	@FaildRate.setter
	def FaildRate(self, value):
		self._FaildRate = value if value is not None else base_types.UninitialisedField(self, 'FaildRate', InternalisationDataRate1, False)

	@FaildRate.deleter
	def FaildRate(self):
		del self._FaildRate
		self._FaildRate = base_types.UninitialisedField(self, 'FaildRate', InternalisationDataRate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Aggt', type=InternalisationData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildRate', type=InternalisationDataRate1, min=1, max=1, mutex_group=None, array=False),
	))