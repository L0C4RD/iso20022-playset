# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification47
from . import YesNoIndicator

class TemporaryFinancialInstrumentIndicator4Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_TempInd"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification47, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification47, False)

	@property
	def TempInd(self):
		return self._TempInd

	@TempInd.setter
	def TempInd(self, value):
		self._TempInd = value if value is not None else base_types.UninitialisedField(self, 'TempInd', YesNoIndicator, False)

	@TempInd.deleter
	def TempInd(self):
		del self._TempInd
		self._TempInd = base_types.UninitialisedField(self, 'TempInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TempInd', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))