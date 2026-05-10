import base_types
import Undertaking1
import Max2000Text
import PartyAndSignature2

class UndertakingApplicationV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgApplDtls", "_InstrsToBk", "_DgtlSgntr"]
	@property
	def UdrtkgApplDtls(self):
		return self._UdrtkgApplDtls

	@UdrtkgApplDtls.setter
	def UdrtkgApplDtls(self, value):
		self._UdrtkgApplDtls = value if type(value) != auto else self.make_default("UdrtkgApplDtls")

	@UdrtkgApplDtls.deleter
	def UdrtkgApplDtls(self):
		del self._UdrtkgApplDtls
		self._UdrtkgApplDtls = None

	@property
	def InstrsToBk(self):
		return self._InstrsToBk

	@InstrsToBk.setter
	def InstrsToBk(self, value):
		self._InstrsToBk = value if type(value) != auto else self.make_default("InstrsToBk")

	@InstrsToBk.deleter
	def InstrsToBk(self):
		del self._InstrsToBk
		self._InstrsToBk = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgApplDtls', type=Undertaking1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrsToBk', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

