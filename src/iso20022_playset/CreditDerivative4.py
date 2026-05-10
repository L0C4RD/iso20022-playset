from . import base_types
from .Max35Text import Max35Text
from .TrancheIndicator3Choice import TrancheIndicator3Choice
from .DebtInstrumentSeniorityType2Code import DebtInstrumentSeniorityType2Code
from .Number import Number
from .PercentageRate import PercentageRate
from .Frequency13Code import Frequency13Code
from .DerivativePartyIdentification1Choice import DerivativePartyIdentification1Choice

class CreditDerivative4(base_types._BaseFieldType):

	__slots__ = ["_Trch", "_RefPty", "_PmtFrqcy", "_ClctnBsis", "_Vrsn", "_Snrty", "_Srs", "_IndxFctr"]
	@property
	def Trch(self):
		return self._Trch

	@Trch.setter
	def Trch(self, value):
		self._Trch = value if type(value) != auto else self.make_default("Trch")

	@Trch.deleter
	def Trch(self):
		del self._Trch
		self._Trch = None

	@property
	def RefPty(self):
		return self._RefPty

	@RefPty.setter
	def RefPty(self, value):
		self._RefPty = value if type(value) != auto else self.make_default("RefPty")

	@RefPty.deleter
	def RefPty(self):
		del self._RefPty
		self._RefPty = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if type(value) != auto else self.make_default("ClctnBsis")

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def Snrty(self):
		return self._Snrty

	@Snrty.setter
	def Snrty(self, value):
		self._Snrty = value if type(value) != auto else self.make_default("Snrty")

	@Snrty.deleter
	def Snrty(self):
		del self._Snrty
		self._Snrty = None

	@property
	def Srs(self):
		return self._Srs

	@Srs.setter
	def Srs(self, value):
		self._Srs = value if type(value) != auto else self.make_default("Srs")

	@Srs.deleter
	def Srs(self):
		del self._Srs
		self._Srs = None

	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if type(value) != auto else self.make_default("IndxFctr")

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trch', type=TrancheIndicator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPty', type=DerivativePartyIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnBsis', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Snrty', type=DebtInstrumentSeniorityType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

