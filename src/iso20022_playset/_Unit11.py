from . import base_types
from .Max35Text import Max35Text
from .UKTaxGroupUnit1Code import UKTaxGroupUnit1Code
from .ISODate import ISODate
from .UnitPrice23 import UnitPrice23
from .DecimalNumber import DecimalNumber
from .TotalFeesAndTaxes41 import TotalFeesAndTaxes41
from .OtherAmount1 import OtherAmount1

class Unit11(base_types._BaseFieldType):

	__slots__ = ["_OrdrDt", "_AcqstnDt", "_Ref", "_TxOvrhd", "_PricDtls", "_OthrAmt", "_Grp1Or2Units", "_CertNb", "_UnitsNb"]
	@property
	def OrdrDt(self):
		return self._OrdrDt

	@OrdrDt.setter
	def OrdrDt(self, value):
		self._OrdrDt = value if type(value) != base_types.auto else self.make_default("OrdrDt")

	@OrdrDt.deleter
	def OrdrDt(self):
		del self._OrdrDt
		self._OrdrDt = None

	@property
	def AcqstnDt(self):
		return self._AcqstnDt

	@AcqstnDt.setter
	def AcqstnDt(self, value):
		self._AcqstnDt = value if type(value) != base_types.auto else self.make_default("AcqstnDt")

	@AcqstnDt.deleter
	def AcqstnDt(self):
		del self._AcqstnDt
		self._AcqstnDt = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if type(value) != base_types.auto else self.make_default("TxOvrhd")

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if type(value) != base_types.auto else self.make_default("OthrAmt")

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = None

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if type(value) != base_types.auto else self.make_default("Grp1Or2Units")

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = None

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqstnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))

