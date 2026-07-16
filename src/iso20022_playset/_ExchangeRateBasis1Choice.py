# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExchangeRateBasis1
from . import Max52Text

class ExchangeRateBasis1Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyPair", "_Prtry"]
	@property
	def CcyPair(self):
		return self._CcyPair

	@CcyPair.setter
	def CcyPair(self, value):
		self._CcyPair = value if value is not None else base_types.UninitialisedField(self, 'CcyPair', ExchangeRateBasis1, False)

	@CcyPair.deleter
	def CcyPair(self):
		del self._CcyPair
		self._CcyPair = base_types.UninitialisedField(self, 'CcyPair', ExchangeRateBasis1, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max52Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyPair', type=ExchangeRateBasis1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
	))