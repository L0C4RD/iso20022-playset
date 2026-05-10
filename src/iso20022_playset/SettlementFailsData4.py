import base_types
import SettlementFailureReason3
import SettlementFailsDerogation1
import SettlementTotalData1

class SettlementFailsData4(base_types._BaseFieldType):

	__slots__ = ["_FailrRsn", "_ElgblForDrgtn", "_Ttl"]
	@property
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if type(value) != auto else self.make_default("FailrRsn")

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = None

	@property
	def ElgblForDrgtn(self):
		return self._ElgblForDrgtn

	@ElgblForDrgtn.setter
	def ElgblForDrgtn(self, value):
		self._ElgblForDrgtn = value if type(value) != auto else self.make_default("ElgblForDrgtn")

	@ElgblForDrgtn.deleter
	def ElgblForDrgtn(self):
		del self._ElgblForDrgtn
		self._ElgblForDrgtn = None

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if type(value) != auto else self.make_default("Ttl")

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FailrRsn', type=SettlementFailureReason3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblForDrgtn', type=SettlementFailsDerogation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
	))

