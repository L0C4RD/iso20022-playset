from . import base_types
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._Max256Text import Max256Text

class ProprietaryStatusJustification2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_PrtryStsRsn"]
	@property
	def PrtryStsRsn(self):
		return self._PrtryStsRsn

	@PrtryStsRsn.setter
	def PrtryStsRsn(self, value):
		self._PrtryStsRsn = value if type(value) != base_types.auto else self.make_default("PrtryStsRsn")

	@PrtryStsRsn.deleter
	def PrtryStsRsn(self):
		del self._PrtryStsRsn
		self._PrtryStsRsn = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryStsRsn', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))

