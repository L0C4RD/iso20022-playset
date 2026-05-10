from . import base_types
from ._AmountAndDirection49 import AmountAndDirection49
from ._CalculationMethod1Code import CalculationMethod1Code
from ._Frequency38Choice import Frequency38Choice
from ._Max3NumericText import Max3NumericText

class CollateralAmount12(base_types._BaseFieldType):

	__slots__ = ["_Acrd", "_CmpndSmplAcrlClctn", "_IntrstPmtDely", "_PmtFrqcy", "_Termntn", "_Tx", "_ValSght"]
	@property
	def Acrd(self):
		return self._Acrd

	@Acrd.setter
	def Acrd(self, value):
		self._Acrd = value if type(value) != base_types.auto else self.make_default("Acrd")

	@Acrd.deleter
	def Acrd(self):
		del self._Acrd
		self._Acrd = None

	@property
	def CmpndSmplAcrlClctn(self):
		return self._CmpndSmplAcrlClctn

	@CmpndSmplAcrlClctn.setter
	def CmpndSmplAcrlClctn(self, value):
		self._CmpndSmplAcrlClctn = value if type(value) != base_types.auto else self.make_default("CmpndSmplAcrlClctn")

	@CmpndSmplAcrlClctn.deleter
	def CmpndSmplAcrlClctn(self):
		del self._CmpndSmplAcrlClctn
		self._CmpndSmplAcrlClctn = None

	@property
	def IntrstPmtDely(self):
		return self._IntrstPmtDely

	@IntrstPmtDely.setter
	def IntrstPmtDely(self, value):
		self._IntrstPmtDely = value if type(value) != base_types.auto else self.make_default("IntrstPmtDely")

	@IntrstPmtDely.deleter
	def IntrstPmtDely(self):
		del self._IntrstPmtDely
		self._IntrstPmtDely = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if type(value) != base_types.auto else self.make_default("Termntn")

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def ValSght(self):
		return self._ValSght

	@ValSght.setter
	def ValSght(self, value):
		self._ValSght = value if type(value) != base_types.auto else self.make_default("ValSght")

	@ValSght.deleter
	def ValSght(self):
		del self._ValSght
		self._ValSght = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acrd', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpndSmplAcrlClctn', type=CalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtDely', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termntn', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSght', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
	))

