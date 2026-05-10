import base_types
import ATMContext26
import ATMEnvironment17
import ATMTransaction42

class ATMInquiryRequest3(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Cntxt", "_Tx"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=ATMEnvironment17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=ATMContext26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=ATMTransaction42, min=1, max=1, mutex_group=None, array=False),
	))

