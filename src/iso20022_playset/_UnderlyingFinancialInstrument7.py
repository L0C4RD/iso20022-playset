# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAttributes124
from . import SecurityIdentification19

class UnderlyingFinancialInstrument7(base_types._BaseFieldType):

	__slots__ = ["_Attrbts", "_Id"]
	@property
	def Attrbts(self):
		return self._Attrbts

	@Attrbts.setter
	def Attrbts(self, value):
		self._Attrbts = value if value is not None else base_types.UninitialisedField(self, 'Attrbts', FinancialInstrumentAttributes124, False)

	@Attrbts.deleter
	def Attrbts(self):
		del self._Attrbts
		self._Attrbts = base_types.UninitialisedField(self, 'Attrbts', FinancialInstrumentAttributes124, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification19, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification19, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attrbts', type=FinancialInstrumentAttributes124, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))