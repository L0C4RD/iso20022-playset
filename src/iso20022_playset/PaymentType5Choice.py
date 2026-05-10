from . import base_types
import PaymentType4Code
import Max4AlphaNumericText

class PaymentType5Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_PrtryTp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PrtryTp(self):
		return self._PrtryTp

	@PrtryTp.setter
	def PrtryTp(self, value):
		self._PrtryTp = value if type(value) != auto else self.make_default("PrtryTp")

	@PrtryTp.deleter
	def PrtryTp(self):
		del self._PrtryTp
		self._PrtryTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=PaymentType4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryTp', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
	))

