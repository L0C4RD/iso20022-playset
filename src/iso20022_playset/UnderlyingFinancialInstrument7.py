from . import base_types
import FinancialInstrumentAttributes124
import SecurityIdentification19

class UnderlyingFinancialInstrument7(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Attrbts"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Attrbts(self):
		return self._Attrbts

	@Attrbts.setter
	def Attrbts(self, value):
		self._Attrbts = value if type(value) != auto else self.make_default("Attrbts")

	@Attrbts.deleter
	def Attrbts(self):
		del self._Attrbts
		self._Attrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attrbts', type=FinancialInstrumentAttributes124, min=0, max=1, mutex_group=None, array=False),
	))

