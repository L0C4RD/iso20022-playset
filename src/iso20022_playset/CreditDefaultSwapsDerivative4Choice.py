import base_types
import CreditDefaultSwapDerivative6
import CreditDefaultSwapSingleName2
import CreditDefaultSwapIndex3
import CreditDefaultSwapDerivative5

class CreditDefaultSwapsDerivative4Choice(base_types._BaseFieldType):

	__slots__ = ["_SnglNmCdtDfltSwp", "_CdtDfltSwpIndx", "_CdtDfltSwpIndxDeriv", "_SnglNmCdtDfltSwpDeriv"]
	@property
	def SnglNmCdtDfltSwp(self):
		return self._SnglNmCdtDfltSwp

	@SnglNmCdtDfltSwp.setter
	def SnglNmCdtDfltSwp(self, value):
		self._SnglNmCdtDfltSwp = value if type(value) != auto else self.make_default("SnglNmCdtDfltSwp")

	@SnglNmCdtDfltSwp.deleter
	def SnglNmCdtDfltSwp(self):
		del self._SnglNmCdtDfltSwp
		self._SnglNmCdtDfltSwp = None

	@property
	def CdtDfltSwpIndx(self):
		return self._CdtDfltSwpIndx

	@CdtDfltSwpIndx.setter
	def CdtDfltSwpIndx(self, value):
		self._CdtDfltSwpIndx = value if type(value) != auto else self.make_default("CdtDfltSwpIndx")

	@CdtDfltSwpIndx.deleter
	def CdtDfltSwpIndx(self):
		del self._CdtDfltSwpIndx
		self._CdtDfltSwpIndx = None

	@property
	def CdtDfltSwpIndxDeriv(self):
		return self._CdtDfltSwpIndxDeriv

	@CdtDfltSwpIndxDeriv.setter
	def CdtDfltSwpIndxDeriv(self, value):
		self._CdtDfltSwpIndxDeriv = value if type(value) != auto else self.make_default("CdtDfltSwpIndxDeriv")

	@CdtDfltSwpIndxDeriv.deleter
	def CdtDfltSwpIndxDeriv(self):
		del self._CdtDfltSwpIndxDeriv
		self._CdtDfltSwpIndxDeriv = None

	@property
	def SnglNmCdtDfltSwpDeriv(self):
		return self._SnglNmCdtDfltSwpDeriv

	@SnglNmCdtDfltSwpDeriv.setter
	def SnglNmCdtDfltSwpDeriv(self, value):
		self._SnglNmCdtDfltSwpDeriv = value if type(value) != auto else self.make_default("SnglNmCdtDfltSwpDeriv")

	@SnglNmCdtDfltSwpDeriv.deleter
	def SnglNmCdtDfltSwpDeriv(self):
		del self._SnglNmCdtDfltSwpDeriv
		self._SnglNmCdtDfltSwpDeriv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglNmCdtDfltSwp', type=CreditDefaultSwapSingleName2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtDfltSwpIndx', type=CreditDefaultSwapIndex3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtDfltSwpIndxDeriv', type=CreditDefaultSwapDerivative5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglNmCdtDfltSwpDeriv', type=CreditDefaultSwapDerivative6, min=0, max=1, mutex_group=1, array=False),
	))

