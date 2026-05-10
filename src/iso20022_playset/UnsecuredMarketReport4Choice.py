from . import base_types
from .ReportPeriodActivity3Code import ReportPeriodActivity3Code
from .UnsecuredMarketTransaction4 import UnsecuredMarketTransaction4

class UnsecuredMarketReport4Choice(base_types._BaseFieldType):

	__slots__ = ["_Tx", "_DataSetActn"]
	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def DataSetActn(self):
		return self._DataSetActn

	@DataSetActn.setter
	def DataSetActn(self, value):
		self._DataSetActn = value if type(value) != auto else self.make_default("DataSetActn")

	@DataSetActn.deleter
	def DataSetActn(self):
		del self._DataSetActn
		self._DataSetActn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tx', type=UnsecuredMarketTransaction4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='DataSetActn', type=ReportPeriodActivity3Code, min=0, max=1, mutex_group=1, array=False),
	))

