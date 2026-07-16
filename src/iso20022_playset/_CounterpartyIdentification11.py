# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Branch5Choice
from . import CollateralRole1Code
from . import CounterpartyTradeNature7Choice
from . import OrganisationIdentification15Choice

class CounterpartyIdentification11(base_types._BaseFieldType):

	__slots__ = ["_Brnch", "_Id", "_Ntr", "_Sd"]
	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if value is not None else base_types.UninitialisedField(self, 'Brnch', Branch5Choice, False)

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = base_types.UninitialisedField(self, 'Brnch', Branch5Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', OrganisationIdentification15Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', OrganisationIdentification15Choice, False)

	@property
	def Ntr(self):
		return self._Ntr

	@Ntr.setter
	def Ntr(self, value):
		self._Ntr = value if value is not None else base_types.UninitialisedField(self, 'Ntr', CounterpartyTradeNature7Choice, False)

	@Ntr.deleter
	def Ntr(self):
		del self._Ntr
		self._Ntr = base_types.UninitialisedField(self, 'Ntr', CounterpartyTradeNature7Choice, False)

	@property
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if value is not None else base_types.UninitialisedField(self, 'Sd', CollateralRole1Code, False)

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = base_types.UninitialisedField(self, 'Sd', CollateralRole1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brnch', type=Branch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntr', type=CounterpartyTradeNature7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
	))