import base_types
import ActiveCurrencyAndAmount
import CollateralMovement6Choice

class CollateralMovement12(base_types._BaseFieldType):

	__slots__ = ["_AgrdAmt", "_MvmntDrctn"]
	@property
	def AgrdAmt(self):
		return self._AgrdAmt

	@AgrdAmt.setter
	def AgrdAmt(self, value):
		self._AgrdAmt = value if type(value) != auto else self.make_default("AgrdAmt")

	@AgrdAmt.deleter
	def AgrdAmt(self):
		del self._AgrdAmt
		self._AgrdAmt = None

	@property
	def MvmntDrctn(self):
		return self._MvmntDrctn

	@MvmntDrctn.setter
	def MvmntDrctn(self, value):
		self._MvmntDrctn = value if type(value) != auto else self.make_default("MvmntDrctn")

	@MvmntDrctn.deleter
	def MvmntDrctn(self):
		del self._MvmntDrctn
		self._MvmntDrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntDrctn', type=CollateralMovement6Choice, min=0, max=None, mutex_group=None, array=True),
	))

