# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportPeriodActivity3Code
from . import UnsecuredMarketTransaction4

class UnsecuredMarketReport4Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSetActn", "_Tx"]
	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if value is not None else base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity3Code, False)

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = base_types.UninitialisedField(self, 'DataSetActn', ReportPeriodActivity3Code, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', UnsecuredMarketTransaction4, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', UnsecuredMarketTransaction4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tx', type=UnsecuredMarketTransaction4, min=1, max=None, mutex_group=1, array=True),
	))