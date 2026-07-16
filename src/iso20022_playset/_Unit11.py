# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ISODate
from . import Max35Text
from . import OtherAmount1
from . import TotalFeesAndTaxes41
from . import UKTaxGroupUnit1Code
from . import UnitPrice23

class Unit11(base_types._BaseFieldType):

	__slots__ = ["_AcqstnDt", "_CertNb", "_Grp1Or2Units", "_OrdrDt", "_OthrAmt", "_PricDtls", "_Ref", "_TxOvrhd", "_UnitsNb"]
	@property
	def AcqstnDt(self):
		return self._AcqstnDt

	@AcqstnDt.setter
	def AcqstnDt(self, value):
		self._AcqstnDt = value if value is not None else base_types.UninitialisedField(self, 'AcqstnDt', ISODate, False)

	@AcqstnDt.deleter
	def AcqstnDt(self):
		del self._AcqstnDt
		self._AcqstnDt = base_types.UninitialisedField(self, 'AcqstnDt', ISODate, False)

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', Max35Text, True)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', Max35Text, True)

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if value is not None else base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@property
	def OrdrDt(self):
		return self._OrdrDt

	@OrdrDt.setter
	def OrdrDt(self, value):
		self._OrdrDt = value if value is not None else base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@OrdrDt.deleter
	def OrdrDt(self):
		del self._OrdrDt
		self._OrdrDt = base_types.UninitialisedField(self, 'OrdrDt', ISODate, False)

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if value is not None else base_types.UninitialisedField(self, 'OthrAmt', OtherAmount1, True)

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = base_types.UninitialisedField(self, 'OthrAmt', OtherAmount1, True)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', UnitPrice23, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', UnitPrice23, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if value is not None else base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes41, False)

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes41, False)

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if value is not None else base_types.UninitialisedField(self, 'UnitsNb', DecimalNumber, False)

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = base_types.UninitialisedField(self, 'UnitsNb', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqstnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))