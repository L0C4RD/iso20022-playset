import base_types
import NoReasonCode
import Tranche3

class TrancheIndicator3Choice(base_types._BaseFieldType):

	__slots__ = ["_Trnchd", "_Utrnchd"]
	@property
	def Trnchd(self):
		return self._Trnchd

	@Trnchd.setter
	def Trnchd(self, value):
		self._Trnchd = value if type(value) != auto else self.make_default("Trnchd")

	@Trnchd.deleter
	def Trnchd(self):
		del self._Trnchd
		self._Trnchd = None

	@property
	def Utrnchd(self):
		return self._Utrnchd

	@Utrnchd.setter
	def Utrnchd(self, value):
		self._Utrnchd = value if type(value) != auto else self.make_default("Utrnchd")

	@Utrnchd.deleter
	def Utrnchd(self):
		del self._Utrnchd
		self._Utrnchd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trnchd', type=Tranche3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Utrnchd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

