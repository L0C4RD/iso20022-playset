# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Price7
from . import ProprietaryPrice2

class TransactionPrice4Choice(base_types._BaseFieldType):

	__slots__ = ["_DealPric", "_Prtry"]
	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price7, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price7, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryPrice2, True)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryPrice2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DealPric', type=Price7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryPrice2, min=1, max=None, mutex_group=1, array=True),
	))