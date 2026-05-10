import base_types
import ISOTime
import ISODate
import AccountStatementDetails3

class AccountStatementData3(base_types._BaseFieldType):

	__slots__ = ["_Tm", "_Dt", "_Dtls"]
	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

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

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if type(value) != auto else self.make_default("Dtls")

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=AccountStatementDetails3, min=0, max=None, mutex_group=None, array=True),
	))

