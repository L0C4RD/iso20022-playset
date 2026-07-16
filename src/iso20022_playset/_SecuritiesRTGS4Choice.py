# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import YesNoIndicator

class SecuritiesRTGS4Choice(base_types._BaseFieldType):

	__slots__ = ["_Ind", "_Prtry"]
	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if value is not None else base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = base_types.UninitialisedField(self, 'Ind', YesNoIndicator, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))