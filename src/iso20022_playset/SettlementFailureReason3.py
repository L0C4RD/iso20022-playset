import base_types
import Max2Fraction1NonNegativeNumber
import SettlementFailureReason2

class SettlementFailureReason3(base_types._BaseFieldType):

	__slots__ = ["_AvrgDrtn", "_Desc"]
	@property
	def AvrgDrtn(self):
		return self._AvrgDrtn

	@AvrgDrtn.setter
	def AvrgDrtn(self, value):
		self._AvrgDrtn = value if type(value) != auto else self.make_default("AvrgDrtn")

	@AvrgDrtn.deleter
	def AvrgDrtn(self):
		del self._AvrgDrtn
		self._AvrgDrtn = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgDrtn', type=Max2Fraction1NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=SettlementFailureReason2, min=1, max=None, mutex_group=None, array=True),
	))

