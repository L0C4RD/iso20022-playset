import base_types
import SettlementDateCode9Choice
import DateAndDateTime2Choice

class SettlementDate20Choice(base_types._BaseFieldType):

	__slots__ = ["_DtCd", "_Dt"]
	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if type(value) != auto else self.make_default("DtCd")

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtCd', type=SettlementDateCode9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
	))

