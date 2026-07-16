# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EUCapitalGain2Code
from . import GenericIdentification30

class EUCapitalGainType3Choice(base_types._BaseFieldType):

	__slots__ = ["_EUCptlGn", "_Prtry"]
	@property
	def EUCptlGn(self):
		return self._EUCptlGn

	@EUCptlGn.setter
	def EUCptlGn(self, value):
		self._EUCptlGn = value if value is not None else base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain2Code, False)

	@EUCptlGn.deleter
	def EUCptlGn(self):
		del self._EUCptlGn
		self._EUCptlGn = base_types.UninitialisedField(self, 'EUCptlGn', EUCapitalGain2Code, False)

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
		base_types.FieldEntry(name='EUCptlGn', type=EUCapitalGain2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))