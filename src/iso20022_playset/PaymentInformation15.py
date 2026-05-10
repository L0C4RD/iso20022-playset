from . import base_types
import PaymentMethod4Code
import CashAccount7

class PaymentInformation15(base_types._BaseFieldType):

	__slots__ = ["_PmtMtd", "_PmtAcct"]
	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	@property
	def PmtAcct(self):
		return self._PmtAcct

	@PmtAcct.setter
	def PmtAcct(self, value):
		self._PmtAcct = value if type(value) != auto else self.make_default("PmtAcct")

	@PmtAcct.deleter
	def PmtAcct(self):
		del self._PmtAcct
		self._PmtAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
	))

